# Testing ideas
# 1. Ensure mode selection works as intended, cycles through all modes
# 2. Check that muting and unmuting works as intended
# 3. User should be unable to set volume below 0% or over 100%


class Radio(object):
    default_modes = ["FM", "AM", "CD", "AUX"]

    # Initial volume is set to 20%, initial mode is set to FM
    def __init__(self):
        self.volume = 20
        self.saved_volume = self.volume
        self.modes = list(self.default_modes)
        self.current_mode = self.modes.pop()

    # Cycle through modes
    def change_mode(self):
        if len(self.modes) == 0:
            # reload modes when list is empty
            self.modes = list(self.default_modes)

        self.current_mode = self.modes.pop()

    # Increase the volume by 10% if not already at max volume
    def increase_volume(self):
        if self.volume <= 90:
            self.volume += 10

    # Decrease the volume by 10% if not already at min volume
    def decrease_volume(self):
        if self.volume >= 10:
            self.volume -= 10

    # Muting sets the volume to 0%, and saves the volume separately so it can be restored
    def toggle_mute(self):
        if self.volume > 0:
            self.saved_volume = self.volume
            self.volume = 0
        else:
            self.volume = self.saved_volume


# If module is run directly, show demo
if __name__ == "__main__":
    my_radio = Radio()

    while True:
        print("Volume: {}% | {}".format(my_radio.volume, my_radio.current_mode))
        print("1. Change mode\n2. Increase volume\n3. Decrease volume\n4. Mute/unmute\n0. Exit")

        option = input("Select option: ").strip()

        if option == "1":
            my_radio.change_mode()
        elif option == "2":
            my_radio.increase_volume()
        elif option == "3":
            my_radio.decrease_volume()
        elif option == "4":
            my_radio.toggle_mute()
        elif option == "0":
            break
        else:
            print("Invalid option")
