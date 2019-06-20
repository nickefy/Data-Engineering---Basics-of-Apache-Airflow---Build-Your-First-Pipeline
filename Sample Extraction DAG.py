# airflow related
from airflow import models
from airflow import DAG
# other packages
from datetime import datetime, timedelta
# import operators from the 'operators' file
from operators import DataSourceToCsv

default_dag_args = {
    # Setting start date as yesterday starts the DAG immediately       when it is
    # detected in the Cloud Storage bucket.
    # set your start_date : airflow will run previous dags if dags #since startdate has not run
    # notify email is a python function that sends notification email upon failure
    'start_date': datetime(2019, 5, 1, 7),
    'email_on_failure': True,
    'email_on_retry': True,
    'project_id' : 'your_project_name',
    'retries': 1,
    'on_failure_callback': notify_email,
    'retry_delay': timedelta(minutes=5),
}
with models.DAG(
    dag_id='your_dag_name',
    # Continue to run DAG once per day
    schedule_interval = timedelta(days=1),
    catchup = True,
    default_args=default_dag_args) as dag:

task1 = 
# code for task2

task2 = DataSourceToCsv.DataSourceToCsv(
    task_id='task name',
    bigquery_table_name = 'tablename',
    extract_query = """ Select * from tablename """,
    connection = 'my defined postgres db connection')

task3 = 
# code for task 3

task3 =
# code for task3

# set dependencies and sequence
task1
task2
task3.set_upstream([task2])
task3 >> task 4