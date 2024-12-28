from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
from common.common_func import get_sftp

with DAG(
    dag_id="dags_python_import_func",  ###localhost로 접속했을때 보이는 제목들(파이썬 파일명과는 상관없음 그러나 일치시켜주는게 보기 좋음)
    schedule="30 6 * * *", ##(분, 시, 일, 월, 요일)
    start_date=pendulum.datetime(2024, 12, 23, tz="Asia/Seoul"), 
    catchup=False
) as dag:
    
    task_get_sftp = PythonOperator(
        task_id = 'task_get_sftp',
        python_callable = get_sftp
    )