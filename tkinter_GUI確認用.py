import tkinter as tk

root = tk.Tk()
root.geometry("350x400")


#red
canvas_red = tk.Canvas(
    width=50,
    height=50,
    bg="red"
)
canvas_red.grid(
    row=0
)

#green
canvas_green = tk.Canvas(
    width=50,
    height=50,
    bg="green"
)
canvas_green.grid(
    row=1
)

#blue
canvas_blue = tk.Canvas(
    width=50,
    height=50,
    bg="blue"
)
canvas_blue.grid(
    row=2
)

button1 = tk.Button(
    text="ボタン１"
)
button1.grid(
    row=3,
    sticky=tk.NSEW
)

text_box = tk.Text()
text_box.grid(
    row=4,
    padx = 0,
    pady = 0
)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(4,weight=1)

root.mainloop()