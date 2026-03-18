# MyTranslator

## Description

MyTranslator is a web-based AI translation tool that leverages advanced Natural Language Processing (NLP) techniques and machine learning models to provide accurate, real-time text translation. Built with FastAPI for the backend and a simple HTML frontend, it supports language detection, translation memory for efficiency, and extensible model management. Ideal for developers, researchers, and users needing reliable multilingual translation capabilities.

## Features

- **Real-Time Translation**: Uses pre-trained transformer models (via Hugging Face Transformers) for high-quality translations.
- **Translation Memory**: Caches translations to avoid redundant processing and improve performance.
- **Automatic Language Detection**: Detects source language using `langdetect`.
- **Text Chunking**: Splits long texts into manageable chunks for efficient processing.
- **RESTful API**: FastAPI-based backend with endpoints for easy integration.
- **Extensible Models**: Modular model manager supporting various NLP models.
- **Web Interface**: Basic HTML frontend for user interaction (expandable with JS/CSS).
- **Experimentation Support**: Jupyter notebooks for testing and prototyping translations.
- **Testing Suite**: Unit tests for validation.

## Project Structure

```
MyTranslator/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── backend/                  # FastAPI application
│   └── app/
│       ├── main.py           # Application entry point
│       ├── config.py         # Configuration settings
│       ├── api/
│       │   └── routes.py     # API endpoints (e.g., /translate)
│       ├── models/           # Translation model management
│       │   ├── model_manager.py    # Handles model loading and selection
│       │   └── translator_model.py # Model-specific logic
│       ├── services/         # Core services
│       │   ├── translation_service.py  # Main translation logic
│       │   └── translation_memory.py   # Caching and memory management
│       └── utils/            # Utility functions
│           ├── language_utils.py      # Language detection helpers
│           ├── supported_languages.py # List of supported languages
│           └── text_utils.py          # Text processing (e.g., chunking)
├── frontend/                 # Web interface
│   └── index.html            # Simple HTML page for translation input/output
├── data/                     # Data storage (e.g., translation memory database)
├── docs/                     # Additional documentation
├── notebooks/                # Jupyter notebooks for experiments
│   └── translation_experiments.ipynb
└── tests/                    # Unit tests
    └── test_translation.py
```

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Steps

1. **Clone the repository**:

   ```
   git clone <repository-url>
   cd MyTranslator
   ```

2. **Install dependencies**:

   ```
   pip install -r requirements.txt
   ```

   This installs key libraries like `transformers`, `torch`, `fastapi`, `uvicorn`, `sentencepiece`, and `langdetect`.

3. **(Optional) Set up a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Usage

### Running the Backend

1. Start the FastAPI server:

   ```
   uvicorn backend.app.main:app --reload
   ```

   - The server will run on `http://127.0.0.1:8000`.
   - Access the interactive API docs at `http://127.0.0.1:8000/docs` (Swagger UI).

2. The backend exposes the following endpoint:
   - **POST /translate**: Translate text.
     - Request body (JSON):
       ```json
       {
         "text": "Hello, world!",
         "target_lang": "es"
       }
       ```
     - Response:
       ```json
       {
         "source_language": "en",
         "translation": "¡Hola, mundo!",
         "from_memory": false
       }
       ```

### Using the Frontend

1. Open `frontend/index.html` in a web browser.
2. (Note: The current HTML file is a placeholder. You may need to add JavaScript for API calls to the backend.)

### Running Experiments

- Open `notebooks/translation_experiments.ipynb` in Jupyter Notebook or VS Code.
- Use it to test models, experiment with translations, or analyze performance.

## Testing

Run the test suite to validate functionality:

```
python -m pytest tests/
```

- Currently includes `test_translation.py` for unit tests on translation services.

## Configuration

- Edit `backend/app/config.py` for settings like model paths, supported languages, or API configurations.
- Translation models are managed in `backend/app/models/`; add new models by extending `ModelManager`.

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Make changes and add tests.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Future Enhancements

- Expand the frontend with JavaScript for dynamic interactions.
- Add authentication and user management.
- Integrate more NLP models or cloud-based translation APIs.
- Implement logging and monitoring for production use.
