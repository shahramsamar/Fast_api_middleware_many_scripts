# FastAPI Middleware Many Scripts

A Python project demonstrating how to implement and utilize **middleware** in **FastAPI** for various use cases. This project contains several scripts showcasing different middleware functionalities, such as logging, request/response modification, and security enhancements.

## Features

- **Custom Middleware**: Includes examples of custom middleware to modify requests and responses in FastAPI.
- **Request Logging**: Logs incoming requests for auditing or debugging purposes.
- **Response Modifications**: Allows modification of response data before it is sent to the client.
- **Error Handling**: Implements middleware for global exception handling and error response formatting.
- **Cross-Origin Resource Sharing (CORS)**: Configures middleware for handling CORS in FastAPI applications.

## Requirements

- **Python 3.x**
- **FastAPI**
- **Uvicorn** (for running the FastAPI application)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/Fast_api_middleware_many_scripts.git
    cd Fast_api_middleware_many_scripts
    ```

2. **Install Dependencies:**

    If you're using `pip`, run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:

    To run the FastAPI app:

    ```bash
    uvicorn main:app --reload
    ```

### How to Use

1. **Middleware for Logging**:
   - This middleware logs the incoming request details, such as method, URL, and headers.
   - It helps in auditing and debugging by keeping track of requests.

2. **Custom Error Handling Middleware**:
   - Provides a way to catch and handle exceptions globally across your application.
   - Custom error messages can be sent to the client for better clarity.

3. **Modifying Response Data**:
   - Middleware can modify the response before it is sent to the client, such as adding custom headers or formatting the response data.

4. **CORS Middleware**:
   - Includes middleware that sets up CORS policies for the FastAPI app, allowing or denying cross-origin requests.

### Example Usage

1. **Logging Middleware Example**:
   - Every incoming request is logged with method, URL, and headers.

2. **Error Handling Example**:
   - If a route raises an error, a structured error response will be sent to the client.

3. **CORS Setup**:
   - Automatically handles requests from different origins if CORS is enabled in the middleware.

### Project Structure

- `main.py`: Contains the FastAPI application and the various middleware setups.
- `middleware.py`: Includes custom middleware classes for logging, error handling, and response modification.
- `requirements.txt`: Lists necessary libraries such as `FastAPI`, `Uvicorn`, etc.

## Contributing

Feel free to fork the project and submit pull requests for new features, improvements, or bug fixes.

## License

This project is open-source and available for educational purposes.
