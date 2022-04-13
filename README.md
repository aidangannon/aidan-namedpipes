# aidan-namedpipes
named pipes experiment, C# and python half-duplex communication through shared memory IPC
# learning outcomes
- basically, having a seperate pipe for upline and downline makes more sense
- when u have same pipe for read/write, you have to close and open in-memory win32 pipe, causing potential syncronization errors
- 2 pipes, 1 for incoming memory reads, 1 for outgoing memory writes
