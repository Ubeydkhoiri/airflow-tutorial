from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'ubeyd',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}
with DAG(
    dag_id="my_first_dag_v5",
    default_args=default_args,
    description='This is my first dag that I write',
    start_date=datetime(2024,9,1,2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the first task"
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo hey, I am task2 and will be running after task1"
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo hey, I am task3 and will be running after task1 at the same time as task2"
    )

    # Task dependencies method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Task dependencies method 2
    # task1 >> task2
    # task1 >> task3

    # Task dependencies method 1
    task1 >> [task2, task3]