from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from airflow.exceptions import AirflowFailException
from utils.slack_notifier import task_fail_slack_alert, task_succ_slack_alert


default_args = {
    "owner": "heumsi",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "end_date": datetime(2024, 1, 4)
}

def _handle_job_error():
    raise AirflowFailException("Job failed")

with DAG(
    dag_id="python_dag_with_slack_webhook",
    default_args=default_args,
    schedule_interval="30 0 * * *",
    tags=['my_dags'],
    catchup=True,
    on_failure_callback=task_fail_slack_alert,
) as dags:
    
    t1 = PythonOperator(
        task_id="raise_exception_and_send_slack_noti",
        python_callable=_handle_job_error
    )
    
    t1