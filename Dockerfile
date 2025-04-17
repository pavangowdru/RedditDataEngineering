FROM apache/airflow:2.7.1-python3.11

# Copy the requirements file into the container
COPY requirements.txt /opt/airflow/

USER root
RUN apt-get update && apt-get install -y gcc python3-dev

USER airflow

# Install the required packages
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
