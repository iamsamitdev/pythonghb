import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# สร้าง object tkinter
mainFrm = tk.Tk() # สร้างออบเจ็ค mainfrm

# แสดงข้อความที่ title bar
mainFrm.title("การเขียนโปรแกรม GUI ด้วยภาษาไพธอน") 

# กำหนดขนาดของ GUI
ttk.Frame(height=250, width=500).pack()
# img = ImageTk.PhotoImage(Image.open("images/samit.jpg"))

# แสดงรูปภาพ
# logo = tk.PhotoImage(file="images/samit.jpg")
label = ttk.Label(mainFrm, image=logo).place(x=0, y=0)
# label = ttk.Label(mainFrm, image=img).place(x=0, y=0)

mainFrm.mainloop() # แสดงผลหน้า GUI