"""
A simple Python DAG using the Taskflow API.
"""
import logging
import time
from datetime import datetime

from airflow import DAG
from airflow.decorators import task

log = logging.getLogger(__name__)

with DAG(
    dag_id='simple_python_taskflow_api',
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['airflow101'],
) as dag:
    @task(task_id="hello_message")
    def say_hello():
        """Print a hello message"""
        print("Hello, World!")

    hello_task = say_hello()

    @task(task_id="go_to_sleep")
    def sleep_for_1():
        """Go to sleep"""
        time.sleep(1)

    sleeping_task = sleep_for_1()

    hello_task >> sleeping_task
