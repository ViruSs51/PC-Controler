import socket
from time import time

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button
from kivy.uix.label import Label

with open('IPv4.txt', 'r') as file: ip = file.read()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, 9999))
data = client.recv(1024)
information = data.decode('utf-8').split(',')

class Mouse(BoxLayout):
    mouse_position = [10, 10]
    start_move_position = [0, 0]
    sinsivity = 15
    click_information = {
        'clicks': 0,
        'time': 0
        }
    
    def on_touch_down(self, touch):
        self.start_move_position = [touch.x, touch.y]

        self.click_information['clicks'] += 1
        if self.click_information['clicks'] == 1:
            self.click_information['time'] = time()

        elif time() > self.click_information['time'] + 0.1:
            self.click_information['clicks'] = 0
        
        elif self.click_information['clicks'] == 2:
            client.send('$!obj!$mouse$!action!$click$!parm!$left'.encode('utf-8'))
            
        elif self.click_information['clicks'] >= 3:
            client.send('$!obj!$mouse$!action!$click$!parm!$right'.encode('utf-8'))

        with self.canvas:
            Color(0, 1, 0, .4)
            d = 15
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))

            Color(1, 0, 0, .4)
            touch.ud['traictory'] = Line(points=(touch.x, touch.y))
    
    def on_touch_move(self, touch):
        if touch.x >= self.start_move_position[0] + 5 and self.mouse_position[0] <= int(information[0]) - self.sinsivity:
            self.mouse_position[0] += self.sinsivity
            self.start_move_position[0] = touch.x
            
        elif touch.x <= self.start_move_position[0] - 5 and self.mouse_position[0] >= self.sinsivity:
            self.mouse_position[0] -= self.sinsivity
            self.start_move_position[0] = touch.x

        if touch.y <= self.start_move_position[1] - 5 and self.mouse_position[1] <= int(information[1]) - self.sinsivity:
            self.mouse_position[1] += self.sinsivity
            self.start_move_position[1] = touch.y
            
        elif touch.y >= self.start_move_position[1] + 5 and self.mouse_position[1] >= self.sinsivity:
            self.mouse_position[1] -= self.sinsivity
            self.start_move_position[1] = touch.y
        
        client.send(f'$!obj!$mouse$!action!$move$!parm!${self.mouse_position[0]}$!separator!${self.mouse_position[1]}'.encode('utf-8'))
        touch.ud['traictory'].points += [touch.x, touch.y]

