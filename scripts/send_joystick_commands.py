import pygame
from pygame.locals import *
import socket
pygame.init()
width, height = 64*10, 64*8
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 2000        # Port to listen on (non-privileged ports are > 1023)
state_dict = {"press":pygame.KEYDOWN,"lift":pygame.KEYUP}
# This distionary holds the important key ids and their current state
# If the key is currently pressed, the second entry in the list is true, else it is false
key_dict = {"forward":[pygame.K_w, False],\
            "left":[pygame.K_a, False],\
            "right":[pygame.K_d, False], \
            "back":[pygame.K_s, False]}            
def print_key_states():
    for k in key_dict:
        if(key_dict[k][1]):
            print(k + " is " + str(key_dict[k][1]) + '\n')

def get_robot_commands():
    # Encode the commands as a byte stream to send to the robot
    # Format is <wheel><direction or stop>
    # Right wheel forward left wheel back is b'rflb'
    # Forward => f, Back => b, stop => s
    command = "rsls"
    if key_dict["forward"][1]: #The w key is pressed
        if(key_dict["left"][1]): #The forward and left keys are pressed
            command = "rfls"
        elif key_dict["right"][1]: #The forward and rightkeys are pressed
            command = "rslf"
        else:
            command = "rflf"

    elif key_dict["back"][1]: #The s key is pressed
        if(key_dict["left"][1]): #The backward and left keys are pressed
            command = "rbls"
        elif key_dict["right"][1]: #The backward and right keys are pressed
            command = "rslb"
        else:
            command = "rblb"
    elif(key_dict["left"][1]): #Only the left key is pressed
        command = "rflb"
    elif key_dict["right"][1]: #The forward and rightkeys are pressed
        command = "rblf" 
    return command.encode('utf-8')
     
def main():
    screen = pygame.display.set_mode((width, height))
    running = True
    
    screen.fill((255,255,255))
    pygame.display.update()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while running:
            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    for k in key_dict:
                        if(key_dict[k][0] == event.key):
                            key_dict[k][1] = True
                            print(k + " key was pressed")
                if(event.type == pygame.KEYUP):
                    for k in key_dict:
                        if(key_dict[k][0] == event.key):
                            key_dict[k][1] = False
                            print(k + " key was released")

                if event.type == pygame.KEYDOWN : 
                    if event.key == pygame.K_ESCAPE:
                        running = False

            c = get_robot_commands()
            s.sendall(c)
            data = s.recv(1024)
            # if data:
            #     print(data.decode('utf-8'))
        s.sendall(b'x') 
        data = s.recv(1024)
        if data:
            print(data.decode('utf-8'))
        s.close()
    pygame.quit()

if __name__ == "__main__":
    main()