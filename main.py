from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello from Python app running on AWS EKS throgh Terraform!.."
    }

@app.get("/health")
def health_check():
    return {
        "status": "UP"
    }
