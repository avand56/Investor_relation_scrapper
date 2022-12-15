from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.s3_operator import S3UploadOperator
from airflow.hooks.http_hook import HttpHook
import requests

default_args = {
    "owner": "airflow",
    "start_date": datetime(2020, 1, 1)
}

dag = DAG("download_and_upload_pdfs", default_args=default_args, schedule_interval="0 0 * * *")

def download_pdf(file_url):
    http = HttpHook()
    response = http.run(file_url)
    return response.content

def upload_to_s3(file_content, s3_bucket, s3_key):
    s3 = S3UploadOperator(
        task_id="upload_pdf_to_s3",
        bucket=s3_bucket,
        key=s3_key,
        file_obj=file_content,
        dag=dag
    )
    s3.execute(None)

download_pdf_task = PythonOperator(
    task_id="download_pdf",
    python_callable=download_pdf,
    op_args=["http://www.example.com/myfile.pdf"],
    dag=dag
)

upload_to_s3_task = PythonOperator(
    task_id="upload_to_s3",
    python_callable=upload_to_s3,
    op_kwargs={"s3_bucket": "my-bucket", "s3_key": "myfile.pdf"},
    dag=dag
)

download_pdf_task >> upload_to_s3_task

