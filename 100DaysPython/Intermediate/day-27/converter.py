from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to km Converter")
window.config(padx=150, pady=150)

miles_input = Entry(width=10)
miles_input.grid(column=5, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=6, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=4, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=5, row=1)

km_label = Label(text="km")
km_label.grid(column=6, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=5, row=2)

window.mainloop()
