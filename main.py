from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello from Python app running on AWS EKS 🚀"
    }

@app.get("/health")
def health_check():
    return {
        "status": "UP"
    }
