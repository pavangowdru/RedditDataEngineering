import s3fs
from utils.constants import AWS_ACCESS_KEY, AWS_SECRET_KEY
import os

def connect_to_s3() :
    try:
        s3 = s3fs.S3FileSystem(anon=False,
                                key=AWS_ACCESS_KEY,
                                secret=AWS_SECRET_KEY)
        
        return s3
    except Exception as e:
        print(e)

def create_bucket_if_not_exists(s3 : s3fs.S3FileSystem, bucket: str):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            print(f"Bucket {bucket} created successfully.")
        else:
            print(f"Bucket {bucket} already exists.")
    except Exception as e:
         print(e)

def upload_to_s3(s3 : s3fs.S3FileSystem, file_path:str, bucket: str, filename: str):
    try:
        if not os.path.exists(file_path):
            print(f"[ERROR] File does not exist: {file_path}")
            return

        s3_path = f"{bucket}/raw/{filename}"
        print(f"Uploading {file_path} to s3://{s3_path}")
        s3.put(file_path, s3_path)

        if s3.exists(s3_path):
            print(f"[SUCCESS] File uploaded: s3://{s3_path}")
        else:
            print(f"[FAILURE] Upload reported success but file not found in bucket.")
    except Exception as e:
        print(f"[ERROR] Exception during upload: {e}")
