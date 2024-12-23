from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",  ###localhost로 접속했을때 보이는 제목들(파이썬 파일명과는 상관없음 그러나 일치시켜주는게 보기 좋음)
    schedule="0 0 * * *", ##(분, 시, 일, 월, 요일)
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"), 
    catchup=False,
    tags=["example", "example2"], ### 처음 들어갔을때 제목(dag_id) 밑에 보이는 파란 글씨들
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2