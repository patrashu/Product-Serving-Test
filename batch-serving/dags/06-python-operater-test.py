from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


default_args = {
    "owner": "heumsi",
    "depends_on_past": False,  # 과거 Task 성공 여부에 따라 실행, False => 그냥 실행
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    dag_id="06-bash-operator",
    description="Bash Operator Example",
    default_args=default_args,
    schedule_interval="@once",
    tags=["my_dags"],
) as dags:
    
    t1 = BashOperator(
        task_id="print_date", # task_id
        bash_command="date", # 실행할 bash command
    )
    
    t2 = BashOperator(
        task_id="sleep",
        bash_command="sleep 5",
        retries=2, # 재시도 횟수
    )
    
    t3 = BashOperator(
        task_id="pwd",
        bash_command="pwd",
    )
    
    t1 >> t2 # t1이 끝나면 t2 실행
    t2 >> t3 # t1이 끝나면 t3 실행