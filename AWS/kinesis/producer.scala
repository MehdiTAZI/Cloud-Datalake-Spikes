val kinesisClient = AmazonKinesisClientBuilder 
   .standard() 
   .withRegion("AWS_REGION") 
   .build(); 
   
var deliveredObject = new JsonObject(); 

deliveredObject.addProperty("key1", "value1"); 
deliveredObject.addProperty("key2", "value2"); 
  
var putRecordRequest = new PutRecordRequest(); 

putRecordRequest.setStreamName("YOUR_TOPIC"); 
putRecordRequest.setPartitionKey("SUITABLE_PARTITION_KEY"); 
putRecordRequest.withData(ByteBuffer.wrap(deliveredObject.toString().getBytes())); 

var putRecordResult = kinesisClient.putRecord(putRecordRequest); 
