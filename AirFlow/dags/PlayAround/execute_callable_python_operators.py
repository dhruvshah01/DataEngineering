from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
import time
from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {
    'owner' : 'dhruvsh01'
}

def greet_name(name):
    print("Hello, {name}!".format(name = name))

def greet_with_city(name, city):
    print("Hello, {name} from {city}!".format(name = name, city = city))

with DAG(
    dag_id = 'execute_multiple_callable_operators',
    description = 'Python callable operators',
    default_args = default_args,
    start_date = days_ago(1),
    schedule_interval = '@daily',
    tags = ['dependencies', 'python']
) as dag:
    taskA = PythonOperator(
        task_id = 'greet_hello',
        python_callable = greet_name,
        op_kwargs = {'name' : 'Dhruv'}
    )
    taskB = PythonOperator(
        task_id = "greet_hello_with_name",
        python_callable = greet_with_city,
        op_kwargs = {'name':'Dhruv', 'city':'Boston'}
    )

taskA >> taskB