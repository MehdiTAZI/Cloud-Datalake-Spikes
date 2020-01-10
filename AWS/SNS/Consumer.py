import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):

    #sns recieved message
    message = event["Records"][0]["Sns"]["Message"]
    
    # serialized data
    data = json.loads(message)
    
    logger.info(data)
   
    
    name = data['name']
    company = data['company']
    dayOfBirth = data['birth']['day']
    
    logger.info(name)
   
    return {
        'statusCode': 200,
        'body': json.dumps('success') 
    }
