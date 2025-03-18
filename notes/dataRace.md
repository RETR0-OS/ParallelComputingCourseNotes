# Data Race
Data races are a common issue in concurrent programming, where two or more threads access shared data and try to change it at the same time. This can lead to unpredictable behavior and bugs that are difficult to reproduce and fix. To prevent data races in concurrent programming, you can use various synchronization techniques.

## Cause of Data Races
- Mutation operations that modify a shared memory resource without proper synchronization.
- Multiple threads accessing the same memory location simultaneously.
- One thread is in middle of a mutation operation while another thread is reading the same memory location.

## Preventing Data Races

### Mutex (Locks)
- A mutex (mutual exclusion) is a synchronization primitive that allows only one thread to access a shared resource at a time.
- A mutex "locks" the resource to one thread so that any other thread trying to access it enters a "blocked state" until the thread with the mutex releases the lock.
- In Python, you can use the `threading.Lock()` class to create a mutex.
- The section of code that accesses the shared resource is called a "critical section" and should be protected by the mutex.
- For performace optimizations, the critical section should contain minimal number of steps to ensure quick release of the mutex, which allows the other threads to acquire it and execute while computational tasks are executed.
- Use the `threading.Lock.acquire()` method to acquire the lock and `threading.Lock.release()` to release it.<br><br>
``Note: Atomic operations: Operations that are indivisible and cannot be interrupted. Such operations are not interrupted by any other thread. Acquiring the Mutex is an atomic operation.``

### Reentrant Mutex
- A reentrant mutex (or recursive mutex) is a type of mutex that allows the same thread to acquire the lock multiple times without causing a deadlock.
- A deadlock is a situation where a thread tries to reacquire a lock it already holds, causing it to wait indefinitely. This also halts all other processes and threads as they can't unlock the Mutex either.
- A reentrant mutex tracks the number of times it has been acquired by the same thread and allows it to release the lock the same number of times. The reentrant mutex is released only when the thread has released it the same number of times it has acquired it.
- A reentrant mutex is especially useful in recursive functions where the same thread may need to acquire the lock multiple times. Hence, it is often called a "recursive mutex." It can also be used in nested function calls to a function that has a critical section from within the critical section of another function.
- A reentrant mutex can be created using the `threading.RLock()` class in Python. The `threading.RLock()` class is a subclass of `threading.Lock()` and provides the same functionality with the added ability to be reentrant.

### Reentrant Locks V/S Regular Locks
| Reentrant Locks                                                                      | Regular Locks                                                     |
|:-------------------------------------------------------------------------------------|:------------------------------------------------------------------|
| Allows the same thread to acquire the lock multiple times without causing a deadlock | Does not allow the same thread to acquire the lock multiple times |
| Must be released by the same thread that acquired it                                 | Can be released by any thread that holds the lock                 |
| Can be used in recursive functions or nested function calls                          | Cannot be used in recursive functions or nested function calls    |
| More overhead due to tracking the number of acquisitions                             | Less overhead as it does not track the number of acquisitions     |

## Try Lock
- A try lock is a non-blocking way to acquire a lock. It attempts to acquire the lock and returns immediately, regardless of whether the lock was acquired or not.
- If the lock is available, the try lock acquires it and returns `True`. If the lock is not available, it returns `False` without blocking the thread.
- In Python, you can use the `threading.Lock.acquire(blocking=False)` method to create a try lock.
- Try locks are useful when you want to avoid blocking a thread if the lock is not available. However, they should be used with caution as they can lead to unpredictable behavior if not handled properly.
- Try locks can be used in situations where you want to perform a non-blocking operation on a shared resource, such as checking if a resource is available before accessing it.
- Try locks can also be used in situations where you want to avoid blocking a thread if the lock is not available, such as in a GUI application where you want to keep the UI responsive while waiting for a lock. Try locks keep I/O non-critical computational tasks running while waiting for the lock to be released.