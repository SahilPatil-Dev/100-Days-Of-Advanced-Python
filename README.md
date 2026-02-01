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

## Day 05 – Decorators
### Wrapping Behavior Like Real Frameworks

---

## What I Learned

- A decorator is a function that **wraps another function** to add behavior without modifying the original code.
- Decorators replace the original function with a wrapper function at definition time.
- The wrapper controls **when and how** the original function is executed.
- `*args` and `**kwargs` are required to make decorators reusable for functions with different signatures.
- Decorators can accept configuration by using **multiple nested functions**.

---

## Key Concepts Practiced

- Function wrapping and replacement
- Using closures to retain access to the original function
- Writing generic wrappers with `*args` and `**kwargs`
- Creating decorators with arguments for configurable behavior
- Preserving original function behavior while adding cross-cutting logic

---

## What Problem Decorators Solve

Decorators solve the problem of **repetitive cross-cutting logic**.

In backend systems, many functions require the same additional behavior such as logging, authentication, or monitoring.  
Decorators allow this behavior to be added **externally**, without duplicating code or modifying business logic.

This results in cleaner, more maintainable systems.

---

## How Decorators Wrap Behavior

- At definition time, the decorator receives the target function.
- The decorator returns a wrapper function.
- The wrapper replaces the original function.
- When the function is called, the wrapper executes first and decides when to invoke the original function.

This wrapping mechanism allows behavior to run **before and after** the original function execution.

---

## Where Decorators Appear in Backend Systems

Decorators are a foundational pattern in backend frameworks and infrastructure code, including:

- Authentication and authorization layers
- Logging and request tracing
- Middleware pipelines
- Dependency injection systems
- Performance monitoring and metrics collection

Frameworks such as FastAPI and Django rely heavily on decorator-based patterns to implement these features.

---

## Files

- **logging_decorator.py**  
  Decorator for logging function calls, arguments, and return values.

- **auth_decorator.py**  
  Role-based access control using a configurable decorator.

- **performance_tracker.py**  
  Execution time measurement for performance monitoring.

---

## Day 06 – Error Handling Strategy
### Designing Fail-Safe Python Code

---

## What I Learned

- Errors are part of normal backend control flow.
- Exceptions should be **raised where detected** and **caught only at boundaries**.
- Returning error strings hides failures and breaks control flow.
- Custom exceptions make intent and failure causes explicit.
- Not all errors should be handled immediately.

---

## Why Exceptions Are Better Than Return Codes

- Exceptions separate error logic from business logic.
- They prevent silent failures.
- They preserve stack traces and context.
- They force the caller to consciously handle failure cases.

Return codes are easy to ignore. Exceptions are not.

---

## Where Errors Should Be Handled in Backend Systems

- Input validation layers
- API boundaries
- Service entry points
- Application startup logic

Lower-level functions should raise errors, not decide outcomes.

---

## User Errors vs System Errors

- User errors:
  - Invalid input
  - Broken business rules
  - Raised intentionally and handled cleanly

- System errors:
  - File access issues
  - Permission problems
  - Missing resources
  - Wrapped and re-raised with context

---

## Files

- **input_validation.py**  
  Custom exceptions for request-style input validation.

- **service_layer.py**  
  Demonstrates controlled error propagation and boundary handling.

- **safe_file_reader.py**  
  Safe file access with preserved error context.

---
