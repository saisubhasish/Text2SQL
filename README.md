# Text-to-SQL Converter
## Architecture
![Screenshot 2024-08-30 100736](https://github.com/user-attachments/assets/c04893ce-c91c-4ad9-a800-43699208de4c)
## User Interface
![Screenshot 2024-08-30 190919](https://github.com/user-attachments/assets/772b5a3a-68ad-43ec-acd6-7a915cceefa0)


## Overview
This project implements a Text-to-SQL converter using Llama2, deployed on Amazon SageMaker, with a Streamlit frontend. It allows users to input natural language queries and receive corresponding SQLite3 SQL queries.

## Components

1. **SageMaker Notebook (`sagemaker.ipynb`)**: 
   - Sets up the SageMaker environment
   - Deploys the Llama2 model
   - Provides functions for prompt engineering and model interaction

2. **Lambda Function**:
   - Serves as an intermediary between the frontend and SageMaker endpoint
   - Processes requests and formats responses

3. **Streamlit App (`app.py`)**:
   - Provides a user-friendly interface for inputting queries and displaying results

## Setup Instructions

### 1. SageMaker Setup
1. Open the `sagemaker.ipynb` notebook in SageMaker.
2. Run all cells to set up the environment, Huggingface token and deploy the model.
3. Note the endpoint name generated for use in the Lambda function.

### 2. Lambda Function Setup
1. Create a new Lambda function in AWS.
2. Copy the provided Lambda function code into the function.
3. Replace the `ENDPOINT` variable with your SageMaker endpoint name.
4. Set up appropriate IAM roles for Lambda to access SageMaker.

### 3. API Gateway Setup
1. Create a new API in API Gateway.
2. Set up a GET method and link it to your Lambda function.
3. Deploy the API and note the invoke URL.

### 4. Streamlit App Setup
1. Create a virtual environment `conda create -p venv python=3.10 -y`
                                `conda activate venv/` 
2. Install required packages: `pip install streamlit requests`
3. Update the `ENDPOINT_URL` in `app.py` with your API Gateway invoke URL.
4. Ensure the `src/logger.py` file is present for logging functionality.

## Usage

1. Start the Streamlit app:
   ```
   streamlit run app.py
   ```
2. Open the provided URL in your web browser.
3. Enter your natural language query in the text area.
4. Click "Convert to SQL" to get the corresponding SQL query.

## Testing

### Lambda Function Test
Use the following JSON to test your Lambda function:

```json
{
  "httpMethod": "GET",
  "path": "/example",
  "queryStringParameters": {
    "query": "Find all user who live in California and have over 1000 credits"
  }
}
```

## Logging

The application uses a custom logger. Ensure that `src/logger.py` is properly configured for your logging needs.

## Notes

- The Llama2 model used is "NousResearch/Llama-2-7b-chat-hf".
- The SageMaker endpoint uses a `ml.g5.2xlarge` instance.
- Adjust the model parameters in the Lambda function as needed for different results.

## Security

- Ensure that your Hugging Face Hub token is kept secure and not exposed in the code.
- Properly configure IAM roles and permissions for AWS services.

## Future Improvements

- Implement better error handling and user feedback.
- Add support for more complex SQL queries and different database types.
- Enhance the UI for a better user experience.
