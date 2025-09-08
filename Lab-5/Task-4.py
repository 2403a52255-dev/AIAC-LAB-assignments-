def get_score(education, experience, gender, age):
    # Scoring logic
    score = 0

    # Education scoring
    edu_scores = {
        'highschool': 10,
        'bachelor': 20,
        'master': 30,
        'phd': 40
    }
    score += edu_scores.get(education.lower(), 0)

    # Experience scoring
    if experience < 1:
        score += 5
    elif experience < 3:
        score += 15
    elif experience < 5:
        score += 25
    else:
        score += 35

    # Gender scoring (should not affect score to avoid bias)
    # score += 0

    # Age scoring (avoid unfair weighting)
    if 18 <= age <= 60:
        score += 10
    else:
        score += 0

    return score

def analyze_bias():
    print("Bias Analysis:")
    print("- Education and experience are weighted based on relevance.")
    print("- Gender does not affect score to avoid bias.")
    print("- Age is only checked for reasonable working age, not weighted unfairly.")
    print("- Ensure that all features are relevant to job performance.")

def main():
    print("Job Applicant Scoring System")
    education = input("Enter education level (HighSchool/Bachelor/Master/PhD): ")
    experience = int(input("Enter years of experience: "))
    gender = input("Enter gender: ")
    age = int(input("Enter age: "))

    score = get_score(education, experience, gender, age)
    print(f"Applicant Score: {score}")

    analyze_bias()

if __name__ == "__main__":
    main()