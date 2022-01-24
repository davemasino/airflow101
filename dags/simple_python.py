"""
A simple Python DAG.
"""
from __future__ import print_function

import time
from datetime import datetime
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

dag = DAG(
    dag_id='simple_python',
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['airflow101'],
)

def say_hello():
    """Print a hello message"""
    print("Hello, World!")


hello_task = PythonOperator(
    task_id='hello_message',
    python_callable=say_hello,
    dag=dag,
)

def sleep_for_1():
    """Go to sleep"""
    time.sleep(1)


sleeping_task = PythonOperator(
    task_id='go_to_sleep',
    python_callable=sleep_for_1,
    dag=dag,
)

hello_task >> sleeping_task