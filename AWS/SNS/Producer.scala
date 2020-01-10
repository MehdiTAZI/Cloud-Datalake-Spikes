
    /*
    // OPTIONAL - if called from outside AWS
    val aws_credentials =new BasicSessionCredentials("", "", "")
    val snsClient = AmazonSNSClientBuilder.standard().withRegion("REGION")
    .withCredentials(new AWSStaticCredentialsProvider(aws_credentials)).build();
    */
    
    // OPTIONAL - if called inside AWS  ( no authentification required ) 
    
    val snsClient = AmazonSNSClientBuilder.standard().withRegion("REGION").build();
    
    var myDataToSend = new JsonObject();
    myDataToSend.addProperty("key1", "value1");
    myDataToSend.addProperty("key2", "value2");
    
    var publishRequest = new PublishRequest()
      .withTopicArn("arn:aws:sns:REGION:ACCOUNT:TOPIC_NAME")
      .withMessage(myDataToSend.toString());
      
    snsClient.publish(publishRequest)
