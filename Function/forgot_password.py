def forgot_password(username, security_question, correct_answer, new_password):
    # Here you would typically have some database or data structure
    # where you store user information, such as username, security question, and correct answer.
    # For the sake of this example, let's assume we have a dictionary to store user data.
    users_data = {
        "user1": {"security_question": "What is your pet's name?", "correct_answer": "fluffy"},
        "user2": {"security_question": "What city were you born in?", "correct_answer": "new york"},
        # Add more users as needed...
    }

    # Check if the username exists in the user data
    if username in users_data:
        # Check if the provided security question matches the stored security question
        if security_question == users_data[username]["security_question"]:
            # Check if the provided answer matches the stored correct answer
            if correct_answer == users_data[username]["correct_answer"]:
                # Update the password with the new password
                # Here you would typically have a function to update the password in your database
                print("Password reset successfully!")
                return True
            else:
                print("Incorrect answer to security question.")
        else:
            print("Incorrect security question.")
    else:
        print("Username not found.")

    # Return False if the password reset was not successful
    return False

# Example usage:
forgot_password("user1", "What is your pet's name?", "fluffy", "new_password")
