import tkinter as tk

def go_back():
    # Implement the functionality to go back here
    print("Going back...")  # Placeholder for actual functionality

# Create a Tkinter window
window = tk.Tk()
window.title("Back Button Example")

# Create a "Back" button
back_button = tk.Button(window, text="Back", command=go_back)
back_button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
