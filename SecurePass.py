import re

def assess_password_strength(password):
    """Assesses the strength of a password based on specific criteria."""
    # Initialize strength score
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Assess the overall strength
    if strength == 5:
        feedback.append("Password is strong.")
    elif strength == 4:
        feedback.append("Password is medium strength.")
    else:
        feedback.append("Password is weak.")

    return feedback


# Menu-driven interface
def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    feedback = assess_password_strength(password)
    
    for item in feedback:
        print(item)


if __name__ == "__main__":
    main()
