# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explored two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)
The application verified the performance of these structures 
using data insertion, removal and critical edge cases.

## Learning Objectives
Features implemented included:
- Stack operations where I built an internal list structure using standard 
  Python arrays. Implemented `push`, `pop`, `peek`, and `is_empty` 
  mechanics to support Last-In, First-Out (LIFO) behavior
- Queue operations where I Utilized an optimized `collections.deque` sequence to 
  build efficient `enqueue`, `dequeue`, `front`, and `is_empty` operations 
  following First-In, First-Out (FIFO) standards.

## Execution and Test Scenarios
The script ran the following:
1. **Empty State Validation:** Tested boundary bounds by attempting to pop, peek, 
    dequeue, and inspect the front of completely empty structures, verifying 
    that errors were intercepted gracefully.
2. **Sequential Data Processing:**
   - Pushed numeric elements (`10, 20, 30, 40`) onto the stack and verified they 
     reversed order upon retrieval.
   - Enqueued array elements (`'A', 'B', 'C', 'D'`) to the queue and verified they 
     maintained their original order upon retrieval.
3. **Single-Item Life Cycle:** Inserted a single item into both structures, deleted it, 
   and validated that the container returned to a completely empty state.
- 
## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.
