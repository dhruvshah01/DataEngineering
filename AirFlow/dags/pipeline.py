import time
import pandas as pd

from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG

from airflow.operators.python import PythonOperator

default_args = {
    'owner':'dhruvsh01'
}

def read_csv_data():
    df = pd.read_csv("datasets/insurance.csv")
    print(df.head())

    return df.to_json()

def remove_null_values(**kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='read_csv')
    df = pd.read_json(data)
    df = df.dropna()

    print(df.head())
    return df.to_json()

def groupby_smoker(ti):
    json_data = ti.xcom_pull(task_ids='drop_null')
    df = pd.read_json(json_data)

    smoker_df = df.groupby('smoker').agg({
        'age': 'mean', 
        'bmi': 'mean',
        'charges': 'mean'
    }).reset_index()

    smoker_df.to_csv(
        'output/grouped_by_smoker.csv', index=False)


def groupby_region(ti):
    json_data = ti.xcom_pull(task_ids='drop_null')
    df = pd.read_json(json_data)

    region_df = df.groupby('region').agg({
        'age': 'mean', 
        'bmi': 'mean', 
        'charges': 'mean'
    }).reset_index()
    

    region_df.to_csv(
        'output/grouped_by_region.csv', index=False)


with DAG(
    dag_id = 'read_csv',
    description = 'Execute pipeline to read csv',
    default_args = default_args,
    start_date = days_ago(1),
    schedule_interval = '@daily',
    tags = ['xcom', 'python']
) as dag:
    read_csv = PythonOperator(
        task_id = 'read_csv',
        python_callable = read_csv_data
    )
    drop_null = PythonOperator(
        task_id = 'drop_null',
        python_callable = remove_null_values
    )

    groupbysmoker = PythonOperator(
        task_id='groupby_smoker',
        python_callable=groupby_smoker
    )
    
    groupbyregion = PythonOperator(
        task_id='groupby_region',
        python_callable=groupby_region
    )

read_csv >> drop_null >> [groupbyregion, groupbysmoker]