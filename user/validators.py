# import re

# def email_validator(email):
#     is_email = re.compile(r'^[a-zA-Z0-9+-_.]+@([a-zA-Z0-9-]{4,})+\.[a-zA-Z0-9-.]+$')
#     if not is_email.fullmatch(email):
#         return False
#     return True


# def password_check_validator(password, password_check):
#     if password == '':
#         return False
#     else:
#         if password != password_check:
#             return False
#         else:
#             return True

# def password_vaildator(phone, phone2):
#     is_password = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@!%*#?&])[A-Za-z\d@!%*#?&]{8,}$')
#     if not is_password.fullmatch(phone) or not is_password.fullmatch(phone2):
#         return False
#     return True