# An Email slicer is a very useful program for separating the username and domain name of an email address. In this Example, I (Sharad Khare) will explain how to write a program to create an Email Slicer with Python.
# sharad@datacode.com (example)

email = input("Please Enter your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_) 