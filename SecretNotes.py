from tkinter import * 
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
from tkinter import messagebox

window = Tk()
window.title("Secret Notes")
window.minsize(width=600, height=600)

content = StringVar()

def check_input(title, secret, master_key):
    if not title or not secret or not master_key:
        messagebox.showerror("Hata", "Alanlari doğru bir şekilde doldurun!")
        return False
    return True
def callback():
    title = content.get()
    secret = secret_text.get("1.0",END.strip())
    master_key = master_entry.get()

    if not check_input(title,secret,master_key):
        return
    
    secret_content = secret_text.get("1.0", END)
    with open('SecretNotes.txt',"a") as file:
        file.write(content.get() + "\n")
        file.write(secret_content)
    messagebox.showinfo("Başarili","Notlariniz Başariyla Kaydedildi.")

key1 = b'u8RAvUKIPE3w3VLklEqXv4466uCeEvlKxCvdvEjxDUs='

#Logo
image = Image.open('secrett.png')
image = ImageTk.PhotoImage(image)

image_label = Label(window, image=image)
image_label.pack(side="top")
image_label.config(width=200, height=200)

#Title Label
title_label = Label(text="Enter Your Title: ",font=("Arial",14,"normal"))
title_label.pack()
title_label.config(padx=20,pady=20)

#Title Entry
title_entry = Entry(window,textvariable=content,width=45)
title_entry.pack()


#Secret Label
secret_label = Label(text="Enter Your Secret: ",font=("Arial",14,"normal"))
secret_label.pack()
secret_label.config(padx=10,pady=10)

#Secret Text
secret_text = Text(window,width=30,height=10)
secret_text.pack()

#Master Key Label
master_label = Label(text="Enter Master Key: ",font=("Arial",14,"normal"))
master_label.pack()
master_label.config(padx=15,pady=15)

#Master Key Entry
master_entry= Entry(width=45)
master_entry.pack()

#Save&Encrypt Button
save_btn = Button(window,text="Save&Encrypt",command=callback)
save_btn.pack()
save_btn.config(padx=8,pady=8)

#Decrypt Button
decrypt_btn = Button(text="Decrypt")
decrypt_btn.pack()
decrypt_btn.config(padx=8,pady=8)



window.mainloop()