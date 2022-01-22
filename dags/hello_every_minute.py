"""
### Tutorial Documentation
Documentation that goes along with the Airflow tutorial located
[here](https://airflow.apache.org/tutorial.html)
"""

from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    'hello_every_minute',
    default_args={
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    description='A simple tutorial DAG that says hello every minute',
    schedule_interval=timedelta(minutes=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['airflow101'],
) as dag:

    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='say_hello',
        depends_on_past=False,
        bash_command='echo Hello!',
        retries=3,
    )

    t1.doc_md = dedent(
        """\
    #### Task Documentation
    This task prints the date
    """
    )

    t2.doc_md = dedent(
        """\
    #### Task Documentation
    This task says hello
    """
    )

    dag.doc_md = __doc__

    t1 >> t2
