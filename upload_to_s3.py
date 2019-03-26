import boto3

s3 = boto3.resource('s3',
        aws_access_key_id='AKIAIGG6M3MA6KLV5RSA',
        aws_secret_access_key='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'
        )

# Create an S3 client
s3 = boto3.client('s3')

filename = '1.csv.gz'
bucket_name = 'mm-challenge'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(filename, bucket_name, filename)