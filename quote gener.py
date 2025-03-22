import tkinter as tk
import random
quotes = ['i am the god',
          'cold water feels warm when hands are freezing']
def gen():
    'genrate'
    random_quote=random.choice(quotes)
    quote_label.config(text=random_quote)

root = tk.Tk()
root.title('quote')
quote_label = tk.Label(root , text="",wraplength=400, justify="center")
quote_label.pack(pady=20)

generate_b = tk.Button(root, text="Generate quote",command=gen)
generate_b.pack()

root.mainloop()