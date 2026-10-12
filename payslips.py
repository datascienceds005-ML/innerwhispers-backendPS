from fastapi import APIRouter
from typing import List, Dict, Any

router = APIRouter(prefix="/api/payslips", tags=["Payslips"])

PAYSLIPS_DATA: List[Dict[str, Any]] = [
    {"slip_id": "PS-2026-01", "name": "Dr. B. Navya Mounika", "role": "Senior Psychiatrist", "sessions": 12, "gross_amount": 2400.0, "status": "Disbursed"},
    {"slip_id": "PS-2026-02", "name": "Dr. Farah Sheikh", "role": "Clinical Psychologist", "sessions": 8, "gross_amount": 1600.0, "status": "Generated"},
    {"slip_id": "PS-2026-03", "name": "Sneha Kulkarni", "role": "Counselor", "sessions": 5, "gross_amount": 880.0, "status": "Pending"},
]

@router.get("")
@router.get("/")
@router.get("/list")
async def get_payslips_data():
    total_pool = sum(slip["gross_amount"] for slip in PAYSLIPS_DATA)
    disbursed = sum(slip["gross_amount"] for slip in PAYSLIPS_DATA if slip["status"] == "Disbursed")
    pending = sum(slip["gross_amount"] for slip in PAYSLIPS_DATA if slip["status"] == "Pending")

    return {
        "status": "success",
        "total_payout_pool": total_pool,
        "disbursed_amount": disbursed,
        "pending_amount": pending,
        "records": PAYSLIPS_DATA
    }
