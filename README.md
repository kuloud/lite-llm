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
   ```bash
   git clone <repository-url>
   cd lite-llm
   ```
1. Create a virtual environment:
   ```bash
   python3.12 -m venv venv
   ```

1. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
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

## Deployment on Vercel

This project is deployed on Vercel and uses the Python runtime with Serverless Functions. The FastAPI app is accessible at:

**Base URL**: `https://lite-llm.vercel.app/api`

### Example Endpoints

- **Chat with GitHub Models**: `/api/models/chat`
  - **Method**: POST
  - **Request Body**:
    ```json
    {
      "messages": [
        {
          "role": "system",
          "content": "You are a helpful assistant."
        },
        {
          "role": "user",
          "content": "What is the capital of France?"
        }
      ]
    }
    ```
  - **Response**:
    ```json
    {
      "response": "The capital of France is Paris."
    }
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License.