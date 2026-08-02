import streamlit as st
import tempfile
from pathlib import Path

from src.core.pdf_loader import PDFLoader
from src.core.text_splitter import TextSplitter
from src.core.embeddings import EmbeddingGenerator
from src.core.vector_store import VectorStoreManager
from src.core.rag_pipeline import RAGPipeline

# Page Configuration
st.set_page_config(
    page_title = "UniMind AI",
    page_icon = "📚",
    layout = "wide"
)

# Title
st.markdown(
  """
  <h1 style='text-align:center;'>
  🤖 UniMind AI
  </h1>

  <p style='text-align:center;color:gray;'>
  Chat with your documents using AI
  </p>

  """,
  unsafe_allow_html=True
 )

st.markdown(
    """
    <style>
    
    .stApp{
        background-color: #0e1117;
        }
        
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
        }
        
        h1 {
            text-align: center;
        }

        /* Step 5: Sidebar styling */

        [data-testid="stSidebar"] {

            background-color: #111827;

      }


      /* Better buttons */

      button {

        border-radius: 10px !important;

     }
     </style>
     """,
     unsafe_allow_html=True
)



if "messages" not in st.session_state:
    st.session_state.messages = []

# Process Button
with st.sidebar:

    st.title("📂 Documents")

    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type="pdf",
        accept_multiple_files=True
    )

    if uploaded_files:

        st.info(
            f"📚 {len(uploaded_files)} PDF(s) uploaded"
        )

    process_button = st.button(
        "📄 Process Documents",
        use_container_width=True
    )

    clear_button = st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    )
    if clear_button:

        st.session_state.messages = []

        st.rerun()

    if "pdf_names" in st.session_state:

      st.divider()

      st.subheader("📚 Active Documents")

      for pdf in st.session_state.pdf_names:
        st.write(
            "📄",
            pdf
        )

# Main chat area
st.header("💬 UniMind Chat")

if len(st.session_state.messages) == 0:

    st.markdown(
        """
          ## Welcome to UniMind 🚀
          
          Upload PDFs and ask questions.
          
          Examples:
          
          - Summarize chapter 1
          - What is EDA?
          - Explain linear regression
          """
        )
    

question = st.chat_input(
    "Message UniMind..."
)

for message in st.session_state.messages:

    if message["role"] == "user":

        with st.chat_message(
            "user",
            avatar="👤"
         ):
            st.write(message["content"])

    else:

        with st.chat_message(
            "assistant",
            avatar="🤖"
         ):
            st.write(message["content"])

if question:

    if "rag" not in st.session_state:

        st.warning("Please upload and process your PDFs first.")

    else:

        # Save user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )


        # Display user message
        with st.chat_message("user"):
            st.write(question)


        # Generate AI response
        with st.chat_message("assistant"):

            response_placeholder = st.empty()

            response_placeholder.markdown(
                "UniMind is thinking..."
            )

            full_response = ""


            response, sources = st.session_state.rag.stream_answer(
                question
            )


            for chunk in response:

                full_response += chunk.content

                response_placeholder.markdown(
                    full_response
                )
             # Show sources
            with st.expander("📚 Sources"):

                for source in sources:

                   st.markdown(
                   f"""
                   📄 **{source['filename']}**

                   Page: {source['page']}  
                   Chunk: {source['chunk_id']}

                   ---
                   """
                 )


        # Save assistant message
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": full_response,
                "sources": sources
            }
        )

        st.rerun()
# Process button action
if process_button:

    if not uploaded_files:
        st.warning("Please upload atleast one PDF.")

    else:

        with st.status(
             "Processing documents...",
              expanded=True
        ) as status:

            st.write("📄 Extracting text...")

            pdf_paths = []

            #Save uploaded files temporarily
              
            for uploaded_file in uploaded_files:

                temp_file = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf"
                )

                temp_file.write(uploaded_file.read())
                temp_file.close()

                pdf_paths.append(
                    {
                        "path": Path(temp_file.name),
                        "filename": uploaded_file.name

                    }
                )

            # Step 1: Load PDFs
            loader = PDFLoader()
            pages = loader.load_pdfs(pdf_paths)

            st.write("✂️ Splitting text into chunks...")

            # Step 2: Split text
            splitter = TextSplitter(
                chunk_size=300,
                chunk_overlap=50
            )

            chunks = splitter.split_text(pages)

            st.write("🧠 Creating embeddings...")

            # Step 3: Generate embeddings
            embedder = EmbeddingGenerator()
            embedded_chunks = embedder.generate_embeddings(chunks)

            st.write("💾 Building vector database...")

            # Step 4: Create vector store
            manager = VectorStoreManager()

            vector_store = manager.create_vector_store(
                embedded_chunks
            )

            # Step 5: Create retriever
            retriever = manager.create_retriever(
               vector_store,
               k=3
            )

            # Create RAG pipeline
            rag = RAGPipeline(retriever)

            # Save in session
            st.session_state.vector_store = vector_store
            st.session_state.rag = rag
            st.session_state.processed = True
            st.session_state.pdf_names = [
                file.name for file in uploaded_files
            ]

        status.update(
           label="Documents processed successfully!",
           state="complete",
           expanded=False
        )

        st.success("Your PDFs are ready! Ask anything 📚")

        st.rerun()