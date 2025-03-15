# Threads and Processes

# Process
- The instance of a program executed by a computer is called a "process."
- A process consists of a program's code, data and state.
- Each process is independent and has its own address space in memory.
- The OS is responsible for managing all simultaneous processes. 

# Threads
- Smaller sub-elements that exist within a process.
- Each thread is an independent path of execution within a process - an independent set of instructions.
- The most basic units managed by the OS. The OS allocates each thread time on the processor to execute its instructions.
- Threads that are a part of the same process share the same address space which gives them access to the same resources in memory and the same data.

```text
Sharing data and resources between processes is possible, but not as easy as sharing data between two threads of the same process. This is because each process exists in a separate memory location. To share data between two processes, programmers have to use system-provided Inter-Process Communication (IPC) like:
- Sockets and Pipes
- Allocation special inter-process shared memory space
- Using remote procedure calls
```
## Threads V/S Processes

| Processes                                  | Threads                                  |
|:-------------------------------------------|:-----------------------------------------|
| Resource - intensive                       | light weight                             |
| More overhead in creation and termination  | low overhead in creation and termination |
| Slower to switch between processes         | faster to switch between threads         |
| Own address space                          | Shared address space                     |
