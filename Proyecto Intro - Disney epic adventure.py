import tkinter as tk

root = tk.Tk()
root.geometry("1000x800")

root.title("Disney epic adventure!")

label = tk.Label(root, text="Disney epic adventure!", font=('Times new roman',50))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, font=('Arial', 15), height=2, width=15)
textbox.pack(padx=20)

myentry = tk.Entry(root)
myentry.pack()

button = tk.Button(root, text="Click me!", font=('Arial',18))
button.pack()



root.mainloop()