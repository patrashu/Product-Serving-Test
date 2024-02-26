# Batch Serving with AirFlow

## Run with Poetry in WSL2

```pwsh
pip install poetry
poetry config virtualenvs.in-project true --local
poetry run python --version  ## check version
poetry install

AIRFLOW_VERSION=2.6.3
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

poetry run pip3 install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

### Airflow DB init

```pwsh
export AIRFLOW_HOME=`pwd`
echo $AIRFLOW_HOME

poetry run airflow db init
```

### Create Airflow Admin 

```pwsh
poetry run airflow users create \
--username admin \
--password 'pswd to string' \
--firstname gildong \
--lastname hong \
--role Admin \
--email honggildong@gmail.com 
```

### Run Airflow WebServer

```pwsh
poetry run airflow webserver --port 8080
```

### Run Airflow Scheduler

```pwsh
poetry run airflow scheduler
```

## Run with Docker compose
```pwsh
docker compose up -d
```