from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {
    'owner' : 'dhruvsh01'
}

def print_function():
    print("Hello World")

with DAG (
    dag_id = 'execute_python_operator',
    description = 'DAG python operator',
    default_args = default_args,
    start_date = days_ago(1),
    schedule_interval = '@daily',
    tags = ['simple', 'python'],
) as dag:
    task = PythonOperator(
        task_id = 'python_task',
        python_callable = print_function
    )

task 