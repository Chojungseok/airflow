from operators.seoul_api_to_csv_operator import SeoulApiToCsvOperator
from airflow import DAG
import pendulum


with DAG(
    dag_id="dags_seoul_api_sharebike",
    schedule = '0 7 * * *',
    start_date=pendulum.datetime(2025, 1, 1, tz = "Asia/Seoul"),
    catchup=False
)as dag:
    '''서울시 공공자전거 대여 정보'''
    tb_souel_sharebike_info=SeoulApiToCsvOperator(
        task_id = 'tb_souel_sharebike_info',
        dataset_nm='tbCycleRentUseDayInfo',
        path='airflow/files/tbCycleRentUseDayInfo/{{data_interval_end.in_timezone("Asia/Seoul") | ds_nodash}}',
        file_name='tbCycleRentUseDayInfo.csv',
        base_dt = '{{ (data_interval_end | timedelta(days=-1)).in_timezone("Asia/Seoul") | ds_nodash }}'

    )


    # '''서울시 공공자전거 대여소 현황'''
    # Seoul_share_bike_starion_List=SeoulApiToCsvOperator(
    #     task_id = 'Seoul_share_bike_starion_List',
    #     dataset_nm='bikeList',
    #     path='airflow/files/bikeList/{{data_interval_end.in_timezone("Asia/Seoul") | ds_nodash}}',
    #     file_name='bikeList.csv'
    # )


    tb_souel_sharebike_info 