import sys, time
from socket import *

# Get the server hostname and port as command line arguments
argv = sys.argv
host = argv[1]
port = argv[2]

# Create UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set socket timeout as 1 second
clientSocket.settimeout(1)

# Command line argument is a string, change the port into integer
port = int(port)
# Sequence number of the ping message
seqno = 0

# Ping for 10 times
# Fill in start
while seqno <= 10:
# Fill in end

    # Format the message to be sent
    data = "Ping " + str(seqno) + " " + time.asctime()

    # Attempt to send and receive
    try:
	# Record the sent time
        sntTime = time.time()

	# Send the UDP packet with the ping message
        clientSocket.sendto(data,(host, port))

	# Receive the server response
        data, address = clientSocket.recvfrom(1024)

	# Record the received time
        rcvTime = time.time()

	# Display the server address and server response as an output
        print "Reply from "
        print address
        print data

	# Round trip time is the difference between sent and received time
        print "RTT: " + str(rcvTime - sntTime)

    except timeout:
        # Server does not response
	# Assume the packet is lost
        print "Request timed out."

    # Continue the loop
    # Fill in start			# Fill in end
    seqno += 1


# Close the client socket
# Fill in start			# Fill in end
if seqno > 10:
    clientSocket.close()
