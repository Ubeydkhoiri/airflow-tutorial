from datetime import datetime, timedelta

from airflow import DAG 

from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

default_args = {
    'owner':'ubeyd',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_minio_s3_v1',
    start_date=datetime(2024,9,1),
    schedule_interval='@daily',
    default_args=default_args
) as dag:
    task1 = S3KeySensor(
        task_id='sensor_minio_s3',
        bucket_name='airflow',
        bucket_key='data.csv',
        aws_conn_id='minio_conn'
    )
