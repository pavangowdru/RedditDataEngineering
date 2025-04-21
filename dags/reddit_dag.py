from datetime import datetime
from airflow import DAG
import os
import sys
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__) )) )

from pipelines.reddit_pipeline import reddit_pipeline
from pipelines.aws_s3_pipeline import upload_s3_pipeline

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 16),
    'retries': 1,
}

file_postfix = datetime.now().strftime("%Y%m%d_%H%M%S")

dag_1 = DAG(
    dag_id ='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'pipeline', 'etl'],
    description='A simple DAG to extract, transform, and load Reddit data',
)

# Extract from reddit
extract_reddit_data = PythonOperator(
    task_id='extract_reddit_data',
    python_callable=reddit_pipeline,
    op_kwargs={
        'filename': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag_1
)

#upload the reddit data to s3
upload_s3 = PythonOperator( 
    task_id = 'upload_to_s3',
    python_callable = upload_s3_pipeline,
    dag = dag_1
)

extract_reddit_data >> upload_s3


