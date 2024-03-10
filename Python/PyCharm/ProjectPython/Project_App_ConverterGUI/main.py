from tkinter import *

LIGHTSTEELBLUE = "#b0c4de"
GREEN = "#9bdeac"

# Create the main window.
window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=320, height=150)
window.config(bg=LIGHTSTEELBLUE, padx=55, pady=25)


def miles_to_km():
    km_result_label.config(text=f"{round(float(miles_input.get()) * 1.60934, 2)}")


miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0, padx=5, pady=5)
miles_input.config(bg=GREEN)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0, padx=5, pady=5)
miles_label.config(bg=LIGHTSTEELBLUE)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1, padx=5, pady=5)
is_equal_label.config(bg=LIGHTSTEELBLUE)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1, padx=5, pady=5)
km_result_label.config(bg=LIGHTSTEELBLUE)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1, padx=5, pady=5)
kilometer_label.config(bg=LIGHTSTEELBLUE)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2, padx=5, pady=5)
calculate_button.config(bg=LIGHTSTEELBLUE)


window.mainloop()
