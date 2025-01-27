import tkinter


def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I am a Label")
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=3, row=0)

# Entry

input = tkinter.Entry(width=12)
print(input.get())
input.grid(column=4, row=2)


window.mainloop()
