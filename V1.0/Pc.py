import socket
import pyautogui as auto

with open('IPv4.txt', 'r') as file: ip = file.read()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, 9999))
server.listen(2)

client_socket, address = server.accept()
client_socket.send(f'{auto.size()[0]},{auto.size()[1]}'.encode('utf-8'))
while True:
    action = client_socket.recv(1024).decode('utf-8').split('$!obj!$')[-1]
    controler_type = action.split('$!action!$')[0]
    action_type = action.split('$!action!$')[1].split('$!parm!$')[0]
    arguments = action.split('$!parm!$')[-1]
    print(f'{"-"*15}\nControler True: {controler_type}\nAction name: {action_type}\nParameters: {arguments}')

    if controler_type == 'mouse':
        if action_type == 'move':
            arguments = arguments.split('$!separator!$')
            auto.moveTo(int(arguments[0]), int(arguments[1]), 0.1)

        elif action_type == 'click':
            if arguments == 'left':
                auto.leftClick()

            elif arguments == 'right':
                auto.rightClick()

    elif controler_type == 'keyboard':
        if action_type == 'key-press':
            auto.hotkey(*arguments.split('$!separator!$'))