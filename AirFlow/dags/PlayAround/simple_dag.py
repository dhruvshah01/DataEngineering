from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG

from airflow.operators.bash import BashOperator

default_args = {
    'owner' : 'dhruvsh01'
}

with DAG(
    dag_id = 'hello_world',
    description = 'First DAG',
    default_args = default_args,
    start_date = days_ago(1),
    schedule_interval = '@daily',
    tags = ['beginner', 'bash', 'hello world']
) as dag:

    task = BashOperator(
        task_id = 'hello_world_task',
        bash_command = 'echo Hello World, let us meet again',
    )

task