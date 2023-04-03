import tkinter.filedialog
from tkinter import *
from tkinter import ttk, filedialog
import pandas

file = None
datas = []


def importing():
    # Clearing the table of previous data
    datas.clear()

    for i in table.get_children():
        table.delete(i)

    # What kind of files can we import
    filetypes = (
        ('szöveges fájl', '*.txt'),
        ('Excel táblázat', ('*.xls', '*.xlsx')),
    )

    # The import method
    filename = filedialog.askopenfilename(
        title='Importálás',
        filetypes=filetypes
    )
    print(filename)
    if filename.endswith(('.xls', '.xlsx')):
        # If we import an excel file
        df = pandas.read_excel(filename)
        # print(df)
        temp = df.values.tolist()
        # print(temp)
        for index in temp:
            datas.append(index)


    else:
        # If we import a txt file
        file = open(filename, encoding="utf-8")
        for index in file:
            index = index.strip().split("\t")
            datas.append(index)

    # Upload the datas to the table
    for index in datas:
        table.insert(parent='', index='end', text='',
                     values=(index[0], index[1]))
    ws.update()


ws = Tk()
ws.title("Quizlet pdf generátor")
ws.geometry('800x800')

table = ttk.Treeview(ws)

table['columns'] = ('term', 'definition')

table.column("#0", width=0, stretch=NO)
table.column('term', width=200)
table.column('definition', width=250)

table.heading('term', text='Kifejezés')
table.heading('definition', text='Fogalom')

for word in datas:
    table.insert(parent='', index='end', text='',
                 values=(word[0], word[1]))

clearbutton = ttk.Button(
    ws,
    text='Importálás',
    command=importing
)

table.pack()
clearbutton.pack()
ws.mainloop()
