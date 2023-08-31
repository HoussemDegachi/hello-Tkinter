import tkinter

# functions
def add_phrase():
    if text_type.get() == "upper":
        phrase_content = user_input.get().upper()
    else:
        phrase_content = user_input.get()

    tkinter.Label(output_frame, text = phrase_content, bg = "#ADD8E6").pack(pady = (0, 4))

# define window
root = tkinter.Tk()
root.config(bg="#123456")
root.title("hello gui")
root.iconbitmap("wave.ico")
root.geometry("350x400")
root.resizable(False, False)

# create layout
input_frame = tkinter.Frame(root, width = 200, height = 100, bg = "#00008B")
output_frame = tkinter.Frame(root, height = 500, bg = "#ADD8E6")
output_frame.pack_propagate()

# create input frame content
text_type = tkinter.StringVar()
text_type.set("normal")

user_input = tkinter.Entry(input_frame)
submit_button = tkinter.Button(input_frame, text = "submit", command = add_phrase)
normal_radio_btn = tkinter.Radiobutton(input_frame, text = "Normal case", value = "normal", bg = "#00008B", fg = "#ADD8E6", variable = text_type)
upper_radio_btn = tkinter.Radiobutton(input_frame, text = "Upper case", value = "upper", bg = "#00008B", fg = "#ADD8E6", variable = text_type)

# display input frame content
user_input.grid(column = 0, row = 0, padx = (10, 20), pady = (10, 20), )
submit_button.grid(column = 1, row = 0, ipadx = 20, pady = (10, 20), padx = 10)
normal_radio_btn.grid(column = 0, row = 1)
upper_radio_btn.grid(column = 1, row = 1)

# display layout
input_frame.pack(pady = 10, padx = 10)
output_frame.pack(pady = (0, 10), padx = 10, ipadx = 16, ipady = 16, fill = "both")
output_frame.pack_propagate(False)

# run window
root.mainloop()