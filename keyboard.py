#!/usr/bin/env python
'''A simple keyboard that you can add new keys onto, and then press and release those keys.

Christian Howard : CS162 @ 14:00,MWF
Assignment 1

For Assignment 2 : 
    If you use this, feel free to send me a link to what you did, or another copy. 
    My Email : christian.howard.6298@mail.linnbenton.edu

Design:
    We can imagine a blank board or surface.
    We then put button-like objects, keys, onto it somewhere.
    Then we can press and release those keys.

    Create a keyboard class, which will contain all of our keys.
    Create another class, which will be our keys.
    Set up basic functions on they key class to operate the key like a button. (Press and Release)
    Set up functions on the keyboard class to operate the keys. 
        Make sure keys exist, and follow any obvious rules(can't release a button if it's not pressed).

Testing:
    Inputing the the following commands should give the following results...
        > add red_button
        red_button has been added
        > press red_button
        red_button has been pressed
        > press blue_button
        blue_button does not exist 
        > release red_button
        red_button has been released
        > release red_button
        red_button can't be released because it's not being pressed
'''

class Keyboard:
    '''A container for keys.'''
    NO_KEY_MSG = 'The key, {name}, does not exist on this keyboard!'

    def __init__(self):
        self.keys = {}

    def __str__(self):
        return (
            'Keyboard\n' + 
            ''.join([f'    [{name}] is {key.str_pressed}\n' for name,key in self.keys.items()])
        )

    def add_key(self, key_name:str):
        '''Adds a key to this keyboard.

        :param key_name: the name to give the new key
        '''
        self.keys[key_name] = Key(key_name)
        print(f'{key_name} has been added to the keyboard!')

    def remove_key(self, key_name:str):
        '''Removes a key from this keyboard.

        :param key_name: the name of the key to remove
        '''
        try:
            del self.keys[key_name]
            print(f'{key_name} has been removed from the keyboard!')
        except KeyError:
            print(Keyboard.NO_KEY_MSG.format(name=key_name))

    def press_key(self, key_name:str):
        '''Presses a key down.

        :param key_name: the name of the key to press
        '''
        try:
            self.keys[key_name].press()
        except KeyError:
            print(Keyboard.NO_KEY_MSG.format(name=key_name))

    def release_key(self, key_name:str):
        '''Releases a key, only if that key is also pressed.

        :param key_name: the name of the key to release
        '''
        try:
            key = self.keys[key_name]

            if key.is_pressed:
                key.release()
            else:
                print('This key can\'t be released because it\'s not being pressed!')
        except KeyError:
            print(Keyboard.NO_KEY_MSG.format(name=key_name))

class Key: 
    '''A button-like object that can be pressed and released.'''
    def __init__(self, name:str):
        '''
        :param name: the name to give the key
        '''
        self.name = name 
        self.is_pressed = False 

    @property
    def str_pressed(self):
        '''A text saying if this key is pressed or not pressed.'''
        return 'pressed' if self.is_pressed else 'not pressed'

    def press(self):
        '''Presses the key down.'''
        self.is_pressed = True 
        print(f'{self.name} has been pressed!')

    def release(self):
        '''Releases the key. (Doesn't care if pressed.)'''
        self.is_pressed = False 
        print(f'{self.name} has been released!')


if __name__ == '__main__':
    HELP_STR = (
        f'Commands:\n'
        f'  > quit\n        Exit the program.'
        f'  > help\n        Displays this message.\n'
        f'  > add [key-name]\n        Adds a key with this name to the keyboard. (Names shouldn\'t contain spaces!)\n'
        f'  > press [key-name]\n      Presses this key down.\n'
        f'  > release [key-name]\n        Releases this key, only if it\'s been pressed.\n'
        f'  > showall\n       Lists all the keys on this keyboard.\n'
        f'  > reset\n       Give yourself a new keyboard.'
    )

    print(
        f'Assemble your keyboard! When you see a > symbol, that means you can enter a command.\n'
        f'To start, you can try using the command: help'
    )

    keyboard = Keyboard()

    while True:
        cmd = input('> ')
        cmd_list = cmd.split() 

        if cmd_list[0] == 'quit':
            print('Destroying keyboard...\nGoodbye!')
            break 
        elif cmd_list[0] == 'help':
            print(HELP_STR)
        # Added a check for len, since not giving the keyname would crash the program.
        elif len(cmd_list) > 1 and cmd_list[0] == 'add':
            keyboard.add_key(cmd_list[1])
        elif len(cmd_list) > 1 and cmd_list[0] == 'remove':
            keyboard.remove_key(cmd_list[1])
        elif len(cmd_list) > 1 and cmd_list[0] == 'press':
            keyboard.press_key(cmd_list[1])
        elif len(cmd_list) > 1 and cmd_list[0] == 'release':
            keyboard.release_key(cmd_list[1])
        elif cmd_list[0] == 'showall':
            print(keyboard)
        elif cmd_list[0] == 'reset':
            keyboard = Keyboard()
            print('You now have a new keyboard!')