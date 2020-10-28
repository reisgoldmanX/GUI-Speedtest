import speedtest
from tkinter import *

root = Tk()  # Calling the Tkinter module.
root.configure(background="black")  # Configure the background as black.
root.title("STest")  # Set the Title of the program.
root.geometry("275x275")  # Sets the resolution to (275x275)

st = Label(root, text="(Do not touch anything after clicking the button!.?)", fg="blue", bg="yellow")
st.pack()  # The warning on the GUİ.


def check():
    try:
        starttest = Label(root, text="(Results of the  connection speed test.)", fg="red", bg="black")
        starttest.pack()
        servernames = []
        test = speedtest.Speedtest()
        down = test.download()
        up = test.upload()
        test.get_servers(servernames)
        rd = ('Download Speed: {:5.2f} Mb'.format(down / (1024 * 1024)))  # Converts bits to megabytes.
        ru = ('Upload Speed: {:5.2f} Mb'.format(up / (1024 * 1024)))  # Converts bits to megabytes.
        res_down = Label(root, text=rd, bg="black", fg="white")  # Printing results to screen.
        res_up = Label(root, text=ru, bg="black", fg="white")  # Printing results to screen.
        res_ping = Label(root, text=f"ping: {test.results.ping} ms", bg="black", fg="white")
        res_down.pack()
        res_up.pack()
        res_ping.pack()
    except:
        err = Label(root, text="Error while testing connection speed!", fg="black", bg="red")
        err.pack()  # Sets the exception error


testBt = Button(root, text="Test Speed!", padx=40, pady=20, bg="black", fg="yellow", command=check)
testBt.pack()  # Sets the button

if __name__ == "__main__":
    root.mainloop()
