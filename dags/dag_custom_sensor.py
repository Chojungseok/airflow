from sensors.seoul_api_date_sensor import SeoulAPIDateSensor
from airflow import DAG
import pendulum
import datetime

with DAG(
    dag_id='dag_custom_sensor',
    start_date=pendulum.datetime(2025,1,1,tz='Asia/Seoul'),
    schedule=None,
    catchup=False
) as dag:
    tb_Cycle_Rent_UseDay_Info = SeoulAPIDateSensor(
        task_id = 'tb_Cycle_Rent_UseDay_Info',
        dataset_nm='tbCycleRentUseDayInfo',
        base_dt_col='RENT_DT',
        day_off=0,
        poke_interval = 600,
        mode = 'reschedule'
    )

