# Amazon-Augmented-AI-A2I
> This repository contains all the code snippets to get Amazon Augmented AI running on AWS platform

## Steps to setup

### A2I Notebook instance
- Upload flow_definition.py file to Amazon Notebook Instance.
- Update the variables in the script.
- Run the script to create a flow definition.
- Copy the generated flow definition ARN which will be used in the Lambda.

### A2I Lambda
- Configure the environment variables in the lambda as required.
- Create a zip of the code inside A2I Lambda folder and upload it to the Lambda which is setup on AWS.
- Update the variables in config.py.





