from fastapi import FastAPI
from .router.excel_router import router as exr

app = FastAPI(
    title="LedgerMind.ai",
    version="1.0.0",
    summary="""
    Enterprise AI platform that transform invoices, receipts, tax documents, 
    and financial records into structured intelligence.
    """
)

app.include_router(exr)

@app.get("/")
def home():
    return {
        "API" : {
            "application" : "LedgerMind.ai",
            "version" : "1.0.0"
        }
    }