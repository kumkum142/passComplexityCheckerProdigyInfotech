import re

def password_strength(password):
    # Initialize strength variables
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password)
    uppercase_criteria = re.search(r'[A-Z]', password)
    number_criteria = re.search(r'\d', password)
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    
    # Initialize score
    score = 0
    
    # Check each criterion and update the score
    if length_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if number_criteria:
        score += 1
    if special_char_criteria:
        score += 1
    
    # Determine strength based on score
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
    
    return strength

def provide_feedback(password):
    strength = password_strength(password)
    feedback = f"Password strength: {strength}\n"
    
    if strength == "Weak":
        feedback += "Consider adding more characters, including uppercase letters, numbers, and special characters."
    elif strength == "Medium":
        feedback += "Your password is fairly strong, but you can make it stronger by adding special characters or more length."
    else:
        feedback += "Your password is strong."
    
    return feedback

# Test the function
password = input("Enter a password to check its strength: ")
print(provide_feedback(password))
