import boto3
import botocore
import json
from config import REGION, OUTPUT_PATH, ROLE

def call_a2i(human_loop_name, flow_definition_arn, ip_content):
    """
    Calls the A2I client
    """
    # A2I Runtime client
    A2I_RUNTIME_CLIENT = boto3.client('sagemaker-a2i-runtime', REGION)

    response = A2I_RUNTIME_CLIENT.start_human_loop(
    HumanLoopName=human_loop_name,
    FlowDefinitionArn=flow_definition_arn,
    HumanLoopInput={
        'InputContent': json.dumps(ip_content)
       }
    )

    return response