from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.utils.dates import days_ago
import random

def select_random(**kwargs):
    item_list = ["A", "B", "C"]
    selected_item = random.choice(item_list)
    if selected_item == "A":
        return 'task_a'
    else:
        return ['task_b', 'task_c']

def common_func(selected):
    print(f"Task {selected} is running")

with DAG(
    dag_id="dags_base_branch_operator",
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False
) as dag:
    
    branch_task = BranchPythonOperator(
        task_id='python_branch_task',
        python_callable=select_random
    )

    task_a = PythonOperator(
        task_id='task_a',
        python_callable=common_func,
        op_kwargs={'selected': 'A'}
    )

    task_b = PythonOperator(
        task_id='task_b',
        python_callable=common_func,
        op_kwargs={'selected': 'B'}
    )

    task_c = PythonOperator(
        task_id='task_c',
        python_callable=common_func,
        op_kwargs={'selected': 'C'}
    )

    branch_task >> [task_a, task_b, task_c]


