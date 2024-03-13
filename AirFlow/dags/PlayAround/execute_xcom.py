import time

from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG

from airflow.operators.python import PythonOperator

default_args = {
    'owner' : 'dhruvsh01'
}

def counter_increment(counter):
    print("Counter {counter}!".format(counter = counter))

    return counter + 1

def counter_multiplier(counter):
    print("Counter {counter}!".format(counter = counter))

    return counter*100
    
with DAG(
    dag_id = 'cross_task_communication',
    description = 'Cross communication with XConn',
    default_args = default_args,
    start_date = days_ago(1),
    schedule_interval = '@daily',
    tags = ['xcom', 'python']

) as dag:
    taskA = PythonOperator(
        task_id = 'counter_increment',
        python_callable = counter_increment,
        op_kwargs = {'counter':15}
    )
    taskB = PythonOperator(
        task_id = 'counter_multiplier',
        python_callable = counter_multiplier,
        op_kwargs = {'counter':9}
    )

taskA >> taskB