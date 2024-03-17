import tkinter as tk

def on_button_click():
    print("Button clicked!")

# Create a Tkinter window
window = tk.Tk()
window.title("On Click Function Example")

# Create a button widget
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
