# def mask_email(email):
#     if '@' not in email:
#         return "Invalid email"

#     local, domain = email.split('@', 1)
    
#     if len(local) < 1:
#         return "Invalid email"
    
#     masked_local = local[0] + '*' * (len(local) - 1)
#     return masked_local + '@' + domain

# emaa = input("Enter an email to mask: ")
# result = mask_email(emaa)
# print(result)
# def pascal_to_snake(text):
#     result = ""
#     for i in range(len(text)):
#         if text[i].isupper():
#             if i != 0:
#                 result += "_"
#             result += text[i].lower()
#         else:
#             result += text[i]
#     return result

# text = input("Enter a PascalCase string to convert to snake_case: ")
# result = pascal_to_snake(text)
# print(result)


def most_frequent_char(s):
    s = s.lower()
    freq = {}

    for char in s:
        if char.isalpha():  # Optional: skip spaces, digits, symbols
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

    # Now find max value
    max_char = ''
    max_count = 0

    for char in s:
        if char in freq and freq[char] > max_count:
            max_count = freq[char]
            max_char = char

    return max_char
s = input("Enter a string to find the most frequent character: ")
result = most_frequent_char(s) 
print(f"The most frequent character is: '{result}'")