from airflow import DAG
from airflow.sensors.filesystem import FileSensor
import pendulum
import datetime

with DAG(
    dag_id='dags_file_sensor',
    start_date=pendulum.datetime(2025,1,1, tz = 'Asia/Seoul'),
    schedule='0 7 * * *',
    catchup=False
)as dag:
    tbCycleRentUseDayInfo_sensor = FileSensor(
        task_id = 'tbCycleRentUseDayInfo_sensor',
        fs_conn_id = 'conn_file_opt_airflow_files',
        filepath='tbCycleRentUseDayInfo/{{(data_interval_end.in_timezone("Asia/Seoul") - macros.timedelta(days=1)) | ds_nodash}}/tbCycleRentUseDayInfo.csv',
        recursive= False,
        poke_interval=60,
        timeout = 60*60*24,
        mode = 'reschedule'
    )