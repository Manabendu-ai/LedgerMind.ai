from fastapi import FastAPI

app = FastAPI(
    title="LedgerMind.ai",
    version="1.0.0",
    summary="""
    Enterprise AI platform that transform invoices, receipts, tax documents, 
    and financial records into structured intelligence.
    """
)

@app.get("/")
def home():
    return {
        "API" : {
            "application" : "LedgerMind.ai",
            "version" : "1.0.0"
        }
    }