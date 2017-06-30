from tkinter import *
from tkinter import ttk

def bodyfunc(master):
         # Body Frame
        notebook = ttk.Notebook(master)
        notebook.pack(side=LEFT)
         
        bodyframeRelocate = ttk.Frame(notebook, relief=SUNKEN)
        bodyframeRelocate.pack()
         
        bodyframeScript = ttk.Frame(notebook, relief=SUNKEN)
        bodyframeScript.pack()
          
        notebook.add(bodyframeRelocate, text = 'Relocate')
        notebook.add(bodyframeScript, text = 'Script')
        ##############################################################
        # FROM label frame
        labelframeFrom = LabelFrame(bodyframeRelocate, text="From:")
        labelframeFrom.pack(side=LEFT, expand=True)
        # FROM treeview       
        treeviewFrom = ttk.Treeview(labelframeFrom)
        treeviewFrom.pack(side=LEFT, padx=5, pady=5)
         
        treeviewFrom.insert('', '0', 'item1', text = 'First Item')
        treeviewFrom.insert('item1', 'end', 'item11', text = ' Item 1.1')
        treeviewFrom.insert('', '1', 'item2', text = 'Second Item')
        ##############################################################
        # TO local frame
        labelframeTo = LabelFrame(bodyframeRelocate, text="To:")
        labelframeTo.pack(side=LEFT, expand=True)
        # TO treeview
        treeviewTo = ttk.Treeview(labelframeTo)
        treeviewTo.pack(side=LEFT, padx=5, pady=5)
