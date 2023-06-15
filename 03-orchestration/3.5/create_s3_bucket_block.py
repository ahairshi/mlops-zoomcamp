from time import sleep
from prefect_aws import S3Bucket, AwsCredentials


def create_aws_creds_block():
    my_aws_creds_obj = AwsCredentials(
        aws_access_key_id="AKIA57GCNNGU32MJ7WQU", aws_secret_access_key="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"
    )
    my_aws_creds_obj.save(name="my-aws-creds", overwrite=True)


def create_s3_bucket_block():
    aws_creds = AwsCredentials.load("my-aws-creds")
    my_s3_bucket_obj = S3Bucket(
        bucket_name="my-first-bucket-abc", credentials=aws_creds
    )
    my_s3_bucket_obj.save(name="zoomcamp-mlops-2023-taxi", overwrite=True)


if __name__ == "__main__":
    create_aws_creds_block()
    sleep(5)
    create_s3_bucket_block()
