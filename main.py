import tkinter.filedialog
from tkinter import *
from tkinter import ttk, filedialog

file = None
datas = []


def importing():
    filetypes = (
        ('szöveges fájl', '*.txt'),
    )

    filename = filedialog.askopenfilename(
        title='Importálás',
        filetypes = filetypes
    )
    print(filename)
    file = open(filename,encoding="utf-8")
    for index in file:
        index = index.strip().split("\t")
        datas.append(index)
    for word in datas:
        table.insert(parent='', index='end', text='',
                     values=(word[0], word[1]))
    ws.update()


ws = Tk()
ws.title("Quizlet pdf generátor")
ws.geometry('800x800')


table = ttk.Treeview(ws)

table['columns']=('term', 'definition')

table.column("#0", width=0,  stretch=NO)
table.column('term', width=200)
table.column('definition', width=250)

table.heading('term', text='Kifejezés')
table.heading('definition', text='Fogalom')

for word in datas:
    table.insert(parent='',index='end',text='',
                 values=(word[0], word[1]))


clearbutton = ttk.Button(
    ws,
    text='Importálás',
    command=importing
)


table.pack()
clearbutton.pack()
ws.mainloop()
