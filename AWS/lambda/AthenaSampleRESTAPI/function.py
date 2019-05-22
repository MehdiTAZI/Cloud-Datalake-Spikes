import boto3
import time

def lambda_handler(event, context):
    
    #whereclause = event[where]
    #Const 
    RUNNING_CONST = "RUNNING"
    
    # AWS services variables
    bucket = "mehdiengie"
    athena_output_prefix = "athena_output/"
    
    table = "jsontable"
    database = "mehdi"
    
    query_sample = "SELECT * FROM "+ table + " limit 10;"
    s3_athena_output = "s3://" + bucket + "/" + athena_output_prefix

    # AWS clients

    athena = boto3.client('athena')
    s3_ressource = boto3.resource('s3')
    
    athenaResult = athena.start_query_execution(QueryString = query_sample,
                                        QueryExecutionContext={
                                            'Database': database
                                        },
                                        ResultConfiguration={
                                            'OutputLocation': s3_athena_output
                                        }
                                        )
    
    query_execution_id = athenaResult['QueryExecutionId']
          
    query_execution_state = RUNNING_CONST
    
    while RUNNING_CONST == query_execution_state:
        time.sleep(50)
        query_execution = athena.get_query_execution(QueryExecutionId=query_execution_id)
        query_execution_state = query_execution['QueryExecution']['Status']['State']
        if query_execution_state == "FAILED":
            raise Exception(query_execution)                   
                                        
    s3KeyResult = query_execution_id + ".csv" 
    
    csv_result_path = athena_output_prefix + s3KeyResult
    
    obj = s3_ressource.Object(bucket,csv_result_path )
    body = obj.get()['Body'].read().decode('utf-8') 
    
    return body
