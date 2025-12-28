import json
import uuid
import boto3

agent_arn = "arn:aws:bedrock-agentcore:us-west-2:028195660756:runtime/core_demo-rorP9g76dQ"
prompt = "Tell me a joke"

# Initialize the Amazon Bedrock AgentCore client
agent_core_client = boto3.client('bedrock-agentcore', region_name="us-west-2")

# Prepare the payload
payload = json.dumps({"prompt": prompt}).encode()

# Invoke the agent
response = agent_core_client.invoke_agent_runtime(
    agentRuntimeArn=agent_arn,
    runtimeSessionId=str(uuid.uuid4()),
    payload=payload,
    qualifier="DEFAULT"
)

print(response)

content = []
for chunk in response.get("response", []):
    print(chunk)
