1 - Create a function lambda
2 - Configure role with Read permission on Athena and Read/Write on S3 ( for output )
3 - Configure timeout to 2min
4 - create testEvent with some samples
5 - put as a the handler lambda_function.lambda_handler
6 - Create the following HTTP lambda function as described in the function.py
