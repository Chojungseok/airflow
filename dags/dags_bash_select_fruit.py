from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_select_fruit", 
    schedule="10 0 * * 6#1", 
    start_date=pendulum.datetime(2024, 12, 25, tz="Asia/Seoul"), 
    catchup=False
) as dag:
    
    t1_orange = BashOperator(
        task_id = "ti_orange",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh ORANGE",
    )

    t2_avocado = BashOperator(
        task_id = "ti_avocado",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh AVOCADO",
    )

    t1_orange >> t2_avocado