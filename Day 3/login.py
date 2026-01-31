def login_requrired(func):
    def wrapper(user):
        if user == "admin":
            return func(user)
        else:
            return "Access Denied"
    return wrapper

@login_requrired
def dashboard(user):
    return f"Welcome to the dashboard!"

print(dashboard("admin"))  # Should print the welcome message
print(dashboard("guest"))  # Should print "Access Denied"