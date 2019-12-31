1 -  initiate job

aws glacier initiate-job --job-parameters '{"Type": "inventory-retrieval"}' --vault-name YOUR_VAULT --account-id YOUR_ACCOUNT_ID --region YOUR_REGION
Result, should be like :
{
    "location": "/YOUR_ACCOUNT_ID/vaults/YOUR_VAULT/jobs/YOUR_JOB_ID",
    "jobId": "YOUR_JOB_ID"
}

2 - get job informations ( like archives ids )

aws glacier get-job-output --job-id YOUR_JOB_ID --vault-name YOUR_VAULT --region YOUR_REGION --account-id YOUR_ACCOUNT_ID output_file.json

3 - remove all archives one by one using the archive id from step 2
aws glacier delete-archive --archive-id=YOUR_ARCHIVE_ID --vault-name YOUR_VAULT --account-id YOUR_ACCOUNT_ID --region YOUR_REGION

aws glacier delete-vault --vault-name YOUR_VAULT --account-id YOUR_ACCOUNT_ID --region YOUR_REGION
