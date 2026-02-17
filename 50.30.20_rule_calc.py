import tkinter as tk
from tkinter import messagebox

# 1. Calculation logic
def calculation(event=None):
    try:
        salary = float(entry.get())
        
        needs = salary * 0.50
        wants = salary * 0.30
        savings = salary * 0.20
        
        result_text = (f"Needs (50%): {needs:,.2f}\n"
                       f"Wants (30%): {wants:,.2f}\n"
                       f"Savings (20%): {savings:,.2f}")
        
        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number (e.g. 5000)")

# 2. GUI Setup
app = tk.Tk() 
app.title("Budget Calculator")
app.geometry("400x400")

# Input Field
label = tk.Label(app, text="Enter Monthly Salary:")
label.pack(pady=(20, 5))

entry = tk.Entry(app)
entry.pack(pady=10)
entry.focus_set() 

# Calculate Button
btn = tk.Button(app, text="Calculate", command=calculation) 
btn.pack(pady=20)

# Result Display
result_label = tk.Label(app, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=20)

entry.bind("<Return>", calculation) 
app.mainloop()

