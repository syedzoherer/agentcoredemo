from bedrock_agentcore_starter_toolkit import Runtime
from boto3.session import Session
boto_session = Session()

agent_runtime=Runtime()

agent_name="core_demo"

response = agent_runtime.configure(
    entrypoint="agent.py",
    auto_create_execution_role=True,
    auto_create_ecr=True,
    requirements_file="requirements.txt",
    region="us-west-2",
    agent_name=agent_name
)

launch_result = agent_runtime.launch(env_vars={"OTEL_PYTHON_EXCLUDED_URLS": "/ping,/invocations"})
