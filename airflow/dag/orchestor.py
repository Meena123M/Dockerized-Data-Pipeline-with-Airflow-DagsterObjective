from airflow import DAG
import sys
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Add your module path
sys.path.append('/opt/airflow/api_request')

def safe_main_callable():
    from insert_data import main
    return main()

default_args = {
    'description': 'Orchestrator DAG for Stock Market Data Ingestion',
    'start_date': datetime(2025, 12, 7),
    'catchup': False,
}

dag = DAG(
    dag_id='stock_data_orchestrator',
    default_args=default_args,
    schedule_interval=timedelta(minutes=5)
)

with dag:
    task1 = PythonOperator(
        task_id='ingest_stock_data_task',
        python_callable=safe_main_callable
    )
