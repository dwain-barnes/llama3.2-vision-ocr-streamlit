# Private Local OCR with Llama 3.2 Vision and Streamlit

![logo](Local_OCR.png)

Welcome to the Private Local OCR project! This tool leverages Meta's Llama 3.2 Vision model via the Ollama platform, providing a user-friendly Streamlit interface for efficient and private text extraction from images. It was made as a part of a blog series [here](https://www.gpt-labs.ai/post/private-local-llamaocr-with-a-user-friendly-streamlit-front-end)

## Features

- **Local OCR Processing**: Perform OCR tasks entirely on your local machine, ensuring data privacy and eliminating the need for internet connectivity.
- **Advanced Vision Model**: Utilize Meta's Llama 3.2 Vision model for accurate text extraction.
- **User-Friendly Interface**: Interact seamlessly through a Streamlit-based front-end, allowing easy image uploads and text viewing.
- **Support for Various Image Formats**: Process multiple image formats, including JPEG, PNG, and BMP.
- **Extensible Architecture**: Easily integrate additional functionalities or models as needed.

## Prerequisites

- **Ollama Platform**: Ensure the Ollama platform is installed and configured on your machine to access the Llama 3.2 Vision model.
- **Python 10 or Higher**: Verify that Python is installed on your system.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/dwain-barnes/llama3.2-vision-ocr-streamlit.git
    cd LlamaOCR-Streamlit
    ```

2. **Set Up a Virtual Environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit Application**:
    ```bash
    streamlit run app.py
    ```

2. **Access the Interface**:
    Open your web browser and navigate to `http://localhost:8501` to access the application.

3. **Upload and Process Images**:
    - Use the "Browse files" button to upload an image.
    - Click the "Process" button to extract text from the uploaded image using the Llama 3.2 Vision model via Ollama.
    - View the extracted text displayed on the interface.

## Dependencies

- Python 10 or higher
- Streamlit
- Ollama
- Pillow


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to Meta for developing the Llama 3.2 Vision model and to the Ollama platform for providing access to advanced AI models. Their work has been instrumental in the development of this project.
