from tkinter import *
from socket import *

root = Tk()
root.title("CMS Messenger")

f=Frame(root)
f.pack()

l1=Label(f,text="Enter a Message: ")
l2=Label(f,text="Enter Username: ")
e1=Entry(f)
e2=Entry(f,width=20)

s=socket(AF_INET,SOCK_DGRAM)
s.bind("127.0.0.1",5000)
send=Button(f, text="Send", width=15, bd=5 , bg="white", command=sendMessage)

v = StringVar()
v.set(s.recvfrom(1024))
msg=Label(f,text="New Message: ",textvariable=v)


l2.grid(column=0, row=0, padx=10, pady=10)
e2.grid(column=1, row=0, padx=10, pady=15)
l1.grid(column=0, row=2, padx=10, pady=15)
e1.grid(column=1, row=2, padx=10, pady=15)
send.grid(column=1, row=3, padx=10, pady=15)
msg.grid(column=0, row=4, padx=10, pady=15)

