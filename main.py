import tkinter.filedialog
from tkinter import *
from tkinter import ttk, filedialog
import pandas
from fpdf import FPDF

file = None
pdftypes = ['táblázat', 'szójegyzék', 'kicsi', 'közepes', 'nagy']
datas = []


def mainconrtol():
    """
    This
    """
    if len(datas) == 0:
        flipbutton['state'] = DISABLED
    else:
        flipbutton['state'] = NORMAL

    if exporttitle.get() not in ["", " "] and len(datas) != 0:
        exportbutton['state'] = NORMAL
    else:
        exportbutton['state'] = DISABLED

    ws.after(100, mainconrtol)


def importing():
    '''
    Here we are importing the words from txt and excel (xls and xlsx) files.
    This will run when the user press import button
    '''
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


def flip():
    '''
    Here we flip the rows of the table
    '''
    # Flip the datas
    temp = []
    for word in datas:
        temp.append([word[1], word[0]])

    # Clear the table and upload the new datas
    for i in table.get_children():
        table.delete(i)

    for index in temp:
        table.insert(parent='', index='end', text='',
                     values=(index[0], index[1]))

    ws.update()

    datas.clear()
    for i in temp:
        datas.append(i)


def normalexport():
    """
    Here we make a pdf table from datas when the user press export button.
    """

    class PDF(FPDF):
        def __init__(self, **kwargs):
            super(PDF, self).__init__(**kwargs)
            self.add_font('LiberationSans', '', 'fonts/LiberationSans-BaDn.ttf', uni=True)
            self.add_font('LiberationSans', 'B', 'fonts/LiberationSansBold-1adM.ttf', uni=True)

        def header(self):
            self.set_font('LiberationSans', 'B', 16)
            self.cell(0, 5, f'{exporttitle.get()}', ln=1)
            self.set_font('LiberationSans', size=12)
            self.cell(0, 10, 'Készült Quizlet pdf export by Török Bence', ln=1)

        '''def footer(self):
            self.set_y(-15)
            self.set_font('helvetica', '', size=8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 10, f'{self.page_no()}/{{nb}}', align='C')'''

    # print(datas)

    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=True)

    pdf.add_page()
    # pdf.cell(0, 10, 'árvíztűrő tükörfúrógép ÁRVÍZTŰRŐ TÜKÖRFÚRÓGÉP', ln=1)
    with pdf.table(
            first_row_as_headings=False,
            col_widths=(8, 32, 60),
            line_height=4 * pdf.font_size,
            borders_layout='HORIZONTAL_LINES') as pdftable:
        for data_row in datas:
            row = pdftable.row()
            pdf.set_font('LiberationSans', 'B', size=16)
            row.cell(f'{datas.index(data_row) + 1}.')
            pdf.set_font('LiberationSans', '', size=16)
            for datum in data_row:
                row.cell(datum)
    exportfilename = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[('PDF fájl', '*.pdf')]
    )

    # print(exportfilename)
    pdf.output(exportfilename)


'''
Create the window, the frame of table, and declarate exportwindows place
'''
ws = Tk()
ws.title("Quizlet pdf generátor")
ws.geometry('800x600')

tableframe = Frame(ws)



'''
Create the table and declarate the parameters of it
'''
table = ttk.Treeview(tableframe)

table['columns'] = ('term', 'definition')

table.column("#0", width=0, stretch=NO)
table.column('term', width=300)
table.column('definition', width=450)

table.heading('term', text='Kifejezés')
table.heading('definition', text='Fogalom')

# This make an empty table
for word in datas:
    table.insert(parent='', index='end', text='',
                 values=(word[0], word[1]))

table.grid(row=0, column=0, columnspan=8, sticky='E', pady=10)
'''
Create the scrollbar of table
'''
tablesb = Scrollbar(tableframe, orient=VERTICAL)
tablesb.grid(row=0, column=9, rowspan=10, pady=2)

'''
Connect the table and the scrollbar
'''
table.config(yscrollcommand=tablesb.set)
tablesb.config(command=table.yview)


'''
Create the import button
'''
clearbutton = ttk.Button(
    ws,
    text='Importálás',
    command=importing
)


'''
Create the flip button
'''
flipbutton = ttk.Button(
    ws,
    text='Felcserélés',
    command=flip
)


'''
Create exportbutton
'''
exportbutton = ttk.Button(
    ws,
    text='Exportálás',
    command=normalexport
)


'''
Create pdf type selector combobox
'''
pdftype = ttk.Combobox(ws, values=pdftypes, state='readonly', width=48)


'''
Create title entry
'''
exporttitle = Entry(ws, width=50)


'''
Create the labels
'''
titlelabel = Label(ws, text='Cím:')
typelabel = Label(ws, text='Típus:')


'''
The grid
'''
titlelabel.grid(row=0, column=0, sticky='w', pady=2)
typelabel.grid(row=1, column=0, sticky='w', pady=2)
pdftype.grid(row=1, column=1, sticky="w", pady=2)
exporttitle.grid(row=0, column=1, sticky='w', pady=2)
clearbutton.grid(row=0, column=2, sticky='E', pady=5, padx=10)
flipbutton.grid(row=1, column=2, sticky='E', pady=5, padx=10)
exportbutton.grid(row=2, column=2, sticky='E', pady=5, padx=10)
tableframe.grid(row=5, column=0, columnspan=10, rowspan=10, sticky='E', pady=10)


'''
Add the elements to the window
and loop the window
'''


ws.after(10, mainconrtol)
ws.mainloop()
