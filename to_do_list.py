import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List by @SinhDang")

def add_task():
    task = entry_task.get()
    if task !="":
        Listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning", message="You Must Enter A Task.")

def delete_task():
    try:
        task_index = Listbox_tasks.curselection()[0]
        Listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You Must Select A Task.")

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        Listbox_tasks.delete(0, tkinter.END)
        for task in tasks: 
            Listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot Find Tasks.Dat.")

def save_tasks():
    tasks = Listbox_tasks.get(0, Listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

#Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

Listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
Listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

Listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=Listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text="Load Tasks", width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Save Tasks", width=48, command=save_tasks)
button_save_tasks.pack()

root.mainloop()