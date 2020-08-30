import os
import uuid

#Fetching the environment variables
#REGION = os.environ['REGION']
WORKER_FLOW_ARN = os.environ['WORKER_FLOW_LOAN']
HUMAN_TASK_ARN = os.environ['HUMAN_TASK_ARN']


BUCKET = ""
ROLE = ""
TASK_TITLE = "Review"
