from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'ubeyd',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG (
    dag_id='dag_with_cathcup_backfill_v2',
    default_args=default_args,
    start_date=datetime(2024,8,30),
    schedule_interval='@daily',
    catchup=False 
    # for catchup backfill >> dokcer exec -it container_id bash >> 
    # airflow dags backfill -s 2024-08-29 -e 2024-08-31 dag_with_cathcup_backfill_v2
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo This is a simple bash command!'
    )