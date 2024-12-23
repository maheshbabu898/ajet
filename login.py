def login(username, password):
    # Sample users database
    users = {'user1': 'pass1', 'user2': 'pass2'}
    if username in users and users[username] == password:
        return "Login successful!"
    return "Invalid username or password."

# Example usage
if __name__ == "__main__":
    print(login("user1", "pass1"))  # Expected: Login successful!
