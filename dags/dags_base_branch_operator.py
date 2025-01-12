from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator, BranchPythonOperator


with DAG(
    dag_id="dags_base_branch_operator",
    start_date=pendulum.datetime(2024, 12, 25, tz = "Asia/Seoul"),
    schedule = None,
    catchup=False
)as dag:
    class CustomBranchOperaotr(BranchPythonOperator):
        def choose_branch(self, context):
            import random
    
    @task.branch(task_id = 'python_branch_task')
    def select_random(self, context):
        import random
        print(context)
        item_list = ["A", "B", "C"]
        selected_item = random.choice(item_list)
        if selected_item == "A":
            return 'task_a'
        elif selected_item in ["B", "C"]:
            return['task_b', 'task_c']

    custom_branch_operaotr = CustomBranchOperaotr(task_id = 'python_branch_task')

    def common_func(**kwargs):
        print(kwargs['selected'])

    task_a = PythonOperator(
        task_id = 'task_a',
        python_callable = common_func,
        op_kwargs = {'selected' : 'A'}
    )
    task_b = PythonOperator(
        task_id = 'task_b',
        python_callable = common_func,
        op_kwargs = {'selected' : 'B'}
    )

    task_c = PythonOperator(
        task_id = 'task_c',
        python_callable = common_func,
        op_kwargs = {'selected' : 'C'}
    )

    custom_branch_operaotr >> [task_a, task_b, task_c]
    
