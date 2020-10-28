
import speedtest
from tkinter import *

root = Tk()
root.configure(background="black")
root.title("STest")
root.geometry("275x275")
root.iconbitmap("")

st = Label(root, text="(Do not touch anything after clicking the button!.?)", fg="blue", bg="yellow")
st.pack()

def check():
    try:
        starttest = Label(root, text="(Results of the  connection speed test.)", fg="red", bg="black")
        starttest.pack()
        servernames = []
        test = speedtest.Speedtest()
        down = test.download()
        up = test.upload()
        test.get_servers(servernames)
        rd = ('Download Speed: {:5.2f} Mb'.format(down/(1024*1024)))
        ru = ('Upload Speed: {:5.2f} Mb'.format(up/(1024*1024)))
        res_down = Label(root, text=rd, bg="black", fg="white")
        res_up = Label(root, text=ru,  bg="black", fg="white")
        res_ping = Label(root, text=f"ping: {test.results.ping} ms",  bg="black", fg="white")
        res_down.pack()
        res_up.pack()
        res_ping.pack()
    except:
        err = Label(root, text="Error while testing connection speed!", fg="black", bg="red")
        err.pack()

testBt = Button(root, text="Test Speed!", padx=40, pady=20, bg="black", fg="yellow", command=check)
testBt.pack()

if __name__ == "__main__":
    root.mainloop()
