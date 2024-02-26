from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


## 앞서, 03번은 kwargs로 여러 정보를 같이 주입함.
## Jinja templete를 사용하면 ds를 kwargs['ds'] => {{ ds }}로 사용할 수 있음
## Python에서는 kwargs로 접근하시면 빠르게 가능.
## SQL에서는 Query에서 Where 절에 execution_date를 필요로할 수 있음 => Where date='{{ ds }}'


default_args = {
    "owner": "heumsi",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "end_date": datetime(2024, 1, 4)
}


def print_current_date_with_jinja(date):
    execution_date = datetime.strptime(date, "%Y-%m-%d").date()
    date_kor = ["월", "화", "수", "목", "금", "토", "일"]
    datetime_weeknum = execution_date.weekday()
    print(f"{execution_date}는 {date_kor[datetime_weeknum]}요일입니다")

    return execution_date


with DAG(
    dag_id="python_dag_with_jinja",
    default_args=default_args,
    schedule_interval="30 0 * * *",
    tags=['my_dags'],
    catchup=True
) as dag:
    execution_date = "{{ ds }}"

    t1 = PythonOperator(
        task_id="print_current_date_with_jinja",
        python_callable=print_current_date_with_jinja,
        # op_args=[execution_date]
        op_kwargs = {
            "date": execution_date
        }
    )

    t1