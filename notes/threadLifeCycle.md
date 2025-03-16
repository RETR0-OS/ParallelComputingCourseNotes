# Thread Lifecycle

Every Program starts out on one thread called the "main" thread. As the program executes, the main thread might create additional child threads, if declared in the program to help out. Those children threads may also be allowed to create additional children, as the program declares. As the children threads finish execution, they notify their parent and terminate. Usually, the main thread is the last to finish execution but this is not compulsory.

Over their lifecycle, from instantiation to termination, a thread may be in one of four states

## The New State
- Any child threads first spawned, spawn in the New State.
- This thread is not running yet, and hence does not take up any CPU resources.
- A New State thread must be assigned a function that it is going to execute.
- Some programming languages require the program to explicitly start the thread after creating it.

## The Runnable State
- Once a thread is "started" from the New State, it enters the Runnable state.
- At this point, the OS scheduler can schedule this thread to execute.

## Blocked State
- Once a Runnable Thread reaches a point where it has to wait for an external event to occur (such as an I/O event), the thread enters the Blocked State.
- When a thread is in the Blocked State, it doesn't use any CPU resources.
- When the external event is completed, then the Blocked State thread returns to the Runnable State.

### The .join() method
- The .join() method is a method of the ``threading`` module's Thread class that allows the thread to enter a Blocked State where it waits for its children threads to finish execution before proceeding. It is useful when the results of the concurrent computation have to be aggregated before proceeding.

## Terminated State
- The Terminated State is achieved when the thread finishes executing.
- Right before entering the Terminated State, the thread notifies its parent that it has finished executing.
- After entering the Terminated State, the thread is freed and no longer uses CPU resources.
- The Terminated State is enter when the thread either finishes execution or is abruptly aborted (due to error or input).