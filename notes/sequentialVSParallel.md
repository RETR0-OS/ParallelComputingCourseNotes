# Sequential vs Parallel Processing

## Sequential Processing
- Tasks are executed one after the other.
- One task must be completed before executing the next
- Sequential programs are limited by the speed of the processor.

## Parallel Processing
- Tasks are executed side-by-side.
- While one task is executing, another is also executed together and the result is aggregated together in the end
- Parallel programs require "coordination" between the parallel steps. Some steps might be dependent on the completion of the previous steps.
- Parallel programs generally increase the throughput of any program.

### Parallel Computing Architectures

#### Flyn's Taxonomy

1) **SISD (Single Instruction Single Data)**: The simplest of the four classes. A sequential computer with a single processor.
2) **MISD (Multiple Instruction Single Data)**: This type of parallel computer executes multiple instructions on the SAME data at the same time. Not very commonly used. 
3) **SIMD (Single Instruction Multiple Data)**: A type of parallel computer with multiple processing units. All of its processors execute ONE instruction at any time, but they can do it on multiple data objects at the same time. Useful when the same operation is performed on massive amounts of data, like image processing. many modern computers use GPUs with SIMD instructions for image processing. 
4) **MIMD (Multiple Instruction Multiple Data)**: The most commonly used type of parallel computing architecture. Every processing unit can execute a different set of instruction on different data at the same time. Used in network clusters in supercomputers and multicore PCs.

##### MIMD Subdivisions
The MIMD architecture provides significant advantages. Hence, it is further subdivided into two types:
- **SPMD (Single Program Multiple Data)**: Multiple processing units execute a copy of the same program on different units of data. Now, even though each processor is executing the same PROGRAM, they do NOT have to be executing the same INSTRUCTION at the same time. This advantage makes it the most widely used form of parallel computing.
- **MPMD (Multiple Program Multiple Data)**: Multiple processing units execute multiple programs on different data units at the same time. Such a program usually assigns one processor as the "host" or the manager that orchestrates the different the processors and farms out the data to them to be processed, collects results and performs aggregation.