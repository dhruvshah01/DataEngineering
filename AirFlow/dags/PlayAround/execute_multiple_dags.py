from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG

from airflow.operators.bash import BashOperator

default_args = {
    'owner' : 'dhruvsh01'
}

with DAG(
    dag_id = 'executing_multiple_dags',
    description = 'Multiple DAGs',
    default_args = default_args,
    start_date = days_ago(1),
    schedule_interval = '@once'
) as dag:

    taskA = BashOperator(
        task_id = 'taskA',
        bash_command = ''' 
                        echo Task A has started
                        for i in {1..5}
                        do
                            echo Task A printing $i
                        done
                        echo Task A completed            
        '''
    )

    taskB = BashOperator(
        task_id = 'taskB',
        bash_command = '''
        echo Task B has started
        sleep 5
        echo Task B has completed
        '''
    )

    taskC = BashOperator(
        task_id = 'taskC',
        bash_command = '''
        echo Task C has started
        sleep 2
        echo Task C has completed
        '''
    )

    taskD = BashOperator(
        task_id = 'taskD',
        bash_command = '''
        echo Task D has completed
        '''
    )

taskA >> taskB
taskA >> taskC

taskD << taskB
taskD << taskC