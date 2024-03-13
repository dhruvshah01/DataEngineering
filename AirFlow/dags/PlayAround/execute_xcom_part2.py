import time

from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG

from airflow.operators.python import PythonOperator

default_args = {
    'owner':'dhruvsh01'
}

def counter_increment(counter):
    print("Counter Value: {counter}".format(counter = counter))

    return counter + 1

def counter_multiplier(ti):
    value = ti.xcom_pull(task_ids = 'counter_increment')
    print("Counter Value: {value}".format(value = value))

    return value*100

def counter_subtractor(ti):
    value = ti.xcom_pull(task_ids = 'counter_multiplier')
    print("Counter value: {value}".format(value = value))

    return value - 8

def print_counter(ti):
    value = ti.xcom_pull(task_ids = 'counter_subtractor')
    print("Counter value: {value}".format(value = value))

with DAG(
    dag_id = 'cross_task_communication_2',
    description = 'Cross-task communication with XCom',
    default_args = default_args,
    start_date = days_ago(1),
    schedule_interval = '@daily',
    tags = ['xcom', 'python']
) as dag:
    taskA = PythonOperator(
        task_id = 'counter_increment',
        python_callable = counter_increment,
        op_kwargs = {'counter':1}

    )
    taskB = PythonOperator(
        task_id = 'counter_multiplier',
        python_callable = counter_multiplier

    )
    taskC = PythonOperator(
        task_id = 'counter_subtractor',
        python_callable = counter_subtractor,

    )
    taskD = PythonOperator(
        task_id = 'print_counter',
        python_callable = print_counter,

    )

taskA >> taskB >> taskC >> taskD

