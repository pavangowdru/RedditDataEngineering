from datetime import datetime
from airflow import DAG
import os
import sys
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__) )) )

from pipelines import reddit_pipeline

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 16),
    'retries': 1,
}

file_postfix = datetime.now().strftime("%Y%m%d_%H%M%S")

dag = DAG(
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
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'daily',
        'limit': 100
    }
)

#upload the reddit data to s3


