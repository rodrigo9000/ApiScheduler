from tkinter import *
from tkinter import ttk
import json
import urllib.request
import urllib.parse
def groupRequest(self, access_token):
            
            groupurl = 'https://s001793.mobicontrolcloud.com:443/mobicontrol/api/devicegroups'
            req = urllib.request.Request(groupurl)
            req.add_header('Accept', 'application/json')
            req.add_header('Authorization', ('Bearer ' + access_token))
    
            response = urllib.request.urlopen(req).read().decode('UTF-8')
            json_obj = json.loads(response)
            # Filter only Regular groups
            json_obj = [obj for obj in json_obj if(obj['Kind'] == 'Regular')]
            return json_obj                   

def loadtreeview(json_obj, treeview_obj):
    # Loop through each list item 
    for num, item in enumerate(json_obj):
        pathRoot = ((json_obj[1]["Path"]).split('\\')[2])
        # Loop through the two treeview objects - From and To
        for obj in (treeview_obj):
            obj.insert('',num, (item["Name"]), text = (item["Name"]))
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
         
#             treeviewFrom.insert('', '0', 'item1', text = 'First Item')
#             treeviewFrom.insert('item1', 'end', 'item11', text = ' Item 1.1')
#             treeviewFrom.insert('', '1', 'item2', text = 'Second Item')
        ##############################################################
        # TO local frame
        labelframeTo = LabelFrame(bodyframeRelocate, text="To:")
        labelframeTo.pack(side=LEFT, expand=True)
        # TO treeview
        treeviewTo = ttk.Treeview(labelframeTo)
        treeviewTo.pack(side=LEFT, padx=5, pady=5)
        
        return(treeviewFrom, treeviewTo)