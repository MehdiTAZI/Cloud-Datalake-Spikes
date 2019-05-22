import json
import urllib.parse
import boto3


# S3 client to 
s3 = boto3.client('s3')

# S3 ressource
s3Ressource =  boto3.resource('s3')

# S3 client 
sns = boto3.client('sns')


def lambda_handler(event, context):


    log = logging.getLogger()
    
    # retreive the bucket name
    bucket = event['Records'][0]['s3']['bucket']['name']
    
    # retreive the file key
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    s3Path = 's3://' + bucket + "/" + key
    
    #s3Path  = buffer.getvalue()
    
    backupBucket = bucket
    
    source_object = {
        'Bucket': bucket,
        'Key': key
    }
    
    
    try:
        
        s3Ressource.meta.client.copy(source_object, backupBucket, bucket + "/"  + key)
         
        response = sns.publish(
            TopicArn='arn:aws:sns:eu-west-1:493399554860:newFileOnS3DACBucketTopic',    
            Message=s3Path,   
            Subject='FILE CREATION'
        )
        
        
        
        #log.info('notification send to SNS')
        #log.debug('copied file : ' + s3Path)
        print('copied file : ' + s3Path)
        return s3Path
        
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
