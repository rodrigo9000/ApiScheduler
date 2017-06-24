from tkinter import *
from tkinter import ttk

import urllib.request
import urllib.parse
import base64

class Feedback:
    def __init__(self, master):

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        ### These lines will create the credential fields username, password, clientId and ClientScret
        self.entry_username = ttk.Entry(self.frame_header, width = 28)
        self.entry_username.insert(0, 'Username')   #Insert the string 'Username' into the Entry field

        self.entry_password = ttk.Entry(self.frame_header, width=28, show = '*')
        self.entry_password.insert(0, 'Password')

        self.entry_clientid = ttk.Entry(self.frame_header, width=28)
        self.entry_clientid.insert(0, 'ClientId')

        self.entry_clientsecret = ttk.Entry(self.frame_header, width=28)
        self.entry_clientsecret.insert(0, 'ClientSecret')

        self.entry_username.pack(side=LEFT, padx=5, pady=5)
        self.entry_password.pack(side=LEFT, padx=5, pady=5)
        self.entry_clientid.pack(side=LEFT, padx=5, pady=5)
        self.entry_clientsecret.pack(side=LEFT, padx=5, pady=5)

        # Creates the Button 'Test'
        testButton = ttk.Button(self.frame_header, text='Test', command=lambda: test(self)).pack(side=LEFT, padx=5, pady=5)

        # Creates the Check icon when the test button is pushed
        self.checkicon = ttk.Label(self.frame_header)
        self.checkicon.pack(side=RIGHT)
        greencheck = PhotoImage(file=r'C:\Users\ghost\PycharmProjects\ApiScheduler\greencheck.gif').subsample(10, 10)
        redcheck = PhotoImage(file=r'C:\Users\ghost\PycharmProjects\ApiScheduler\redcheck.gif').subsample(10, 10)

        def test(self):
            url = 'https://s001793.mobicontrolcloud.com/mobicontrol/api/token'

            token = (self.entry_clientid.get()).strip(' ') + ":" + (self.entry_clientsecret.get()).strip(' ')
            token = token.encode('utf-8')
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
                response = urllib.request.urlopen(req)
                self.checkicon.config(image=greencheck)
            except urllib.error.HTTPError as e:
                print(e.code)
                self.checkicon.config(image=redcheck)


def main():
    # Tk constructor method
    root = Tk()
    root.geometry('1024x350+500+300')
    feedback = Feedback(root)
    root.mainloop()

if __name__== "__main__": main()