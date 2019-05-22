Notify an SNS TOPIC ( SMS + EMAIL ) and backup the file according to a prefix 


1 - Create SNS TOPIC

2 - Create 2 SNS SUBSCRIPTIONS ( MAIL & SMS )

3 - Validate the email and phone to receive notifications

4- create a role with write and read access policies on S3 and with publish on SNS policies

5 - Create lambda function on S3 creation event with a prefix pointing on sensitive data

6 - Check that on that the trigger on S3 is activated

7 - Copy / Past the lambda function

8 - You can test using the TestEvent Lambda functionality
