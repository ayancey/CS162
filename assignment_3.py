from tkinter import *
from tkinter.scrolledtext import *


class Window(Frame):
    def __init__(self, master=None):
        self.volume = 100
        self.status_box = None
        self.radio_elements = None
        self.mode = StringVar(None, "FM")
        self.frequency = IntVar()
        self.power = True

        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Helper method which adds the string to the status box
    def __update_status(self, text):
        self.status_box.insert(END, "{}\n".format(text))
        # scroll to bottom automatically
        self.status_box.see("end")

    def mode_change(self):
        self.__update_status("Mode changed to {}".format(self.mode.get()))

    def frequency_change(self, value):
        self.__update_status("Frequency changed to {}".format(value))

    # Gray out all the UI elements so the user knows the power is off
    def toggle_power(self):
        if self.power:
            self.power = False
            for element in self.radio_elements:
                element.configure(state=DISABLED)
        else:
            self.power = True
            for element in self.radio_elements:
                element.configure(state=NORMAL)

    def volume_up(self):
        if self.volume <= 90:
            self.volume += 10
            self.__update_status("Volume is now {}".format(self.volume))
        else:
            self.__update_status("Volume is at maximum")

    def volume_down(self):
        if self.volume >= 10:
            self.volume -= 10
            self.__update_status("Volume is now {}".format(self.volume))
        else:
            self.__update_status("Volume is at minimum")

    def init_window(self):
        self.master.title("Radio")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # Initialize widgets
        mode_label = Label(self, text="Mode")
        fm_button = Radiobutton(self, text="FM", variable=self.mode, value="FM", command=self.mode_change)
        am_button = Radiobutton(self, text="AM", variable=self.mode, value="AM", command=self.mode_change)
        aux_button = Radiobutton(self, text="AUX", variable=self.mode, value="AUX", command=self.mode_change)

        frequency_label = Label(self, text="Frequency")
        frequency_slider = Scale(self, from_=0, to=100, length=200, orient=HORIZONTAL, command=self.frequency_change)

        power = Button(self, text="Power", width=10, command=self.toggle_power)
        volume_up = Button(self, text="Volume Up", width=10, command=self.volume_up)
        volume_down = Button(self, text="Volume Down", width=10, command=self.volume_down)

        self.status_box = ScrolledText(self, height=6, width=62)

        self.radio_elements = [fm_button, am_button, aux_button, frequency_slider, volume_up, volume_down, self.status_box]

        # Place all widgets on frame
        mode_label.place(x=25, y=0)
        fm_button.place(x=25, y=30)
        am_button.place(x=25, y=60)
        aux_button.place(x=25, y=90)

        frequency_label.place(x=160, y=35)
        frequency_slider.place(x=160, y=60)

        power.place(x=440, y=0)
        volume_up.place(x=440, y=40)
        volume_down.place(x=440, y=80)

        self.status_box.place(x=0, y=150)


root = Tk()
root.resizable(False, False)
# size of the window
root.geometry("520x250")
app = Window(root)
root.mainloop()
