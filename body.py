from tkinter import *
from tkinter import ttk

def bodyfunc(master):
    
    # Body Frame
    notebook = ttk.Notebook(master)
    notebook.pack(side=LEFT)
     
    bodyframeRelocate = ttk.Frame(notebook, width=600, height=400, relief=SUNKEN)
    bodyframeRelocate.pack()
     
    bodyframeScript = ttk.Frame(notebook, width=400, height=400, relief=SUNKEN)
    bodyframeScript.pack()
      
    notebook.add(bodyframeRelocate, text = 'Relocate')
    notebook.add(bodyframeScript, text = 'Script')
    
    # Label Frame
    labelframeFrom = LabelFrame(bodyframeRelocate, text="From:")
    labelframeFrom.pack(expand=True)
    # TreeView          
    treeview = ttk.Treeview(labelframeFrom)
    treeview.pack()
     
    treeview.insert('', '0', 'item1', text = 'First Item')
    treeview.insert('item1', 'end', 'item11', text = ' Item 1.1')
    treeview.insert('', '1', 'item2', text = 'Second Item')