
DataBase = ["ملح" , "لحم" , "حوم"] # هنا ضع الكلمات

#----------------------------------------- المكتبات
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter.messagebox import showinfo
#-------------------------------------------------------


#انشاء نافذة بمكتبة تكنتر والتحكم بخواصها
searchTool = tk.Tk()
searchTool.geometry("479x450+492+102")
searchTool.minsize(120, 1)
searchTool.maxsize(1370, 749)
searchTool.resizable(0,  0)
searchTool.title("اداة البحث في الكلمات العربية")
searchTool.configure(background="#353535")

# الملصق العلوي
Label1 = tk.Label(searchTool, anchor='center', background="#14afdc", foreground="#ffffff", text='''اداة البحث في الكلمات العربية''')
Label1.place(relx=0.0, rely=0.0, height=41, width=481)

#ملصقات شرح  البرنامج
Label2 = tk.Label(searchTool, anchor='w', background="#353535", foreground="#ffffff", text='''اهلا بك في اداة البحث في الكلمات العربية''')
Label2.place(x=230, y=60, height=21, width=399)

Label3 = tk.Label(searchTool, anchor='w', background="#353535", foreground="#ffffff", text='''كل ماعليك هو كتابة الاحرف المراد البحث فيها والفصل بين كل حرف وحرف بشرطة - واترك''')
Label3.place(relx=0.084, rely=0.2, height=21, width=399)

Label4 = tk.Label(searchTool, anchor='w', background="#353535", foreground="#ffffff", text='''الباقي على الاداة''')
Label4.place(relx=0.731, rely=0.267, height=21, width=91)

# مربع البحث
Search = tk.Entry(searchTool, background="#7d7d7d", font="TkFixedFont", foreground="#ffffff", relief="flat")
Search.place(relx=0.104, rely=0.4, height=20, relwidth=0.614)


def SearchGo():
    if Search.get().replace(" ","") == "" :
        showinfo("","قم بادخال الاحرف اولا")
    else :
        CharsList = Search.get()
        CharsList = CharsList.split('-')

        for i in range(len(CharsList)):
            CharsList[i] = CharsList[i].strip()

        Result = []

        for i in DataBase:
            for ii in CharsList:
                if ii in i:
                    continue
                else:
                    break
            else:
                Result.append(i)

        ResultView.delete(0, END)

        for i in Result:
            ResultView.insert(END , i)

        if ResultView.get(0) == "" :
            showinfo("","لا يوجد نتائج بحث")

Button1 = tk.Button(searchTool, background="#1d9bc0", compound='left', foreground="#ffffff", relief="flat", text='''ابدأ البحث''', command=SearchGo)
Button1.place(relx=0.104, rely=0.489, height=54, width=387)


#ملصقات اضافية

Label5 = tk.Label(searchTool, anchor='w', background="#353535", compound='left', foreground="#ffffff", text='''ضع الاحرف هنا''')
Label5.place(relx=0.752, rely=0.4, height=21, width=81)

Label6 = tk.Label(searchTool, anchor='w', background="#353535", compound='left', foreground="#ffffff", text='''نتائج البحث''')
Label6.place(relx=0.793, rely=0.667, height=21, width=61)


#مربع عرض نتائج البحث
ResultView = tk.Listbox(searchTool, background="#11889d", foreground="#ffffff", relief="flat")
ResultView.place(relx=0.104, rely=0.778, relheight=0.16, relwidth=0.823)

searchTool.mainloop()