from airflow import DAG
import pendulum


with DAG(
    dag_id="dags_python_task_operator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2024, 12, 24, tz="Aisa/Seoul"),
    catchup=False,
):