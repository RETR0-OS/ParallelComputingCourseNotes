# Concurrent VS Parallel Execution

Just because a program has independent steps that can be executed simultaneously, does automatically make the program parallely executable. Such programs are generally called "concurrent" programs.

## Concurrency
- The ability to be broken into independent parts that can be executed out of order without affecting the final result.
- It focuses on how a program is STRUCTURED, rather than how it is executed.
- In such programs, a single core processor executed multiple instructions from the same program alternately in a sequential manner to give the ILLUSION of parallel processing. The time taken to execute concurrent processes is lesser than that of sequential processes but more than parallel computing.
- Concurrent processes are useful for I/O-bound tasks, such as GUIs. While one process is collecting input or is writing to disk, another process can continue its processing on the processor, hence saving time.

## Parallelism
- The ability of a program to execute independent instructions on a multicore processor at the SAME TIME without affecting the final result.
- It focuses on how the program is EXECUTED, rather than how it is structured.
- In such programs, a multicore processor runs different instructions from the same program parallely at the same time, without have to give turns to a different instruction in the middle of execution. The time taken to complete parallel processes is the least =.
- Parallel computing is useful for compute-intensive tasks which are not interrupted by the need for I/O or any other things, such as matrix multiplications.
- Parallel computing require parallel hardware such as multicore processors, GPUs or Compute Clusters.

## Concurrency V/S Parallelism

| Concurrency                                                  | Parallelism                                         |
|:-------------------------------------------------------------|:----------------------------------------------------|
| Independent tasks executed sequentially                      | Independent tasks executed simultaneously           |
| About program structure dealing with multiple things at once | Program execution and doing multiple things at once |
| Ideal for I/O bound tasks                                    | Ideal for Compute-intensive tasks                   |
| Concurrency does not guarantee parallelism                   | Parallelism does not guarantee a speed-up           |
| Can be achieved on a single-core processor                   | Requires parallel hardware                          |