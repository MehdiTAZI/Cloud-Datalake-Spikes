1 - Create a function lambda

2 - Configure role with Read permission on Athena and Read/Write on S3 ( for output )

3 - Configure timeout to 2min ( for the while clause )

4 - create testEvent with some samples

5 - put as a the handler lambda_function.lambda_handler

6 - Create the following HTTP lambda function as described in the function.py

7 - Configure AMAZON API GATEWAY to expose the rest web api

8 - Use Lambda Proxy integration

9 - configure timeout to 29 000
