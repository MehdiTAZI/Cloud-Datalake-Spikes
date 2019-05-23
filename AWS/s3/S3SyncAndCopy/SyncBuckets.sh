# !/bin/bash

# TODO: IF CROSS REGION, aws s3 mb DST_BUCKET --region us-east-1
SRC_BUCKET=$1
DST_BUCKET=$2
PROFILE=$3

aws configure set $PROFILE.s3.max_concurrent_requests 500
aws configure set $PROFILE.s3.max_queue_size 10000
aws configure set $PROFILE.s3.multipart_threshold 64MB
aws configure set $PROFILE.s3.multipart_chunksize 16MB
# aws configure set $PROFILE.s3.max_bandwidth 50MB/s
aws configure set $PROFILE.s3.use_accelerate_endpoint true
#aws configure set $PROFILE.s3.addressing_style path


# TODO: IF CROSS REGION, create temporary bucket in the same region as source  SRC -> TMP -> DST_BUCKET
aws s3 sync s3://$SRC_BUCKET s3://$DST_BUCKET --profile $PROFILE
