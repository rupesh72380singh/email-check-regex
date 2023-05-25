# ^ = start karne ke liye
# + = join karne ke liye
# \ = serch karne ke liye
# \w = special character serach karne ke liye
# { = position
# ? = only 1 bar
import regex
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter the email:")
if regex.search( email_condition , user_email):
    print("right email")
else:
    print("wrong email")