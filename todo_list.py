import tkinter
import tkinter.messagebox
import pickle

root=tkinter.Tk()
root.title("To-Do list")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_task.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Enter a task.")

def delete_task():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")
def load_tasks():
    try:
        tasks = pickle.load(open("task.dat", "rb"))
        listbox_task.delete(0, tkinter.END)
        for task in tasks:
            listbox_task.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat")

def save_tasks():
    tasks = listbox_task.get(0, listbox_task.size())
    pickle.dump(tasks, open("task.dat", "wb"))

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_task = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_task.pack(side = tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_task.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_task.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_load_task = tkinter.Button(root, text="Load Task", width=48, command=load_tasks)
button_load_task.pack()

button_save_task = tkinter.Button(root, text="Save Task", width=48, command=save_tasks)
button_save_task.pack()

root.mainloop()