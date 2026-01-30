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


## Day 03 – Functions as First-Class Objects  
### Behavior as Data in Python

---

### What I Learned

- Functions in Python are objects and can be:
  - Assigned to variables
  - Stored in data structures
  - Passed as arguments
  - Returned from other functions
- This allows programs to choose behavior dynamically at runtime instead of hard-coding logic with conditionals.

---

### Key Concepts Practiced

- Using dictionaries to map operations to functions
- Passing functions as arguments to execute dynamic behavior
- Returning functions from factory functions
- Building configurable logic without `if / elif` chains

---

### Why This Matters

Modern backend systems rely on treating **behavior as data**.

Frameworks such as FastAPI and Django use this pattern to implement:
- Dependency injection
- Middleware pipelines
- Permission and authorization checks
- Request validation layers

Understanding functions as first-class objects is foundational for writing **clean, extensible, and testable backend code**.

---

### Files

- **function_executor.py**  
  Dynamic operation execution using function mappings.

- **permission_checker.py**  
  Function factory for role-based permission checks.

- **validator_engine.py**  
  Rule-based validation using lists of validator functions.

---

## Day 04 – Closures
### Functions That Retain State Safely

---

## What I Learned

- A **closure** is a function that remembers variables from the scope in which it was created.
- Closures allow state to persist across function calls **without using global variables or classes**.
- The remembered state lives in the **outer function’s local scope**, preserved by the inner function.
- The `nonlocal` keyword is required when an inner function needs to **modify** outer-scope variables.

---

## Key Concepts Practiced

- Creating inner functions that access outer-scope variables
- Retaining private state across multiple function calls
- Using `nonlocal` to safely mutate closure state
- Building stateful logic without globals or object-oriented patterns

---

## What Problem Closures Solve

Closures solve the problem of **state management with isolation**.

They allow functions to:
- Maintain state across calls
- Avoid shared global variables
- Encapsulate logic and data together
- Create multiple independent instances of the same behavior

This enables predictable and reusable behavior in systems that require controlled state.

---

## Why Closures Are Safer Than Globals

Global variables introduce:
- Hidden dependencies
- Shared mutable state
- Race conditions in concurrent systems
- Difficult-to-test logic

Closures provide:
- Private, instance-level state
- Explicit creation of stateful behavior
- Improved testability and predictability
- Better safety in multi-request backend environments

Each closure instance maintains its own isolated memory.

---

## Where This Appears in Backend Systems

Closures are commonly used in backend development for:

- Request and usage counters
- Rate limiting and throttling logic
- Authorization and permission checks
- Dependency injection systems
- Request-scoped configuration and context handling

Frameworks such as FastAPI and Django rely on closure-based patterns internally to manage state without global side effects.

---

## Files

- **request_counter.py**  
  Closure-based request counter that retains state across calls.

- **access_control.py**  
  Role-based access checker using closure-stored permissions.

- **rate_limiter.py**  
  Lightweight rate limiting logic using closure state.
