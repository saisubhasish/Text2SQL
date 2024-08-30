import json
import boto3

ENDPOINT = "huggingface-pytorch-tgi-inference-2024-08-29-09-21-40-993"
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    # TODO implement
    
    query_params = event['queryStringParameters']
    
    query = query_params.get('query')
    
    payload = {
        "inputs":query,
        "parameters":{
            "do_sample":True,
            "top_p":0.7,
            "temperature":0.3,
            "top_k":50,
            "max_new_tokens":400,
            "repetition_penalty":1.03
                }
        }
        
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType="application/json", Body=json.dumps(payload))
    prediction = json.loads(response['Body'].read().decode('utf-8'))
    final_result = prediction[0]['generated_text']
    
    return {
        'statusCode': 200,
        'body': json.dumps(final_result)
    }
