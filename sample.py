from PIL import Image, ImageTk
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox

# Sample numbers set to ensure uniqueness
existing_sample_numbers = set()

# Function to save reagent details
def save_details():
    sample_number = entry_sample_number.get()
    reagent_name = entry_name.get()
    parameter = entry_parameter.get()
    department = entry_department.get()
    machine_name = entry_machine_name.get()
    quantity = entry_quantity.get()
    unit = quantity_unit_var.get()
    expiry_date = entry_expiry.get()

    if not sample_number or not reagent_name or not parameter or not department or not machine_name or not quantity or not expiry_date:
        messagebox.showerror("Error", "All fields are required!")
        return

    if sample_number in existing_sample_numbers:
        messagebox.showerror("Error", "Sample Number must be unique!")
        return

    # Save the sample number to the set to ensure uniqueness
    existing_sample_numbers.add(sample_number)

    # Display the entered details (replace with database logic if needed)
    print(f"Sample Number: {sample_number}")
    print(f"Reagent Name: {reagent_name}")
    print(f"Parameter: {parameter}")
    print(f"Department: {department}")
    print(f"Machine Name: {machine_name}")
    print(f"Quantity: {quantity} {unit}")
    print(f"Expiry Date: {expiry_date}")

    messagebox.showinfo("Success", "Reagent details saved successfully!")

    # Clear the input fields
    entry_sample_number.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_parameter.delete(0, tk.END)
    entry_department.delete(0, tk.END)
    entry_machine_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    quantity_unit_var.set("ml")
    entry_expiry.set_date("")

# Create the main window
root = tk.Tk()
root.title("Lab Reagent Input Form")
root.geometry("600x600")

# Load a local background image
try:
    bg_image = Image.open("lab.jpg")  # Replace with the correct path if not in the same directory
    bg_image = bg_image.resize((600, 600), Image.Resampling.LANCZOS)  # Resize to fit the window
    bg_photo = ImageTk.PhotoImage(bg_image)
except Exception as e:
    messagebox.showerror("Error", f"Unable to load background image: {e}")
    bg_photo = None

# Create canvas
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack(fill="both", expand=True)

if bg_photo:
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Add widgets on top of the canvas
canvas.create_text(300, 30, text="Lab Reagent Input Form", font=("Helvetica", 18, "bold"), fill="#FF5733")

canvas.create_text(100, 80, text="Sample Number:", font=("Helvetica", 12, "bold"), fill="black")
entry_sample_number = tk.Entry(root, width=30, font=("Helvetica", 12))
entry_sample_number_window = canvas.create_window(300, 80, window=entry_sample_number)

canvas.create_text(100, 120, text="Reagent Name:", font=("Helvetica", 12, "bold"), fill="black")
entry_name = tk.Entry(root, width=30, font=("Helvetica", 12))
entry_name_window = canvas.create_window(300, 120, window=entry_name)

canvas.create_text(100, 160, text="Parameter:", font=("Helvetica", 12, "bold"), fill="black")
entry_parameter = tk.Entry(root, width=30, font=("Helvetica", 12))
entry_parameter_window = canvas.create_window(300, 160, window=entry_parameter)

canvas.create_text(100, 200, text="Department:", font=("Helvetica", 12, "bold"), fill="black")
entry_department = tk.Entry(root, width=30, font=("Helvetica", 12))
entry_department_window = canvas.create_window(300, 200, window=entry_department)

canvas.create_text(100, 240, text="Machine Name:", font=("Helvetica", 12, "bold"), fill="black")
entry_machine_name = tk.Entry(root, width=30, font=("Helvetica", 12))
entry_machine_name_window = canvas.create_window(300, 240, window=entry_machine_name)

canvas.create_text(100, 280, text="Quantity:", font=("Helvetica", 12, "bold"), fill="black")
entry_quantity = tk.Entry(root, width=15, font=("Helvetica", 12))
entry_quantity_window = canvas.create_window(240, 280, window=entry_quantity)

quantity_unit_var = tk.StringVar(value="ml")
quantity_unit_menu = tk.OptionMenu(root, quantity_unit_var, "ml", "l")
quantity_unit_menu.config(cursor="hand2")  # Add hover effect
quantity_unit_window = canvas.create_window(360, 280, window=quantity_unit_menu)

canvas.create_text(100, 320, text="Expiry Date:", font=("Helvetica", 12, "bold"), fill="black")
entry_expiry = DateEntry(root, width=27, background='darkblue', foreground='black', borderwidth=2)
entry_expiry_window = canvas.create_window(300, 320, window=entry_expiry)

# Save button with hand cursor
save_button = tk.Button(root, text="Save", command=save_details, bg="white", fg="black", font=("Helvetica", 12, "bold"), cursor="hand2")
save_button_window = canvas.create_window(300, 380, window=save_button)

# Run the application
root.mainloop()
