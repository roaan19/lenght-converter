import tkinter as tk

def convert_length():
    try:
        meters = float(entry.get())
        feet = meters * 3.28084
        result_label.config(text=f"{feet:.2f} feet")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.configure(bg="#f0f4f7")  

title_label = tk.Label(root, text="Meters to Feet Converter", font=("Helvetica", 16), fg="#2c3e50", bg="#f0f4f7")
title_label.pack(pady=20)

entry = tk.Entry(root, font=("Helvetica", 14), bg="#ecf0f1", fg="#2c3e50")
entry.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_length, font=("Helvetica", 12, "bold"), bg="#3498db", fg="white")
convert_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14), fg="#27ae60", bg="#f0f4f7")
result_label.pack(pady=20)

root.mainloop()
