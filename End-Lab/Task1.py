def clean_email_data(email_list):
    """
    Clean a list of email addresses by:
    1. Converting all characters to lowercase
    2. Removing leading/trailing whitespace
    3. Removing duplicate email addresses while keeping order
    
    Parameters:
        email_list (list): A list containing email address strings.
    
    Returns:
        list: A cleaned list of unique, standardized email addresses.
    """

    # Step 1: Apply strip() and lower() to every email using a list comprehension
    cleaned_list = [email.strip().lower() for email in email_list]

    # Step 2: Remove duplicates while preserving the original order
    # Using a set to track seen items (AI-suggested optimal approach for O(n) performance)
    unique_emails = []
    seen = set()

    for email in cleaned_list:
        if email not in seen:
            unique_emails.append(email)
            seen.add(email)

    return unique_emails



