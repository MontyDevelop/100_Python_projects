from tkinter import *
import speedtest


def checkspeed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download = str(round(st.download() / 10**6, 2)) + " Mbps"
    upload = str(round(st.upload() / 10**6, 2)) + " Mbps"

    download_speed.config(text=download)
    upload_speed.config(text=upload)


screen = Tk()
screen.geometry("400x220")
screen.title("Internet Speed Test")
screen.config(bg="black", padx=20, pady=20)

FONT = ("Arial", 14, "bold")

Label(screen, text="Download Speed:", fg="red", bg="black", font=FONT).grid(row=0, column=0)
download_speed = Label(screen, text="00", fg="white", bg="black", font=FONT)
download_speed.grid(row=0, column=1)

Label(screen, text="Upload Speed:", fg="green", bg="black", font=FONT).grid(row=1, column=0)
upload_speed = Label(screen, text="00", fg="white", bg="black", font=FONT)
upload_speed.grid(row=1, column=1)

Button(
    screen,
    text="Check Speed",
    bg="blue",
    fg="white",
    font=FONT,
    command=checkspeed
).grid(row=2, column=0, columnspan=2, pady=20)

screen.mainloop()
