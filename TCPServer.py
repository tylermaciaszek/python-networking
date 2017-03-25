#Tyler Maciaszek 110039813 Server code to make basic TCP server for lab
#March 9th, 2017
#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort = 9813
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
while True:
    #Establish the connection
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        if message != "": #Checking if empty
            filename = message.split()[1] #get correct file name by splitting 
            f = open(filename[1:]) #open file
            outputdata = f.readlines() #read all the lines of file
            connectionSocket.send(('HTTP/1.1 200 OK\r\n\r\n').encode()) #send and encode data from file
            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.close()
    except IOError:
        connectionSocket.send(("HTTP/1.1 404 Not Found\r\n\r\n").encode()) #File not found error code
    except Exception as inst:
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)          # print the args
        serverSocket.close()  
