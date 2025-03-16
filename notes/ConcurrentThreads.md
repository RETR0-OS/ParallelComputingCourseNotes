# Threads for Concurrent Tasks in Python

Concurrent computing in Python is very easy using Threads. However, the Global Interpreter Lock (GIL) feature of Python prevents PARALLEL execution.

## (Global Interpreter Lock) GIL
- A mechanism that prevents multiple python threads from executing at the same time, hence preventing parallel computing.
- Unique to Python
- Despite the presence of the GIL, there are significant advantages to writing multi-threaded programs. 

### CPython Interpreter
- Most common and widely used interpreter
- Underlying code written in a mix of C and Python
- GIL was implemented to ensure thread-safe operations

### Jython
- Java-based interpreter for Python that DOES NOT have the GIL, and hence supports parallel computing.

## When to use Threads

### I/O Bound Tasks and Applications
- GIL is not a bottleneck as most tasks are waiting for external input.
- Can implement concurrent computing using the ```threading``` module.

## When to not use Threads

### CPU Bound Tasks and Applications
- GIL can become a bottleneck as no parallel computing is present. However, work-around are present.
- Such applications are usually written in compiled languages like C++ and included into function libraries that a top-level python program can call-into. This allows the compute-intensive tasks to execute outside the GIL's restrictions using parallel threads.
- To keep parallel-computing tasks written in python, Python provides the ```multiprocessing``` module that allows the program to run across multiple PROCESSES instead of multiple THREADS. Each process has its own interpreter and GIL. So, the different processes can execute in parallel. The downside is sharing data between processes is complicated, and creating and terminating processes has a higher overhead that handling threads.