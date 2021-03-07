import speedtest
from tkinter import *
from tkinter import ttk
import threading


root = Tk()  # Calling the Tkinter module.
root.configure(background="black")  # Configure the background as black.
root.title("SpeedTester")  # Set the Title of the program.
root.geometry("275x275")  # Sets the resolution to (275x275)
root.resizable(False, False)  # Set resize to false

dev = Label(root, text="Developer : reisgoldmanX", fg="red", bg="black")
dev.place(relx=1.0, rely=1.0, anchor='se')
bar = ttk.Progressbar(root, orient=HORIZONTAL, length=150, mode="determinate")  # Set progress bar
start_test = Label(root, text="(Results of the  connection speed test.)", fg="green", bg="black")


def check():
    try:
        servernames = []
        bar["value"] -= bar["value"]
        test = speedtest.Speedtest()
        bar.pack()
        bar["value"] += 20
        down = test.download() / (1024 * 1024)
        bar["value"] += 30
        up = test.upload() / (1024 * 1024)
        bar["value"] += 30
        test.get_servers(servernames)
        bar["value"] += 10
        ping = test.results.ping
        bar["value"] += 10
        start_test.pack()
        test_done = "Download Speed: {:5.2f} Mb\nUpload Speed: {:5.2f} Mb\nPing: {} ms".format(down, up, ping)
        var.set(test_done)
        all1.pack()
    except:
        print("hata")


def threadButtonOne():
    try:
        threading.Thread(target=check).start()
    except:
        threading.Thread(target=check).start()


testBt = Button(root, text="Test Speed!", padx=40, pady=20, bg="black", fg="yellow", command=threadButtonOne)
testBt.pack()  # Sets the button
var = StringVar()
var.set("Click the button...")
all1 = Label(root, textvariable=var, bg="black", fg="white", font=("Courier", 12))  # Printing results to screen.

root.mainloop()
