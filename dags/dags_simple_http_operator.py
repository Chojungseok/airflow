from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
import pendulum
import datetime
from airflow.decorators import task

with DAG(
    dag_id="dags_simple_http_operator",
    start_date=pendulum.datetime(2025, 1, 1, tz = "Asia/Seoul"),
    schedule = None,
    catchup=False
)as dag:
    '''서울시 공공 자전거 대여 정보'''

    tb_Cycle_Rent_Use_Day_Info = SimpleHttpOperator(
        task_id = 'tb_Cycle_Rent_Use_Day_Info',
        http_conn_id = 'openapi.seoul.go.kr',
        endpoint = '{{var.value.apikey_openapi_seoul_go_kr}}/json/tbCycleRentUseDayInfo/1/10/20250101',
        method = 'GET',
        headers = {'Content-Type': 'application/json',
                   'charset' : 'utf-8',
                   'Accept' : '*/*'}
    )

    @task(task_id = 'python_2')
    def python_2(**kwargs):
        ti = kwargs['ti']
        rslt = ti.xcom_pull(task_ids = 'tb_Cycle_Rent_Use_Day_Info')
        import json
        from pprint import pprint

        pprint(json.loads(rslt))



    tb_Cycle_Rent_Use_Day_Info >> python_2()