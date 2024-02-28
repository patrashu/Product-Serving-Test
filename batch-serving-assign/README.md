## Run airflow with Docker in WSL2

### Prerequisites
- Install Docker
- WSL2 Docker Setting

### Run / Exit
```bash
export AIRFLOW_HOME=`pwd`
echo $AIRFLOW_HOME

docker-compose up -d  # Run
docker-compose down  # Exit
```

### 