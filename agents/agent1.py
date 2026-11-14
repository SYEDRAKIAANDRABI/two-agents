 
def login(username, password):

    if not username:
        return "Username cannot be empty"

    if not password:
        return "Password cannot be empty"

    correct_username = "admin"
    correct_password = "1234"

    if username == correct_username and password == correct_password:
        return "Login successful"

    return "Invalid credentials"
