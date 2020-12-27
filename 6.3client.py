import socket
import sys

sock = socket.socket()
host = '192.168.0.155'
port = 6666

try:
    sock.connect((host,port))
    print (' Socket successfully connected ! ')
except socket.error as e:
    print ( str(e) )

loop = True

while loop:
    print ('\n ---- MATHEMATICS EQUATION CALCULATOR ----')
    print (' 1. Log Ralculation ')
    print (' 2. Square Root ')
    print (' 3. Exponential ')
    print (' 4. Power ')
    print (' 5. Exit ')

    choice = input ('\n Enter  your choice of equation (e.g = 1) : ' )
    sock.send(choice.encode())

    if choice == '1':
        print ('\n -- Log calculation -- ')
        numb = input('\n Enter Number : ')
        base = input('\n Enter base : ')
        sock.sendall(str.encode('\n'.join([str(numb), str(base)])))
        result = sock.recv(1024)
        print ( ' Answer for log ' + numb + ' base ' + base + ' : ' + str(result.decode()))

    elif choice == '2':
        root = True
        while root:
            print ('\n -- Square Root -- ')
            numb = input ('\n Enter Number : ')
            if float(numb) <  0:
                print('\n Negative Number Cant Be Square Root')
            else:
                root = False
                sock.send(numb.encode())
                result = sock.recv(1024)

        print ( ' Answer for square root of ' + numb +' : ' + str(result.decode()))


    elif choice == '3':
        print ('\n -- Exponential --')
        numb = input ('\n Enter Number : ')
        sock.send(numb.encode())
        result = sock.recv(1024)

        print ( ' Answer for exponential of ' + numb + ' : ' + str(result.decode()))

    elif choice == '4':
        print ('\n -- Power --')
        numb = input('\n Enter Number : ')
        power = input('\n Enter Power : ')
        sock.sendall(str.encode('\n'.join([str(numb), str(power)])))
        result = sock.recv(1024)
        print ( ' Answer for ' + numb + ' power of ' + power + ' : ' + str(result.decode()))

    elif choice == '5':
        numb = '5'
        sock.send(numb.encode())
        sock.close()
        sys.exit()
    else:
        print ('\n Invalid input please try again !')

    input ( '\n Press Enter to Continue .. ')
