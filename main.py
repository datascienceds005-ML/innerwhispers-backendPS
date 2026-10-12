from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

# 1. Routers Import (पुराने और नए modules)
import finance
import expenses  # <--- आपका expenses.py यहाँ import हुआ

app = FastAPI(title="InnerWhispers Platform Backend")

# 2. CORS Middleware (ताकि frontend आसानी से fetch कर सके)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. API Routers Include
app.include_router(finance.router)
app.include_router(expenses.router)  # <--- expenses API router यहाँ attach हुआ

# 4. Frontend HTML Routes
@app.get("/")
def serve_home():
    return FileResponse("finance.html")

@app.get("/budget")
def serve_budget():
    return FileResponse("budget.html")

@app.get("/dashboard")
def serve_dashboard():
    return FileResponse("dashboard.html")

# <--- नया route: expenses.html दिखाने के लिए --->
@app.get("/expenses")
def serve_expenses():
    return FileResponse("expenses.html")
