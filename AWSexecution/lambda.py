import json
import boto3

ENDPOINT = "huggingface-pytorch-tgi-inference-2024-08-30-10-43-34-978"
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    query_params = event['queryStringParameters']
    query = query_params.get('query')
    
    payload = {
        "inputs":query,
        "parameters":{
            "do_sample":True,
            "top_p":0.7,
            "temperature":0.8,
            "top_k":50,
            "max_new_tokens":512,
            "repetition_penalty":1.03
            
                }
        }
        
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType="application/json", Body=json.dumps(payload))
    generation = json.loads(response['Body'].read().decode('utf-8'))
    final_response = generation[0]['generated_text']
    
    return {
        'statusCode': 200,
        'headers':{"Access-Control-Allow-Origin":'*'},
        'body': json.dumps(final_response)
    }
