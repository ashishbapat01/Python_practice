def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage:
file_path = "example.txt"
file_content = read_file(file_path)
print(file_content)
