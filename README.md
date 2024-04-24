# Sentimental Analysis API

##### Hugging Face, FastAPI and Dockers

## Overview

This document provides the necessary instructions to set up and run the FastAPI application which uses a Hugging Face Transformer model for sentiment analysis. This application is containerized using Docker.

## Dependencies

The project relies on the following dependencies:

- FastAPI: A modern web framework for building APIs with Python.
- Transformers: The Hugging Face library for natural language processing (NLP) tasks, including pre-trained models.
- Pyngrok: A Python wrapper for ngrok, which exposes local servers over public URLs.
- Nest_asyncio: A library for running asyncio nested in other asyncio loops.
- NLTK: The Natural Language Toolkit for text processing tasks.
- Pydantic: A data validation library for Python.

## Model Used

It uses the following pre-trained transformer model from Hugging Face: 
**cardiffnlp/twitter-roberta-base-sentiment-latest**.

It classifies the text as *positive*, *negative*, or *neutral*

## Installation 

To install and run the API locally, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Docker installed.
3. Build the Docker container using the provided Dockerfile.
4. Run the Docker container.

## Building and Running the Docker Container

To construct and launch the Docker container, execute these steps:

1. Move to the directory containing your FastAPI application.
2. Create a Docker image with this command:

```
docker build -t sentimental-analysis-api .
```
4. Containerize the application by creating a Docker container from the built image
```
docker run -p 8000:8000 sentimental-analysis-api
```
5. Access the API using the URL http://localhost:8000.
6. Explore the API documentation at http://localhost:8000/docs or http://localhost:8000/redoc.

## API Endpoints

- **GET /:** A welcome endpoint that redirects to the Swagger UI page.
- **POST /analyze:** The endpoint for sentimental Analysis. It accepts JSON input with a text field and returns the sentimental analysis results.

## Testing the API
```
pytest
```
Use this command where your test.py is located it will automatically run the predefined test cases.

## Interacting with API

You can interact with the API using the Swagger UI or by making HTTP requests from tools like curl or Postman.

## License

This project is licensed under the apache - 2.0 License.
 
