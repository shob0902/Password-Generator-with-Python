import tkinter as tk
import string
import random
#Function for generating password
def gen_pass():
    p = []
    for _ in range(5):
        alp = random.choice(string.ascii_letters)
        sym = random.choice(string.punctuation)
        n = random.choice(string.digits)
        p.append(alp)
        p.append(sym)
        p.append(n)
    genPass = ''.join(p)# Join list into a single string
    l.config(text="Generated Password:\n" + genPass)
root = tk.Tk()#Application window
root.title("Password Generator")
root.geometry("400x200")
root.config(bg="#f0f0f0")
b = tk.Button(root, text="Generate Password", font=("Arial", 14), command=gen_pass)#Button
b.pack(pady=20)
l = tk.Label(root, font=("Arial", 12, "bold"), fg="green", bg="#f0f0f0")#Displaying password
l.pack(pady=20)
root.mainloop()#Run
