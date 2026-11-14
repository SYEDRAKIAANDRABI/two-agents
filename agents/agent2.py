
failed_attempts = 0

def login(username, password):

    global failed_attempts

    correct_username = "admin"
    correct_password = "1234"

    if failed_attempts >= 3:
        return "Account locked"

    if username == correct_username and password == correct_password:
        failed_attempts = 0
        return "Login successful"

    failed_attempts += 1
    return "Invalid credentials"
