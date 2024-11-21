import os
import ollama
import streamlit as st
from PIL import Image

# Constants
UPLOAD_FOLDER = "uploads"
SYSTEM_PROMPT = """Act as an OCR assistant. Analyze the provided image and:
1. Recognize all visible text in the image as accurately as possible.
2. Maintain the original structure and formatting of the text.
3. If any words or phrases are unclear, indicate this with [unclear] in your transcription.
Provide only the transcription without any additional comments."""

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def perform_ocr(image_path):
    """Perform OCR on the given image using Llama 3.2-Vision through the Ollama library."""
    try:
        response = ollama.chat(
            model='llama3.2-vision',
            messages=[{
                'role': 'user',
                'content': SYSTEM_PROMPT,
                'images': [image_path]
            }]
        )
        return response.get('message', {}).get('content', "")
    except Exception as e:
        st.error(f"An error occurred during OCR processing: {e}")
        return None

# Streamlit app
st.set_page_config(
    page_title="LlamaOCR - Local OCR Tool",
    page_icon="📄",
    layout="centered"
)

st.title("📄 LlamaOCR - Local OCR Tool")
st.write("Effortlessly extract text from images using the power of **Llama 3.2-Vision**. Upload an image to get started!")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png", "gif"])

if uploaded_file:
    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display uploaded image
    st.subheader("Uploaded Image:")
    image = Image.open(file_path)
    st.image(image, caption="Your Uploaded Image", use_column_width=True)

    # Perform OCR
    with st.spinner("Performing OCR..."):
        ocr_result = perform_ocr(file_path)

    if ocr_result:
        st.subheader("OCR Result:")
        st.text_area("Extracted Text", ocr_result, height=200)
    else:
        st.error("OCR failed. Please try again.")
else:
    st.info("Please upload an image to begin.")

# Add footer
st.markdown(
    """
    ---
    **LlamaOCR** | Built with ❤️ using [Streamlit](https://streamlit.io) and **Llama 3.2-Vision**.
    """
)
