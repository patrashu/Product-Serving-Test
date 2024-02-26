from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


default_args = {
    "owner": "heumsi",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "end_date": datetime(2024, 1, 4),
}


def print_current_date():
    date_kor = ["월", "화", "수", "목", "금", "토", "일"]
    date_now = datetime.now().date()  ## 현재 날짜로 반영됨 (2024-01-01이 아니라 실행 시점으로)
    datetime_weeknums = date_now.weekday()
    print(f"{date_now}는 {date_kor[datetime_weeknums]}요일입니다.")
    
    
with DAG(
    dag_id="python_dag1",
    default_args=default_args,
    schedule_interval="30 0 * * *",
    tags=["my_dags"],
    catchup=True,
) as dag:
    
    t1 = PythonOperator(
        task_id="print_current_date",
        python_callable=print_current_date,
    )
    
    t1