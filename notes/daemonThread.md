# Daemon Threads
- Detached from the main parent thread
- If a child thread is initialized as a Daemon thread and the parent thread is finished executing, the parent can enter a terminated state without having to wait for the child thread to finish executing.
- Daemon threads are usually used to run periodic tasks, like garbage collection, in support of the main thread.
- A thread must be explicitly set as a Daemon Thread as by default threads are non-daemon
- A process ends as soon as the main thread finishes execution and there are no non-daemon threads still executing. Hence, since the process terminates in such a situation, any daemon threads attached to that process are also terminated. This means that daemon threads never get to exit gracefully. Hence, daemon threads should never be used to perform sensitive operations like I/O tasks that cannot tolerate abrupt termination.
- When a thread is created, it inherits the Daemon status from its parent. Hence, a daemon thread can never spawn a non-daemon thread. 
