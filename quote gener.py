import tkinter as tk
import random
import winsound 
quotes = ['the longer you stay on the train going the wrong direction the more expensive it will be to get home',
          'cold water feels warm when hands are freezing',
          'a focused fool will always accomplish more than a distracted genius',
          'lessons in life will be repeated until they are learned',
          'you decide what you are',
          'actions speak louder than words',
          "LIFE IS HARD BUT I'M HARDER",
          "it won't happen overnight, but if you give up, it won't happen at all"]
def sound():
    winsound.playsound("SystemAsterisk", winsound.SND_ALIAS)
def gen():
    'genrate'
    random_quote=random.choice(quotes)
    quote_label.config(text=random_quote , bg='grey')

root = tk.Tk()
root.title('quote')
root.geometry('400x200')
root.configure(bg='grey')

quote_label = tk.Label(root , text="",wraplength=350, justify="center",font=("Georgia", 16, "bold italic"))
quote_label.pack(pady=20)

generate_b = tk.Button(root, text="Generate quote",command=gen,bg='grey' , fg='white')
generate_b.pack()

gen()

root.mainloop()