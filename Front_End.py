from tkinter import  *
import Back_End

def selected_item(event):
    global row_selected
    index = data_list.curselection()[0]
    row_selected = data_list.get(index)

    print(index)

    input_1.delete(0, END)
    input_2.delete(0, END)
    input_3.delete(0, END)
    input_4.delete(0, END)
    input_5.delete(0, END)
    input_6.delete(0, END)

    input_1.insert(END, row_selected[1])
    input_2.insert(END, row_selected[2])
    input_3.insert(END, row_selected[3])
    input_4.insert(END, row_selected[4])
    input_5.insert(END, row_selected[5])
    input_6.insert(END, row_selected[6])


def viewAll():
    data_list.delete(0, END)

    for item in Back_End.view():
        data_list.insert(END, item)

def searchAll():
    data_list.delete(0, END)

    for item in Back_End.search(date_input_1.get(), spendings_input_2.get(), exercise_input_3.get(), study_input_4.get(), meal_input_5.get(), games_input_6.get()):
        data_list.insert(END, item)

def delete_row():

    Back_End.delete(row_selected[0])

def addNew():

    Back_End.insert(date_input_1.get(), spendings_input_2.get(), exercise_input_3.get(), study_input_4.get(), meal_input_5.get(), games_input_6.get())

    data_list.delete(0,END)
    data_list.insert(END, (date_input_1.get(), spendings_input_2.get(), exercise_input_3.get(), study_input_4.get(), meal_input_5.get(), games_input_6.get()))

    input_1.delete(0, END)
    input_2.delete(0, END)
    input_3.delete(0, END)
    input_4.delete(0, END)
    input_5.delete(0, END)
    input_6.delete(0, END)

def update_row():
    print(exercise_input_3.get())
    print(spendings_input_2.get())
    Back_End.update(row_selected[0],date_input_1.get(), spendings_input_2.get(), exercise_input_3.get(), study_input_4.get(), meal_input_5.get(), games_input_6.get() )

    viewAll()
    
    input_1.delete(0, END)
    input_2.delete(0, END)
    input_3.delete(0, END)
    input_4.delete(0, END)
    input_5.delete(0, END)
    input_6.delete(0, END)
    input_6.delete(0, END)


win = Tk()

win.wm_title('Database_1')

l1 = Label(win, text = 'Date')
l1.grid(row = 0, column = 0)

l2 = Label(win, text = 'Spendings')
l2.grid(row = 0, column = 2)

l3 = Label(win, text = 'Exercise')
l3.grid(row = 1, column = 0)

l4 = Label(win, text = 'Study')
l4.grid(row = 1, column = 2)

l5 = Label(win, text = 'Meals')
l5.grid(row = 2, column = 0)

l6 = Label(win, text = 'Games')
l6.grid(row = 2, column = 2)

l7 = Label(win, text = '') #adds a space between the input and data_list view
l7.grid(row = 3, column = 0)

date_input_1 = StringVar() #date
input_1 = Entry(win, textvariable=date_input_1)
input_1.grid(row = 0, column = 1)

spendings_input_2 = StringVar() #spendings
input_2 = Entry(win, textvariable=spendings_input_2)
input_2.grid(row = 0, column = 3)

exercise_input_3 = StringVar() #exercise
input_3 = Entry(win, textvariable=exercise_input_3)
input_3.grid(row = 1, column = 1)

study_input_4 = StringVar() #study
input_4 = Entry(win, textvariable=study_input_4)
input_4.grid(row = 1, column = 3)

meal_input_5 = StringVar() #meal
input_5 = Entry(win, textvariable=meal_input_5)
input_5.grid(row = 2, column = 1)

games_input_6 = StringVar() #games
input_6 = Entry(win, textvariable=games_input_6)
input_6.grid(row = 2, column = 3)


data_list = Listbox(win, height = 8, width = 45)
data_list.grid(row = 4, column = 0, rowspan = 9, columnspan = 2)

scroll = Scrollbar(win)
scroll.grid(row = 4, column = 2, rowspan = 9)


data_list.bind('<<ListboxSelect>>', selected_item)

button_add = Button(win, text = 'Add', width = 12, command = addNew)
button_add.grid(row  = 4, column = 3)

button_search = Button(win, text = 'Search', width = 12, command  = searchAll)
button_search.grid(row  = 5, column = 3)

button_delete = Button(win, text = 'Delete', width = 12, command = delete_row)
button_delete.grid(row  = 6, column = 3)

button_viewAll = Button(win, text = 'View All', width = 12, command = viewAll)
button_viewAll.grid(row  = 7, column = 3)

button_exit = Button(win, text = 'Update', width = 12, command = update_row)
button_exit.grid(row  = 8, column = 3)

button_exit = Button(win, text = 'Exit', width = 12, command = win.destroy)
button_exit.grid(row  = 9, column = 3)


win.mainloop()