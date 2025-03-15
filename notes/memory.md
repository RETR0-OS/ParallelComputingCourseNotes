# Shared VS Distributed Memory

Any parallel computing system is useful only if the data shared between processes can be shared fast enough. Memory orchestration plays a major role in speeding up parallel computing tasks.

Computer memory works much slower than processors. Usually, when one processor is performing I/O operations on a memory block, it prevents other processors from accessing the same memory block. This creates a bottleneck.

## Shared Memory
- All processors have access to the same memory with a global address space.
- If one process changes any memory block, the change is reflected in the other processes as well
- A shared memory need not be stored on the same physical device. It could b spread across a cluster of systems as well.
- Based on the way the processors are connected to memory and how quickly they can access it, shared memory is subdivided into two categories: UMA and NUMA.
- The shared memory architectures are easier to program for as it is easier to shared data between different processors.
- While easy to work with, these systems do not scale well as adding additional processors increases the load on the shared memory bus.

### Uniform Memory Access (UMA)
- All processors have equal access to the memory and can access the memory equal fast.
- The most common type of UMA is a Symmetric Multi Processing System (SMP).
#### SMP
- In SMP, two or more identical processors are connected to the same shared memory, often through a system bus.
- In SMP, every processor has its own "cache" memory, which is extremely fast and only visible to that particular processor. Caches usually introduce "cache coherency" issues, which are usually handled by the hardware itself.
 
### Non-Uniform Memory Access (NUMA)
- Made by physically connecting multiple SMP systems together through a system bus. 
- The access is Non-uniform, ie, some processors have quicker access to certain parts of the memory than others as it takes longer to access memory over the system bus.

## Distributed Memory
- Each processor has its own local memory with its own address space.
- The concept of a global address space does not exist.
- All the processors are connected with some form of a network (eg. Ethernet). Each processor operates independently.
- Any changes made to the local memory of a processor is not reflected in the memory of the other processors.
- The programmer needs to define how and when the data is communicated between processes in a distributed system. This presents a disadvantage as it adds communication overheads.
- The advantage of distributed systems is that they are highly scalable. With more processors added to the system, additional memory is added as well. 