class Keyboard(BoxLayout):
    keys = {
        '1': {
            'esc': ('esc', 1.1),
            '!1': 1,
            'F1': ('f1', 1.1),
            'F2': ('f2', 1.1),
            'F3': ('f3', 1.1),
            'F4': ('f4', 1.1),
            '!2': .55,
            'F5': ('f5', 1.1),
            'F6': ('f6', 1.1),
            'F7': ('f7', 1.1),
            'F8': ('f8', 1.1),
            '!3': .55,
            'F9': ('f9', 1.1),
            'F10': ('f10', 1.1),
            'F11': ('f11', 1.1),
            'F12': ('f12', 1.1),
            '!4': .2,
            'Power': ('power', 1.1),
            'Sleep': ('sleep', 1.1),
            'Wake\nUp': ('wakeup', 1.1),
            '!5': 4.6
        },
        '2': {
            '`': ('~', 1.1),
            '1': ('1', 1.1),
            '2': ('2', 1.1),
            '3': ('3', 1.1),
            '4': ('4', 1.1),
            '5': ('5', 1.1),
            '6': ('6', 1.1),
            '7': ('7', 1.1),
            '8': ('8', 1.1),
            '9': ('9', 1.1),
            '0': ('0', 1.1),
            '_': ('_', 1.1),
            '=': ('=', 1.1),
            '<---': ('backspace', 2.2),
            '!1': .25,
            'Print\nScreen\nSysRq': ('printscreen', 1.1),
            'Scroll\nlock': ('scrolllock', 1.1),
            'Pause\nBreak': ('pausebreak', 1.1),
            '!2': .25,
            'Num\nLock': ('numlock', 1.1),
            '/': ('/', 1.1),
            '*': ('*', 1.1),
            '-': ('-', 1.1),
        },
        '3': {
            'Tab': ('tab', 1.3),
            'Q': ('q', 1.1),
            'W': ('w', 1.1),
            'E': ('e', 1.1),
            'R': ('r', 1.1),
            'T': ('t', 1.1),
            'Y': ('y', 1.1),
            'U': ('u', 1.1),
            'I': ('i', 1.1),
            'O': ('o', 1.1),
            'P': ('p', 1.1),
            '[': ('[', 1.1),
            ']': (']', 1.1),
            'Enter': ('enter', 1.95),
            '!1': .25,
            'Insert': ('insert', 1.1),
            'Home': ('home', 1.1),
            'Page\nUp': ('pageup', 1.1),
            '!2': .25,
            '7': ('num7', 1.1),
            '8': ('num8', 1.1),
            '9': ('num9', 1.1),
            '+': ('+', 1.1),
        },
        '4': {
            'Caps Lock': ('capslock', 1.5),
            'A': ('a', 1.1),
            'S': ('s', 1.1),
            'D': ('d', 1.1),
            'F': ('f', 1.1),
            'G': ('g', 1.1),
            'H': ('h', 1.1),
            'J': ('j', 1.1),
            'K': ('k', 1.1),
            'L': ('l', 1.1),
            ';': (';', 1.1),
            '\'': ('\'', 1.1),
            '\\': ('\\', 1.1),
            '!1': 2,
            'Delete': ('delete', 1.1),
            'End': ('end', 1.1),
            'Page\nDown': ('pagedown', 1.1),
            '!2': .25,
            '4': ('num4', 1.1),
            '5': ('num5', 1.1),
            '6': ('num6', 1.1),
            '!3': 1.1
        },
        '5': {
            'Shift': ('shiftleft', 1.7),
            'Z': ('z', 1.1),
            'X': ('x', 1.1),
            'C': ('c', 1.1),
            'V': ('v', 1.1),
            'B': ('b', 1.1),
            'N': ('n', 1.1),
            'M': ('m', 1.1),
            ',': (',', 1.1),
            '.': ('.', 1.1),
            '/': ('/', 1.1),
            'shift': ('shiftright', 3.5),
            '!1': 1.38,
            '^': ('up', 1),
            '!2': 1.37,
            '1': ('num1', 1.1),
            '2': ('num2', 1.1),
            '3': ('num3', 1.1),
            'enter': ('enter', 1.07),
        },
        '6': {
            'Ctrl': ('ctrl', 1.25),
            'Win': ('winleft', 1.2),
            'Alt': ('altleft', 1.2),
            'Space': ('space', 6.6),
            'alt': ('right alt', 1.2),
            'win': ('winright', 1.2),
            'print': ('menu', 1.2),
            'ctrl': ('ctrlright', 1.7),
            '!1': .7,
            '<': ('left', 1.1),
            '\/': ('down', 1.1),
            '>': ('right', 1.1),
            '!2': .25,
            '0': ('num0', 2.2),
            'Del': ('del', 1.1),
            '!3': 1.04,
        }
    }

    keys_pressed = []

    def get_row(self, key):
        return ''.join([key_row if key.text in self.keys[key_row] else '' for key_row in self.keys])[0]

    def button_pressed(self):
        keys = [self.keys[key_location[0]][key_location[1]][0] for key_location in self.keys_pressed]
        client.send(f'$!obj!$keyboard$!action!$key-press$!parm!${"$!separator!$".join(keys)}'.encode('utf-8'))

    def press_button(self, key):
        row = self.get_row(key)
        self.keys_pressed.append((row, key.text))
        
        self.button_pressed()
    
    def unpress_button(self, key):
        row = self.get_row(key)

        del_index = 0
        while del_index < len(self.keys_pressed):
            if self.keys_pressed[del_index] == (row, key.text): self.keys_pressed.remove((row, key.text))
            else: del_index += 1

class Menu(BoxLayout):

    def select_controler(self, control_type):
        self.ids['controler'].clear_widgets(self.ids['controler'].children)
        
        if control_type == 1:
            self.ids['controler'].add_widget(Mouse())

        elif control_type == 2:
            self.keyboard = Keyboard(orientation='vertical')
            
            for row in self.keyboard.keys:
                keys_row = GridLayout(rows=1)

                for key in self.keyboard.keys[row]:
                    if key[0] == '!':
                        keys_row.add_widget(Label(text='', size_hint_x=self.keyboard.keys[row][key]))
                    else:
                        keys_row.add_widget(Button(text=key, size_hint_x=self.keyboard.keys[row][key][1], font_size=20, on_release=self.keyboard.unpress_button, on_press=self.keyboard.press_button))

                self.keyboard.add_widget(keys_row)

            self.ids['controler'].add_widget(self.keyboard)

class KontsuApp(App):
    window_size = Window.size

    def build(self):
        menu = Menu()

        return menu

KontsuApp().run()