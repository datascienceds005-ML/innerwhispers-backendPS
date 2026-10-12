from fastapi import APIRouter
from typing import List, Dict, Any

router = APIRouter(prefix="/api/expenses", tags=["Expenses"])

# In-memory / initial data layer (Migrated from Node.js)
EXPENSES_DATA: List[Dict[str, Any]] = [
    {"id": 1, "title": "AWS Cloud Infrastructure", "category": "Infrastructure", "amount": 14200.0, "date": "2026-10-01", "status": "Paid"},
    {"id": 2, "title": "Clinical Staff Stipend Pool", "category": "Payroll", "amount": 45000.0, "date": "2026-10-02", "status": "Paid"},
    {"id": 3, "title": "Outreach & Digital Marketing", "category": "Marketing", "amount": 8500.0, "date": "2026-10-03", "status": "Pending"},
    {"id": 4, "title": "Admin & Office Operations", "category": "Operations", "amount": 2300.0, "date": "2026-10-04", "status": "Paid"},
]

@router.get("")
@router.get("/")
@router.get("/summary")
async def get_expenses_summary():
    total_spent = sum(item["amount"] for item in EXPENSES_DATA)
    pending_spent = sum(item["amount"] for item in EXPENSES_DATA if item["status"] == "Pending")
    paid_spent = sum(item["amount"] for item in EXPENSES_DATA if item["status"] == "Paid")
    
    return {
        "status": "success",
        "total_expenses": total_spent,
        "paid_expenses": paid_spent,
        "pending_expenses": pending_spent,
        "total_records": len(EXPENSES_DATA),
        "expenses": EXPENSES_DATA
    }
