import jdatetime
import tkinter as tk
from tkinter import messagebox


def convert_date():
    input_date = entry.get()
    try:
        year, month, day = map(int, input_date.split('/'))
        jalali_date = jdatetime.date.fromgregorian(year=year, month=month, day=day)
        messagebox.showinfo("Converted Date", str(jalali_date))
    except ValueError:
        messagebox.showerror("Error", "Invalid date format!")


def show_description():
    description = "Please enter the date in the format: year/month/day"
    messagebox.showinfo("Date Format", description)


window = tk.Tk()
window.title("Date Converter - Use year/month/day format")

entry = tk.Entry(window)
entry.pack()

button_convert = tk.Button(window, text="Convert", command=convert_date)
button_convert.pack()

button_description = tk.Button(window, text="Show Description", command=show_description)
button_description.pack()

window.mainloop()
