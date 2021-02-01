from tkinter import Tk, Menu, Frame, Button, Label, Radiobutton, Entry
from tkinter import ttk, IntVar, StringVar, Scrollbar

# ================estilos=========================
config = [('arial', 16), ('verdana', 13)]
colors = ('#5F9EA0', '#4682B4', '#B0C4DE', '#B0E0E6', '#ADD8E6', '#87CEEB')
# ('#DCDCDC', '#D3D3D3','#C0C0C0','#A9A9A9' )

# ===================root=============================
root = Tk()
root.title('contacto list')
width = 800
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(False, False)

# =========================tags==========================
tab_control = ttk.Notebook(root)
tab_look = ttk.Frame(tab_control)
tab_control.add(tab_look, text='Lista')
tab_edit = ttk.Frame(tab_control)
tab_control.add(tab_edit, text='Editar')
tab_control.pack(expand=1, fill='both')

# =========================frames==========================
frame_buttons = Frame(tab_edit)
frame_buttons.config(width=200, height=400, bg=colors[1], bd=25)
frame_buttons.pack(side='left', padx=25, pady=25,
                   expand=1, fill='both')

frame_form = Frame(tab_edit)
frame_form.config(width=700, height=500, bd=1, bg=colors[1])
frame_form.pack(side='right', padx=25, pady=25,
                expand=1, fill='both')


# ========================botones========================
btn_add = Button(frame_buttons)
btn_add.config(text='añadir', bg=colors[4], font=config[1], borderwidth=0)
btn_add.pack(padx=10, pady=25)

btn_delete = Button(frame_buttons)
btn_delete.config(text='Eliminar', bg=colors[4], font=config[1], borderwidth=0)
btn_delete.pack(padx=10, pady=25)

btn_update = Button(frame_buttons)
btn_update.config(text='actualizar',
                  bg=colors[4], font=config[1], borderwidth=0)
btn_update.pack(padx=10, pady=25)

btn_read = Button(frame_buttons)
btn_read.config(text='leer', bg=colors[4], font=config[1], borderwidth=0)
btn_read.pack(padx=10, pady=25)


# ========================formulario========================
# ========================lista desplegable=================
number = StringVar()
select_number = ttk.Combobox(frame_form,
                             width=3, textvariable=number, state='r',
                             font=config[1])
select_number['values'] = [1, 2, 3, 4, 5, 6]  # actualizarlo
select_number.grid(row=0, column=1, sticky='w')
# select_number.current(0)
select_number.focus()


# ========================labels========================
lbl_id = Label(frame_form)
lbl_id.config(text='Id', font=config[0], bg=colors[1])
lbl_id.grid(row=0, column=0, pady=15, padx=10, sticky='w')

lbl_name = Label(frame_form)
lbl_name.config(text='nombre', font=config[0], bg=colors[1])
lbl_name.grid(row=1, column=0, pady=15, padx=10, sticky='w')

lbl_lname = Label(frame_form)
lbl_lname.config(text='apellido', font=config[0], bg=colors[1])
lbl_lname.grid(row=2, column=0, pady=15, padx=10, sticky='w')

lbl_contacto = Label(frame_form)
lbl_contacto.config(text='contacto', font=config[0], bg=colors[1])
lbl_contacto.grid(row=3, column=0, pady=15, padx=10, sticky='w')

lbl_email = Label(frame_form)
lbl_email.config(text='correo', font=config[0], bg=colors[1])
lbl_email.grid(row=4, column=0, pady=15, padx=10, sticky='w')

lbl_Dirección = Label(frame_form)
lbl_Dirección.config(text='dirección', font=config[0], bg=colors[1])
lbl_Dirección.grid(row=5, column=0, pady=15, padx=10, sticky='w')

lbl_genre = Label(frame_form)
lbl_genre.config(text='genero', font=config[0], bg=colors[1])
lbl_genre.grid(row=6, column=0, pady=15, padx=10, sticky='w')

# ========================checkbuttons========================
var_man = IntVar()
chb_man = Radiobutton(frame_form)
chb_man.config(
    text='Hombre', font=config[0], bg=colors[1],
    variable=var_man, value=1)
chb_man.grid(row=6, column=1)

var_woman = IntVar()
chb_woman = Radiobutton(frame_form)
chb_woman.config(
    text='mujer', font=config[0], bg=colors[1],
    variable=var_woman, value=2)
chb_woman.grid(row=6, column=3)

# ========================Entrys========================
en_name = Entry(frame_form)
en_name.config(width=30, font=config[1], bg=colors[4], borderwidth=0)
en_name.grid(row=1, column=1, columnspan=4)

en_lname = Entry(frame_form)
en_lname.config(width=30, font=config[1], bg=colors[4], borderwidth=0)
en_lname.grid(row=2, column=1, columnspan=4)

en_contacto = Entry(frame_form)
en_contacto.config(width=30, font=config[1], bg=colors[4], borderwidth=0)
en_contacto.grid(row=3, column=1, columnspan=4)

en_email = Entry(frame_form)
en_email.config(width=30, font=config[1], bg=colors[4], borderwidth=0)
en_email.grid(row=4, column=1, columnspan=4)

en_direccion = Entry(frame_form)
en_direccion.config(width=30, font=config[1], bg=colors[4], borderwidth=0)
en_direccion.grid(row=5, column=1, columnspan=4)

# ==============================================================================
frame_table = Frame(tab_look)
frame_table.config(bg=colors[1], pady=10, padx=10)
frame_table.pack(expand=1, fill='both')

# =================================tables=====================================
scrollbarx = Scrollbar(frame_table, orient='horizontal')
scrollbary = Scrollbar(frame_table, orient='vertical')
scrollbary.pack(side="right", fill="y")
scrollbarx.pack(side='bottom', expand=True, fill='x')
tree = ttk.Treeview(frame_table)
tree.config(
    columns=("Id", "Nombre", "Apellido", "Genero", "Dirección", "Contacto"), height=500, selectmode="extended", padding=15,
    yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
tree.heading('Id', text="Id")
tree.heading('Nombre', text="Nombre")
tree.heading('Apellido', text="Apellido")
tree.heading('Genero', text="Genero")
tree.heading('Dirección', text="Dirección")
tree.heading('Contacto', text="Contacto")
tree.column('#0', stretch=False, minwidth=0, width=0)
tree.column('#1', stretch=False, minwidth=30, width=30)
tree.column('#2', stretch=False, minwidth=200, width=200)
tree.column('#3', stretch=False, minwidth=180, width=180)
tree.column('#4', stretch=False, minwidth=70, width=70)
tree.column('#5', stretch=False, minwidth=150, width=150)
tree.column('#6', stretch=False, minwidth=150, width=150)
tree.pack(ipadx=10, ipady=10, expand=1, fill='x')

contacto1 = tree.insert("", 1,
                        values=("23", "Luis Daniel", "Tisoy Tandioy", 'male', 'av caracas #2-77', '3207156743'))

contacto2 = tree.insert("", 2,
                        values=("2", "Waira Shabima Rocio De Los Angeles", "Tisoy Tandioy", 'Female', 'av caracas #2-77', '3206675807'))

if __name__ == "__main__":
    root.mainloop()
