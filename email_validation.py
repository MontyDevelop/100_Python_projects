# ----------Simple version------------

# email = input("Enter your email address: ")

# list1 = []
# for i in range(len(email)):
#     if email[i] =="@" or email[i] == ".":
#         list1.append(i)
# print(list1)
 
# if len(email) >= 6: #g@g.in
#     if "@" in email:
#         if "." in email:
#             if " " not in email:
#                 if 0 not in list1 and (len(email)-1) not in list1:
#                     print("Valid Email address")
#                 else:
#                     print("Not a valid Email address")
#             else:
#                 print("Not a valid Email address")        
#         else:
#             print("Not a valid Email address")
#     else:
#         print("Not a valid Email address")
# else:
#     print("Not a valid Email address")            


# -----------------------regex version--------------------------
import re

email = input("Enter your email address: ")
# pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
pattern = r'^(?![._])[a-zA-Z0-9._]+(?<![._])@[a-zA-Z]+(\.[a-zA-Z]{2,})+$'

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")

# ^ → start of string
# [a-zA-Z0-9._]+ → username
# @ → must exist once
# [a-zA-Z]+ → domain name
# \. → dot
# [a-zA-Z]{2,} → extension (min 2 letters)
# $ → end of string

# Real systems:

# Use regex for basic filtering
# Then verify using email confirmation