from tkinter import *
from tkinter import ttk

def bodyfunc(master):
<<<<<<< HEAD
    
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
=======
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
>>>>>>> c422ec9f63aa543574566c12fed60203056ae5e1
