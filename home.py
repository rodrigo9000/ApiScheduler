from tkinter import *
from tkinter import ttk

class Feedback:
    def __init__(self, master):
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        ### These lines will create the credential fields username, password, clientId and ClientScret
        self.entry_username = ttk.Entry(self.frame_header, width = 28)
        self.entry_username.insert(0, 'Username')   #Insert the string 'Username' into the Entry field

        self.entry_password = ttk.Entry(self.frame_header, width=28)
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
        check = PhotoImage(file=r'C:\Users\ghost\PycharmProjects\ApiScheduler\greencheck.gif').subsample(10, 10)

        def test(self):
            self.checkicon.config(image=check)

def main():
    # Tk constructor method
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__== "__main__": main()