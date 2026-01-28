# 100-Days-Of-Advanced-Python
A 100-day deep dive into advanced Python concepts through experiments, internals, and real-world use cases.

## Day 01 – Python Execution Model & Memory References

### What I Learned
- Python variables do not store values, they reference objects
- Difference between mutable and immutable objects
- Why assignment does not create a copy
- How function arguments work internally

### Key Insight
Most Python bugs are not syntax problems — they are reference problems.

### Files
- `memory_references.py` → experiments with object identity and mutation

This foundation is critical for writing clean, predictable, and scalable Python code.

## Day 02 – Mutability Traps & Default Arguments

### What I Learned
- Default arguments are evaluated once at function definition
- Mutable defaults cause shared state bugs
- The `None` pattern prevents hidden side effects
- Class constructors are especially risky with mutable defaults

### Key Insight
Defaults belong to the function object, not the function call.

### Files
- `default_arguments.py` → experiments demonstrating shared state bugs
