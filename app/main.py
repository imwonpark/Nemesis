from fastapi import FastAPI

app = FastAPI(
    title="Project Nemesis, Red Teaming Framework",
    description="Framework for AI agent safety and security tests.",
    version="0.1.0",
)

@app.get("/health", tags=["Status"])
def health_check():
    """
    Simple health check to confirm the API is running.
    """
    return {"status": "ok"}
