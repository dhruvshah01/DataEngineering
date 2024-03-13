from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
import time
from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'dhruvsh01'
}

def task_A():
    print("Hello, TaskA")
    time.sleep(5)
    print("TaskA executed")

def task_B():
    print("TaskB executed")

def task_C():
    print("Hello, TaskC")
    time.sleep(5)
    print("TaskC executed")

def task_D():
    print("TaskD executed")

with DAG(
    dag_id = 'executing_multiple_python_operators',
    description = 'Multiple DAGs',
    default_args = default_args,
    start_date = days_ago(1),
    schedule_interval = '@daily',
    tags = ['dependencies', 'python']
) as dag: 
    taskA =  PythonOperator(
        task_id = 'taskA_python_script',
        python_callable = task_A
    )
    taskB = PythonOperator(
        task_id = 'taskB_python_script',
        python_callable = task_B
    )
    taskC =  PythonOperator(
        task_id = 'taskC_python_script',
        python_callable = task_C
    )
    taskD = PythonOperator(
        task_id = 'taskD_python_script',
        python_callable = task_D
    )

    taskA >> [taskB, taskC]
    [taskB, taskC] >> taskD



