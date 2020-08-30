"""Initiation of the A2I workflow"""
import boto3
import io
import json
import uuid
import botocore
import time
import os
from config import BUCKET, TASK_TITLE, HUMAN_TASK_ARN, WORKER_FLOW_ARN
from a2i import call_a2i
from format_data import format_data

def lambda_handler(event, context):
    """This function fetches the JSON file contents from the S3 bucket and triggers the A2I workflow"""

    try:
        file_name = event['Records'][0]['s3']['object']['key']

        #Initiate the S3 client
        s3 = boto3.resource('s3')
        content_object = s3.Object(BUCKET, file_name)
        file_content = content_object.get()['Body'].read().decode('utf-8')

        #Format the data as per the requirement of the A2I input
        formatted_data = format_data(file_content)
        
        #JSON input to the A2I workflow
        ip_content = {'Pairs': formatted_data['filtered_content'], 'Images': formatted_data['images'], 'file_data':{"file_name": file_name}}
        flow_definition_arn = WORKER_FLOW_ARN

        #Call the A2I workflow
        HUMAN_LOOP_NAME = file_name
        a2i_response = call_a2i(HUMAN_LOOP_NAME, flow_definition_arn, ip_content)
    
    except Exception as e:
         print(e)
