import os
import uuid

#Fetching the environment variables
#REGION = os.environ['REGION']
WORKER_FLOW_LOAN = os.environ['WORKER_FLOW_LOAN']
WORKER_FLOW_OTHER =  os.environ['WORKER_FLOW_OTHER']
HUMAN_TASK_ARN = os.environ['HUMAN_TASK_ARN']


BUCKET = ""
TASK_TITLE = "Review"
ROLE = ""
