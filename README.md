# FastAPI Service

This project is a FastAPI application designed to provide an lightweight LLM service.


## Project Structure

```
lite-llm
├── app
│   ├── main.py          # Entry point of the FastAPI application
│   ├── routers          # Contains route definitions
│   ├── models           # Contains data models
│   ├── services         # Contains business logic
│   └── utils            # Contains utility functions
├── requirements.txt     # Lists project dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd lite-llm
   ```

1. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the FastAPI application, use the following command:

```
uvicorn app.main:app --reload
```

You can access the API documentation at `http://127.0.0.1:8000/docs`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License.