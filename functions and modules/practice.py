# def password_strength(password):
#     if len(password) <8:
#         return "Weak password: must be at least 8 characters long."
#     if not any(char.isdigit() for char in password):
#         return "Weak password: must contain at least one digit."
#     if not any(char.isupper() for char in password):
#         return "Weak password: must contain at least one uppercase letter."
#     if not any(char.islower() for char in password):
#         return "Weak password: must contain at least one lowercase letter."
#     if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
#         return "Weak password: must contain at least one special character."
#     return "Strong password."

# password = input("Enter a password to check its strength: ")
# result = password_strength(password)
# print(result)
