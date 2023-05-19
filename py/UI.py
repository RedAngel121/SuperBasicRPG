import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Get the directory path of the Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

def shake_window():
    # Get the current position of the window
    x = root.winfo_x()
    y = root.winfo_y()

    # Shake the window by moving it back and forth
    for i in range(5):
        if i % 2 == 0:
            root.geometry(f"+{x + 7}+{y}")
        else:
            root.geometry(f"+{x - 7}+{y}")
        root.update()
        root.after(50)
        
def start_game():
    print("Starting a new game...")
    # Add your game logic here

def load_game():
    print("Loading game...")
    # Add your load game logic here

def open_inventory_window():
    inventory_window = tk.Toplevel(root)
    inventory_window.title("Inventory")
    
    # Calculate the required height of the inventory window based on the number of items
    num_items = 10  # Replace this with the actual number of items
    item_height = 25  # Height of each item in pixels
    inventory_width = 200
    inventory_height = num_items * item_height + 50  # Adjust the height based on the number of items
    inventory_window.geometry(f"{inventory_width}x{inventory_height}")

    # Create widgets and layout for the inventory window here
    
    # Status Labels
    for i in range(num_items):
        item_label = tk.Label(inventory_window, text=f"Item {i+1}")
        item_label.pack()

    quit_button = tk.Button(inventory_window, text="Quit", command=inventory_window.destroy)
    quit_button.pack(side=tk.TOP)  # Align to the right side with padding

def close_inventory_tab(tab):
    # Remove the tab from the notebook
    notebook.forget(tab)

def quit_game():
    print("Quitting the game...")
    # Add any cleanup or saving logic here
    root.destroy()

def open_inventory():
    # Create a new tab
    inventory_tab = ttk.Frame(notebook)
    notebook.add(inventory_tab, text="Inventory")

    # Create a close button for the tab
    close_button = ttk.Button(inventory_tab, text="X", width=10, command=lambda: close_inventory_tab(inventory_tab))
    close_button.pack(side=tk.RIGHT, padx=5, pady=5)

    # Add content to the inventory tab
    inventory_label = ttk.Label(inventory_tab, text="Inventory Content")
    inventory_label.pack(padx=10, pady=10)

# Create the main window
root = tk.Tk()
root.title("Super Basic RPG")

# Construct the absolute path to the image file
image_filename = "cat.png"  # Replace with the filename of your image
image_path = os.path.join(script_dir, image_filename)
background_image = Image.open(image_path)
background_photo = ImageTk.PhotoImage(background_image)

# Create a Canvas widget and place the background image on it
canvas = tk.Canvas(root, width=background_image.width, height=background_image.height)
canvas.pack()
canvas.create_image(0, 0, image=background_photo, anchor=tk.NW)

# Create a notebook widget
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

"""
# Load the image
image = Image.open(image_path)

# Calculate the aspect ratio to maintain the image's original proportions
window_width = 200
window_height = 200
aspect_ratio = min(window_width / image.width, window_height / image.height)
new_width = int(image.width * aspect_ratio)
new_height = int(image.height * aspect_ratio)

# Resize the image to fit the available space
image = image.resize((new_width, new_height))
photo = ImageTk.PhotoImage(image)

# Create the image label and display the image
image_label = tk.Label(root, image=photo)
image_label.pack()
"""

# Create buttons
start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(side=tk.TOP)  # Add padding

load_button = tk.Button(root, text="Load Game", command=load_game)
load_button.pack(side=tk.TOP)   # Add padding

# Create a button to open the inventory tab
inventory_button = ttk.Button(root, text="Open Inventory", command=open_inventory)
inventory_button.pack(pady=10)

shake_button = tk.Button(root, text="Shake", command=shake_window)
shake_button.pack(side=tk.TOP)

quit_button = tk.Button(root, text="Quit", command=quit_game)
quit_button.pack(side=tk.TOP)   # Align to the right side with padding

# Start the main event loop
root.mainloop()