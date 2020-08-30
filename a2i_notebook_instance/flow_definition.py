"""Creates a FLow Definition ARN for A2I"""
import boto3
import io
import json
import uuid
import botocore
import time
import botocore
from sagemaker import get_execution_role


ROLE = get_execution_role()
REGION = ""
WORKTEAM_ARN = ""
HUMAN_TASK_ARN = ""
BUCKET = ""
OUTPUT_PATH = f's3://{BUCKET}/a2i_results'

def create_flow_definition(flow_definition_name, human_task_arn, task_title):
    '''
    Creates Flow Definition resource.
    Returns FlowDefinitionArn
    '''
    # Amazon SageMaker client
    SAGEMAKER_CLIENT = boto3.client('sagemaker', REGION)
    
    # A2I Runtime client
    A2I_RUNTIME_CLIENT = boto3.client('sagemaker-a2i-runtime', REGION)

    response = SAGEMAKER_CLIENT.create_flow_definition(
    FlowDefinitionName = flow_definition_name,
    RoleArn = ROLE,
    HumanLoopConfig = {
    'WorkteamArn': WORKTEAM_ARN,
    'HumanTaskUiArn': human_task_arn,
    'TaskCount': 1,
    'TaskDescription': "Rate for " + task_title,
    'TaskTitle': task_title
    },
    OutputConfig = {
    'S3OutputPath' : OUTPUT_PATH
        }
    )
    return response['FlowDefinitionArn']


def main():
    flow_definition_name = ""
    task_title = ""

    flow_defintiion_arn = create_flow_definition(flow_definition_name, 
                                            HUMAN_TASK_ARN, task_title)
    print(flow_defintiion_arn)


if __name__ == "__main__":
    main()