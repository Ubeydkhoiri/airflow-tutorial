from datetime import datetime, timedelta

from airflow import DAG 
from airflow.operators.bash import BashOperator


default_args = {
    'owner':'ubeyd',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id="dag_with_cron_expression_v3",
    start_date=datetime(2024,8,25),
    schedule_interval='0 3 * * Tue-Fri'
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo dag with cron expression!"
    )