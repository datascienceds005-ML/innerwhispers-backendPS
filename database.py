"""
database.py — Simulated Mock Database Driver for InnerWhispers Backend
Provides execute_query, execute_write, and execute_many for standalone API testing.
"""

from typing import Any, Dict, List, Optional

async def execute_query(sql: str, params: Optional[tuple] = None) -> List[Dict[str, Any]]:
    """Simulates SELECT queries returning mock records for Finance and Admin modules."""
    sql_clean = " ".join(sql.strip().split()).lower()

    # 1. Transactions & Financial Overview
    if "from transactions" in sql_clean:
        if 'type="income"' in sql_clean or "type = 'income'" in sql_clean:
            return [{"totalIncome": 48299}]
        if 'type="expense"' in sql_clean or "type = 'expense'" in sql_clean:
            return [{"totalExpenses": 1500}]
        if "sum(approval_status='approved')" in sql_clean or "sum(approval_status = 'approved')" in sql_clean:
            return [{"totalExpenses": 1500, "approved": 1, "pending": 0, "rejected": 0}]
        if "group by month(date)" in sql_clean:
            return [{"month": "Sep", "total": 1500}]
        if "group by category" in sql_clean:
            return [{"category": "Operations", "total": 1500}]
        
        # Standard Transactions List
        return [
            {
                "id": 1,
                "party": "Aditya Rao",
                "partyType": "Patient",
                "doctor": "Dr. B. Navya Mounika",
                "type": "Consultation Fee",
                "amount": 1500,
                "date": "Yesterday",
                "dayBucket": "Yesterday",
                "method": "UPI",
                "status": "Paid",
                "description": "Consultation session"
            },
            {
                "id": 2,
                "party": "Yash Mehta",
                "partyType": "Patient",
                "doctor": "Dr. B. Navya Mounika",
                "type": "Consultation Fee",
                "amount": 1500,
                "date": "2 days ago",
                "dayBucket": "2 days ago",
                "method": "Card",
                "status": "Paid",
                "description": "Consultation session"
            },
            {
                "id": 3,
                "party": "NAU PBL Program",
                "partyType": "Institution",
                "doctor": "—",
                "type": "Institutional Subscription",
                "amount": 45000,
                "date": "5 Sep 2026",
                "dayBucket": "older",
                "method": "Bank Transfer",
                "status": "Paid",
                "description": "Institutional mental health plan"
            }
        ]

    # 2. Budgets
    if "from budgets" in sql_clean:
        return [
            {
                "id": 1,
                "category": "Clinical Staff Payouts",
                "name": "Clinical Staff Payouts",
                "budgeted": 250000,
                "spent": 182000,
                "total_amount": 250000,
                "duration": "Q3 2026"
            },
            {
                "id": 2,
                "category": "Platform Operations",
                "name": "Platform Operations",
                "budgeted": 80000,
                "spent": 64500,
                "total_amount": 80000,
                "duration": "Q3 2026"
            }
        ]
    if "from budget_categories" in sql_clean:
        return [{"name": "Operations", "amount": 80000}]

    # 3. Doctor Payouts (80/20 Model)
    if "from doctor_payouts" in sql_clean or "payout" in sql_clean:
        return [
            {
                "id": 1,
                "doctor": "Dr. B. Navya Mounika",
                "period": "This Week",
                "sessions": 2,
                "gross": 3000,
                "amount": 2400,
                "status": "Pending"
            },
            {
                "id": 2,
                "doctor": "Dr. Farah Sheikh",
                "period": "This Week",
                "sessions": 1,
                "gross": 1200,
                "amount": 960,
                "status": "Pending"
            }
        ]

    # 4. Admin Dashboard Analytics
    if "from interns" in sql_clean or "count(*)" in sql_clean:
        return [{"count": 12}]
    if "from attendance" in sql_clean:
        return [{"status": "Present", "count": 10}, {"status": "Absent", "count": 2}]
    if "from leave_requests" in sql_clean:
        return []

    return []

async def execute_write(sql: str, params: Optional[tuple] = None) -> Dict[str, Any]:
    """Simulates INSERT, UPDATE, DELETE write operations."""
    return {"affected_rows": 1, "insert_id": 1}

async def execute_many(sql: str, params_list: List[tuple]) -> Dict[str, Any]:
    """Simulates batch write operations."""
    return {"affected_rows": len(params_list)}
