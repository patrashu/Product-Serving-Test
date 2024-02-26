from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

## 앞선 파일에서 datetime.now().date()를 사용하면 언제 실행하든 현재 실행하는 시점의 시간이 반영됨
## Airflow Batch 특성상, 실행 시점이 아닌 DAG 실행 시점을 기준으로 하고 싶을 때가 있음
## 예를 들어, 과거 데이터 마이그레이션의 경우 
## 이러한 상황에 execution_date / logical_date를 주입하여 사용할 수 있음
## 역동성 : 연산을 여러번 적용하더라도 결과가 달라지지 않는 성질
## 핵심은 kwargs의 값에서 추출하여 ds를 사용하면 됨.

default_args = {
    "owner": "heumsi",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
}


def print_current_date_with_context(*args, **kwargs):
    execution_date = kwargs["ds"]
    execution_date_nodash = kwargs["ds_nodash"]
    print(f"execution_date: {execution_date}")
    print(f"execution_date_nodash: {execution_date_nodash}")
    execution_date = datetime.strptime(execution_date, "%Y-%m-%d").date()
    
    date_kor = ["월", "화", "수", "목", "금", "토", "일"]
    datetime_weeknums = execution_date.weekday()
    print(f"{execution_date}는 {date_kor[datetime_weeknums]}요일입니다.")

with DAG(
    dag_id="python_dag_with_context",
    default_args=default_args,
    schedule_interval="30 0 * * *",
    tags=["my_dags"],
    catchup=True,
) as dag:
    
    t1 = PythonOperator(
        task_id="print_current_date_with_context",
        python_callable=print_current_date_with_context,
    )
    
    t1