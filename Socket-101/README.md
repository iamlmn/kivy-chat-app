#Socket 101

The socket itself is just one of the endpoints in a communication between programs on some network.

A socket will be tied to some port on some host. In general, you will have either a client or a server type of entity or program.


In the case of the server, you will bind a socket to some port on the server (localhost). In the case of a client, you will connect a socket to that server, on the same port that the server-side code is using.


For IP sockets, the address that we bind to is a tuple of the hostname and the port number.

###  Buffering and streaming data

What if the msg exceeds the buffer size?

There are a few logical ways that you could handle for this, but one common way is by starting all messages with a header that contains the length of the message that is going to come. The next challenge is normalizing this header in some way. You might consider using some series of characters, or some format, but then you run the risk of people accidentally, or purposefully, mimicking this formatting. Instead, you can go with a fixed-length header, where the first n bytes of data will be the header data, which will include the length of the message to come. Once we've received that length of data, we know any following information will be a new message, where we need to grab the header and continue repeating this process.

So what we need to do now is choose some truly maximal message size. Say, 1,000,000,000 bytes. Right, there's almost no circumstance where someone would attempt anything even close to this via our chat app, so this will be fine. That number is 10 bytes (10 chars).

