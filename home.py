from tkinter import *
from tkinter import ttk
import os
import urllib.request
import urllib.parse
import base64
from tkinter.ttk import Panedwindow, Notebook
import json
class Feedback:
    def __init__(self, master):

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        ### These lines will create the credential fields username, password, clientId and ClientScret
        self.entry_username = ttk.Entry(self.frame_header, width = 28)
        self.entry_username.insert(0, 'rodrigo2')   #Insert the string 'Username' into the Entry field

        self.entry_password = ttk.Entry(self.frame_header, width=28, show = '*')
        self.entry_password.insert(0, '1')

        self.entry_clientid = ttk.Entry(self.frame_header, width=28)
        self.entry_clientid.insert(0, '154a4c63dcd1431cb91d36667fe38efc')

        self.entry_clientsecret = ttk.Entry(self.frame_header, width=28)
        self.entry_clientsecret.insert(0, 'Z4MINpFgRu9vq51VSxCoDRgxY7xxjUtv')

        self.entry_username.pack(side=LEFT, padx=5, pady=5)
        self.entry_password.pack(side=LEFT, padx=5, pady=5)
        self.entry_clientid.pack(side=LEFT, padx=5, pady=5)
        self.entry_clientsecret.pack(side=LEFT, padx=5, pady=5)

        # Creates second frame to place URL field
        self.frame_header2 = ttk.Frame(master)
        self.frame_header2.pack()

        # URL Entry field is created a placed inside the second frame - just bellow name field
        self.entry_url = ttk.Entry(self.frame_header2, width=66)
        self.entry_url.insert(0, 'https://s001793.mobicontrolcloud.com/mobicontrol')
        self.entry_url.pack(side=LEFT, padx=5, pady=5)

        # Creates the Button 'Test'
        testButton = ttk.Button(self.frame_header, text='Test', command=lambda: test(self)).pack(side=LEFT, padx=5, pady=5)

        # Creates the image icons to be shown when Test button is pressed
        self.lightgrey = PhotoImage(file=(os.environ['USERPROFILE'] + '\git\ApiScheduler\\') + 'lightgrey.gif').subsample(10, 10) # Image icon to be used as place holder
        greencheck = PhotoImage(file=(os.environ['USERPROFILE'] + '\git\ApiScheduler\\') + 'greencheck.gif').subsample(10, 10)
        redcheck = PhotoImage(file=(os.environ['USERPROFILE'] + '\git\ApiScheduler\\') + 'redcheck.gif').subsample(10, 10)

        # Creates a Label to host green/check images as well as the initial place holder img
        self.checkicon = ttk.Label(self.frame_header)
        self.checkicon.config(image = self.lightgrey)
        self.checkicon.pack(side=RIGHT)
        
        # Separator widget
        ttk.Separator(master, orient = HORIZONTAL).pack(fill=BOTH, expand=True)
        
        # Body structure
        import body
        treeview_obj = body.bodyfunc(master)
          
        def test(self):
            # get the url and add the path at the end of the string to get the token
            url = (self.entry_url.get()).strip('\/') + '/api/token' #'https://s001793.mobicontrolcloud.com/mobicontrol/api/token'
            print(url)
            # generates the token following the format (ClientId:ClientSecret)
            token = (self.entry_clientid.get()).strip(' ').strip('\n') + ":" + (self.entry_clientsecret.get()).strip(' ').strip('\n')

            token = token.encode('utf-8') # turn the str into binary
            encoded = base64.b64encode(token)

            values = {'grant_type': 'password',
                      'username': (self.entry_username.get()).strip(' '),
                      'password': (self.entry_password.get()).strip(' ')}

            data = urllib.parse.urlencode(values)
            data = data.encode('ascii')
            req = urllib.request.Request(url, data)
            req.add_header('Authorization', ('Basic ' + encoded.decode('utf-8')))
            req.add_header('content-type', 'application/x-www-form-urlencoded')

            try:
                # Convert from bytes to text
                resp_text = urllib.request.urlopen(req).read().decode('UTF-8')
                # Use loads to decode from text
                json_obj = json.loads(resp_text)
                # Save access token to a variable                
                access_token = (json_obj["access_token"])                
                # change to Green icon
                self.checkicon.config(image=greencheck)
                # Call the function groupRequest passing the access token as parameter
                import body
                json_obj = body.groupRequest(self, access_token)
                body.loadtreeview(json_obj, treeview_obj)

            except urllib.error.HTTPError as e:
                print(e.code)
                self.checkicon.config(image=redcheck)


def main():
    # Tk constructor method
    root = Tk()
    # root.geometry('1024x350+500+300')
    feedback = Feedback(root)
    root.mainloop()

if __name__== "__main__": main()