# FastAPI Service

This project is a FastAPI application designed to provide an lightweight LLM service.


## Project Structure

```
lite-llm
├── api
│   ├── index.py         # Contains serverless functions for Vercel
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
   git clone git@github.com:kuloud/lite-llm.git
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

## API Documentation
You can access the interactive API documentation provided by FastAPI at the following URLs:

Swagger UI: https://lite-llm.vercel.app/docs
ReDoc: https://lite-llm.vercel.app/redoc

## Deployment on Vercel

This project is deployed on Vercel and uses the Python runtime with Serverless Functions. The FastAPI app is accessible at:

**Base URL**: `https://lite-llm.vercel.app`

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

## WebSocket Endpoints

### `/ws`
This WebSocket endpoint is used to interact with GitHub models.

#### Connection
To establish a WebSocket connection, use the following URL:
```plaintext
ws://your - server - address/ws/github - model

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License.