from airflow.sensors.bash import BashSensor
from airflow.operators.bash import BashOperator
from airflow import DAG
import pendulum
import datetime

with DAG(
    dag_id = 'dags_bash_sensor',
    start_date=pendulum.datetime(2025,1,1,tz='Asia/Seoul'),
    schedule='0 6 * * *',
    catchup=False
)as dag:
    
    sensor_task_by_poke = BashSensor(
        task_id = 'sensor_task_by_poke',
        env={'FILE':'/opt/airflow/files/tbCycleRentUseDayInfo/{{(data_interval_end.in_timezone("Asia/Seoul") - macros.timedelta(days=1)) | ds_nodash}}/tbCycleRentUseDayInfo.csv'},
        bash_command=f'''echo $FILE &&
                        if [ -f $FILE ]; then
                                exit 0
                        else
                                exit 1
                        fi''',
        poke_interval = 30,
        timeout = 60*2,
        mode = 'poke',
        soft_fail=False
    )

    sensor_task_by_reschedule = BashSensor(
        task_id = 'sensor_task_by_reschedule',
        env={'FILE':'/opt/airflow/files/tbCycleRentUseDayInfo/{{(data_interval_end.in_timezone("Asia/Seoul") - macros.timedelta(days=1)) | ds_nodash}}/tbCycleRentUseDayInfo.csv'},
        bash_command=f'''echo $FILE &&
                        if [ -f $FILE ]; then
                                exit 0
                        else
                                exit 1
                        fi''',
        poke_interval = 30,
        timeout = 60*9,
        mode = 'reschedule',
        soft_fail=True
    )

    bash_task = BashOperator(
        task_id = 'bash_task',
        env={'FILE':'/opt/airflow/files/tbCycleRentUseDayInfo/{{(data_interval_end.in_timezone("Asia/Seoul") - macros.timedelta(days=1)) | ds_nodash}}/tbCycleRentUseDayInfo.csv'},
        bash_command='echo "건수: `cat $FILE | wc -l`"',
    )


    [sensor_task_by_poke, sensor_task_by_reschedule] >> bash_task