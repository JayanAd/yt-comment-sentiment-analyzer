import mlflow

mlflow.set_tracking_uri("http://ec2-54-167-167-8.compute-1.amazonaws.com:5000")

try:
    mlflow.set_experiment("test-connection")
    with mlflow.start_run() as run:
        mlflow.log_metric("test_metric", 1.0)
        print(f"Connection successful! Run ID: {run.info.run_id}")
except Exception as e:
    print(f"Connection failed: {e}")