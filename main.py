from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

# Routers Import
import finance
import expenses
import invoices
import payslips

app = FastAPI(title="InnerWhispers Platform Backend")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. API Routers Include
app.include_router(finance.router)
app.include_router(expenses.router)
app.include_router(invoices.router)
app.include_router(payslips.router)

# 2. HTML Frontend File Serving Routes
@app.get("/")
def serve_home():
    return FileResponse("finance.html")

@app.get("/budget")
def serve_budget():
    return FileResponse("budget.html")

@app.get("/dashboard")
def serve_dashboard():
    return FileResponse("dashboard.html")

@app.get("/expenses")
def serve_expenses():
    return FileResponse("expenses.html")

@app.get("/invoices")
def serve_invoices():
    return FileResponse("invoices.html")

@app.get("/payslips")
def serve_payslips():
    return FileResponse("payslips.html")
