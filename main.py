import tkinter as tk

mapping = {
    ord(' '): '_', ord('а'): 'a', ord('б'): '6', ord('в'): 'B', ord('г'): 'r',
    ord('д'): 'g', ord('е'): 'e', ord('ё'): 'e', ord('ж'): 'JIL', ord('з'): '3',
    ord('и'): 'u', ord('й'): 'u', ord('к'): 'K', ord('л'): 'JI', ord('м'): 'M',
    ord('н'): 'H', ord('о'): '0', ord('п'): 'n', ord('р'): 'p', ord('с'): 'c',
    ord('т'): 'T', ord('у'): 'y', ord('ф'): 'F', ord('х'): 'x', ord('ц'): 'u',
    ord('ч'): '4', ord('ш'): 'III', ord('щ'): 'IIl', ord('ъ'): 'b', ord('ы'): 'bI',
    ord('ь'): 'b', ord('э'): 'e', ord('ю'): 'IO', ord('я'): '9I'
}

root = tk.Tk()
root.geometry("335x55")

input_entry = tk.Entry(root, width=40)
input_entry.pack()

var = tk.StringVar()
output_entry = tk.Entry(root, textvariable=var, width=40)
output_entry.pack()


def on_change(*args):
    s = input_var.get().lower()
    var.set(s.translate(mapping))

input_var = tk.StringVar()
input_entry.config(textvariable=input_var)
input_var.trace_add("write", on_change)




root.mainloop()
