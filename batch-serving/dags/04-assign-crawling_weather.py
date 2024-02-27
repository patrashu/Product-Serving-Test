import os
import requests
import pandas as pd

from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator


OUTPUT_DIR = os.path.join(os.curdir, "data")
DOC_PATH = os.path.join(OUTPUT_DIR, "forecasts.csv")

FCST_URL = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst"
SERVICE_KEY = "your_secret" # TODO: use your secret key


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 2, 7),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


# TODO 1. get_forecast 함수를 완성합니다
def get_forecast(page_num, lat, lng) -> pd.DataFrame:
    # TODO:
    #  requests, FCST_URL, SERVICE_KEY 를 활용하여 서울의 초단기 날씨 예보를 수집합니다
    #  lat, lng 는 좌표 정보이며, Pandas DataFrame 형태로 결과를 반환합니다
    return df


# TODO 2. processing 함수를 완성합니다
def processing(**kwargs) -> pd.DataFrame:
    # TODO:
    #  get_forecast 함수를 통해 수집한 예보를 가져옵니다.
    #  같은 지역에 대한 다른 시간대의 예보 데이터가 쌓일 경우, 가장 최근의 데이터를 제외하고 중복 제거합니다.
    #  예보 데이터는 수집 시점을 기준으로 2~4시간 사이의 예보를 반환합니다.
    #  중복된 데이터가 있을 시 제거해야 합니다.
    return latest_forecast_df


# TODO 3. save_file 함수를 완성합니다
def save_file(**kwargs):
    # TODO: get_forecast_task 를 통해 다운 받은 예보 결과를 가져온 뒤 csv 파일 형태로 저장합니다.
    #   마찬가지로 중복된 행을 제거해야 합니다.


# TODO 4. 한 시간에 한번씩 서울 지역의 날씨 데이터를 수집하는 DAG를 완성합니다. 주어진 두 함수를 활용합니다.
with DAG(
        dag_id='04-crawling_weather',
        default_args=default_args,
        schedule_interval="* 12 * * *",  # hourly
        catchup=True,
        tags=['assignment'],
) as dag:
    execution_date = "{{ ds_nodash }}"

    # TODO: get_forecast 함수를 활용해 forecast_task 를 완성합니다.
    get_forecast_task = PythonOperator(
        task_id="get_forecast_task",
        python_callable=get_forecast,
        op_kwargs={
        }
    )

    processing_task = PythonOperator(
        task_id="processing_task",
        python_callable=processing,
    )

    save_task = PythonOperator(
        task_id="save_forecast_task",
        python_callable=save_file,
    )

    get_forecast_task >> processing_task >> save_task
