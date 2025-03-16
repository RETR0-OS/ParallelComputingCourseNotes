# Execution Scheduling

Different threads and processes do not execute randomly. The OS is responsible for scheduling these different tasks.

## Scheduler
- Included in the OS
- Responsible for scheduling the execution of different threads and processes for execution on the available CPUs
- Enables multiple programs to run concurrently on a single processor.
- Any process that is ready to be executed get loaded into the memory and then into "READY QUEUE." After this, the scheduler cycles through all the processes in the ready queue and assigns eac of them time on the processor. In this case, 3 possible scenarios exist.
  1) The process moves out of the ready queue and runs on the processor till it finishes.
  2) The process moves out the ready queue and runs on the processor, but gets blocked by an I/O event. In this case, this process is moved to the I/O queue and the Scheduler saves the state of this process to resume it later.
  3) The process moves out of the ready and get executed on the processor, but does not finish tits computation in the allotted time. In this case, the Scheduler saves the state of the process and moves it back into the ready queue to be reassigned  execution time and resumed from last checkpoint.
- Scheduler is responsible for storing the states of the currently running processes and loading the context and states of the new processes to be executed.
- The switching between the processes and tasks is called ``context switching.``

### Scheduling Algorithms
- Different operating systems use different scheduling algorithms based on their specific purposes and system requirements
- Some scheduling algorithms aim to maximize throughput, while others focus on minimizing latency for improved responsiveness
- Preemptive scheduling: Can interrupt low-priority processes for high-priority ones
- Non-preemptive scheduling: Allows processes to run for their full allotted time once started
- Types of scheduling algorithms:
  1) First come, first served
  2) Shortest job next
  3) Priority
  4) Shortest time remaining
  5) Round-Robin
  6) Multiple-level queues
- Types of scheduling goals
  1) Maximize throughput
  2) Maximize fairness
  3) Minimize wait time
  4) Minimize latency