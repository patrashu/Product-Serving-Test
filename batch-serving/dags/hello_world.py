from datetime import timedelta

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def print_hello():
    return 'Hello world!'


with DAG(
    dag_id="Hello_world",
    description="Hello world example",
    start_date=days_ago(2),
    schedule_interval="0 6 * * *", #UTC+9
    tags=['my_dags']
) as dags:
    
    t1 = BashOperator(
        task_id="print_hello",
        bash_command="echo hello",
        owner='heumsi',
    )
    
    t2 = PythonOperator(
        task_id="print_world",
        python_callable=print_hello,
        owner='heumsi',
    )
    
    t1 >> t2
