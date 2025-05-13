import string

def check_password_strength(password):
    length_criteria = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    # Scoring system
    score = sum([length_criteria, has_upper, has_lower, has_digit, has_symbol])

    # Feedback
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    # Detailed feedback
    print("\n--- Password Analysis ---")
    print(f"Length OK: {'O' if length_criteria else 'X'}")
    print(f"Uppercase: {'O' if has_upper else 'X'}")
    print(f"Lowercase: {'O' if has_lower else 'X'}")
    print(f"Digit: {'O' if has_digit else 'X'}")
    print(f"Symbol: {'O' if has_symbol else 'X'}")
    print(f"\nPassword Strength: {strength}")

# Run the checker
user_password = input("Enter a password to check its strength: ")
check_password_strength(user_password)
