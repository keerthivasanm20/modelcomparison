import vars
import boto3
import json

def call_claude(prompt):
    session = boto3.Session(
    aws_access_key_id= vars.AWS_ACCESS_KEY_ID,
    aws_secret_access_key= vars.AWS_SECRET_ACCESS_KEY,
    region_name='us-east-1'  
    )

    bedrock = session.client('bedrock-runtime')

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 512,
    }

    response = bedrock.invoke_model(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        body=json.dumps(body),
        contentType="application/json"
    )
    print(f"Response status code: {response['ResponseMetadata']['HTTPStatusCode']}")
    print(f"Response content: {response['body'].read()}")
    breakpoint()

    response_body = json.loads(response['body'].read())
    return response_body['content'][0]['text']