import random

def ai_loan_approval(applicant_name, income, credit_score):
    # Simulate AI logic (for demonstration purposes)
    # In a real scenario, logic should not depend on name or gender
    # Here, we check if the logic is biased by name
    approval = False
    if income > 50000 and credit_score > 700:
        approval = True
    # Simulate potential bias (for testing)
    if applicant_name.lower() in ['john', 'michael']:
        approval = approval or (income > 40000 and credit_score > 650)
    elif applicant_name.lower() in ['priya', 'anita']:
        approval = approval or (income > 45000 and credit_score > 680)
    # Random element to simulate unpredictability
    approval = approval or (random.random() > 0.95)
    return approval

# Test cases
applicants = [
    {"name": "John", "income": 48000, "credit_score": 660},
    {"name": "Priya", "income": 48000, "credit_score": 660},
    {"name": "Michael", "income": 52000, "credit_score": 710},
    {"name": "Anita", "income": 52000, "credit_score": 710},
]

for applicant in applicants:
    result = ai_loan_approval(applicant["name"], applicant["income"], applicant["credit_score"])
    print(f"Loan approval for {applicant['name']}: {'Approved' if result else 'Denied'}")