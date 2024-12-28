from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
import random

with DAG(
    dag_id="dags_python_operator",  ###localhost로 접속했을때 보이는 제목들(파이썬 파일명과는 상관없음 그러나 일치시켜주는게 보기 좋음)
    schedule="30 6 * * *", ##(분, 시, 일, 월, 요일)
    start_date=pendulum.datetime(2024, 12, 23, tz="Asia/Seoul"), 
    catchup=False,
    tags=["example", "example2"], ### 처음 들어갔을때 제목(dag_id) 밑에 보이는 파란 글씨들
) as dag:
    def select_fruit():
        fruit = ['APPLE', 'BANANA','ORANGE','AVOCADO']
        rand_int = random.randint(0,3)
        print(fruit[rand_int])
    
    py_t1 = PythonOperator(
        task_id = 'py_t1',
        python_callable=select_fruit
    )

    py_t1