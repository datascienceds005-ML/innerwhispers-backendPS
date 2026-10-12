from fastapi import APIRouter
from typing import List, Dict, Any

router = APIRouter(prefix="/api/invoices", tags=["Invoices"])

INVOICES_DATA: List[Dict[str, Any]] = [
    {"invoice_no": "INV-2026-001", "client": "National University Health", "amount": 45000.0, "date": "2026-09-28", "due_date": "2026-10-15", "status": "Settled"},
    {"invoice_no": "INV-2026-002", "client": "Apex Wellness Center", "amount": 18500.0, "date": "2026-10-01", "due_date": "2026-10-20", "status": "Unpaid"},
    {"invoice_no": "INV-2026-003", "client": "Student Counseling Cell", "amount": 6100.0, "date": "2026-10-02", "due_date": "2026-10-10", "status": "Settled"},
]

@router.get("")
@router.get("/")
@router.get("/all")
async def get_invoices_data():
    total_invoiced = sum(inv["amount"] for inv in INVOICES_DATA)
    settled_amount = sum(inv["amount"] for inv in INVOICES_DATA if inv["status"] == "Settled")
    unpaid_amount = sum(inv["amount"] for inv in INVOICES_DATA if inv["status"] == "Unpaid")

    return {
        "status": "success",
        "total_billed": total_invoiced,
        "settled_amount": settled_amount,
        "unpaid_amount": unpaid_amount,
        "invoices": INVOICES_DATA
    }
