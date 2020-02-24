from tkinter import *
from socket import *

root = Tk()
root.title("CMS Messenger")

def sendMessage():
    c=b(e1.get())
    s.sendto(c,(n,5000))
def quitSession():
    s.close()

f=Frame(root)
f.pack()

l2=Label(f,text="Enter Username: ")
l3=Label(f,text="Enter IP ADDRESS: ")
l1=Label(f,text="Enter a Message: ")
e1=Entry(f)
e2=Entry(f,width=20)
e3=Entry(f,width=20)

n=e3.get()
s=socket(AF_INET,SOCK_STREAM)
s.connect((n,5000))
send=Button(f, text="Send", width=15, bd=5 , bg="white", command=sendMessage)

l2.grid(column=0, row=0, padx=10, pady=10)
l3.grid(column=0, row=1, padx=10, pady=10)
l1.grid(column=0, row=3, padx=10, pady=15)
e1.grid(column=1, row=3, padx=10, pady=15)
e2.grid(column=1, row=0, padx=10, pady=15)
e3.grid(column=1, row=1, padx=10, pady=15)
send.grid(column=1, row=4, padx=10, pady=15)


v = StringVar()
msg=Label(f,text="New Message: ",textvariable=v)
v.set(s.recvfrom(1024))
msg.grid(column=0, row=5, padx=10, pady=15)


Quit=Button(f, text="Quit", width=15, bd=5 , bg="white", command=quitSession)
Quit.grid(column=0, row=4, padx=10, pady=15)
