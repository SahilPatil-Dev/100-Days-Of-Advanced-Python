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

## Day 07 – Modules, Packages & Project Structure
### Organizing Python Code Like Real Backend Systems

---

## Why Structure Matters More Than Syntax

In backend systems, code is read more often than it is written.

Clean structure:
- Reduces onboarding time
- Prevents accidental bugs
- Makes systems easier to extend
- Lowers maintenance risk

Messy structure increases cost, not speed.

---

## How the Code Is Layered

- **main.py**
  Entry point responsible only for orchestration and error handling.

- **validators/**
  Input validation logic. Rejects bad data early.

- **services/**
  Business logic and core operations.

- **exceptions/**
  Custom, domain-specific exceptions shared across layers.

Each layer has a single responsibility.

---

## Where Business Logic Lives

Business logic lives inside the **services** layer.

- It is never placed in `main.py`
- It does not handle user interaction
- It raises errors instead of printing messages

This mirrors real backend service architecture.

---

## Project Structure

- **main.py**  
  Application entry point and error boundary.

- **validators/user.py**  
  User input validation logic.

- **services/payment.py**  
  Payment processing logic.

- **exceptions/errors.py**  
  Custom exception definitions.

---

## Day 08 – Python Standard Library Power
### Writing Safer Backend Code Using Built-in Tools

---

## Why Standard Library Mastery Matters

Production backend systems fail due to:
- broken file paths
- duplicate identifiers
- incorrect timestamps
- missing logs

Python’s standard library provides reliable, battle-tested tools to prevent these issues without adding unnecessary dependencies.

---

## What This Project Demonstrates

This project simulates a backend login audit system using only the Python standard library.

It focuses on:
- safe file handling
- request traceability
- timezone-aware event logging
- structured persistence

---

## Key Tools Used

### pathlib
Used to locate and manage files safely across operating systems without fragile string paths.

### datetime (timezone-aware)
All timestamps are generated using UTC to avoid silent timezone bugs common in backend systems.

### uuid
Each login event is assigned a globally unique request ID, making events traceable across systems.

### logging
The logging module is used instead of `print()` to produce structured, timestamped, severity-aware output suitable for production environments.

---

## Why print() Is Avoided

`print()` statements:
- lack severity levels
- cannot be filtered
- do not scale in production

The logging module provides observability required for real backend systems.

---

## File Overview

- **login_audit.py**  
  Simulates a backend login audit system.  
  Each login generates a unique request ID, a timezone-aware timestamp, is persisted to disk, and logged using Python’s logging module.

---

## Backend Relevance

Patterns used here appear directly in:
- authentication systems
- audit logging
- request tracing
- security event tracking
- compliance logs

This reflects real backend infrastructure behavior using only Python’s standard library.

---

## Day 09 – Data Validation & Serialization
### Making Python Code API-Ready Without Frameworks

---

## Purpose of This Project

Backend systems never trust raw input.

This project demonstrates how to:
- validate untrusted input at a clear boundary
- normalize data into a predictable internal model
- serialize internal objects into JSON-safe output
- handle validation errors at the system boundary

The structure mirrors how real APIs process requests internally.

---

## Validation Boundary

All input validation happens inside the `User.from_dict()` method.

This ensures:
- business logic never validates input
- validation rules are centralized
- invalid data is rejected early

Raw dictionaries are never passed deeper into the system.

---

## Internal Model vs External Representation

### Internal Model (`User`)
- Strongly typed
- Normalized (email lowercased, age converted to int)
- Safe for business logic to consume

### External Representation
- Plain dictionaries
- JSON-safe
- Only approved fields are exposed

Internal objects are never returned directly.

---

## Error Handling Strategy

- Custom exceptions are raised during validation
- Errors propagate upward naturally
- Exceptions are caught only at the API boundary
- Clean error messages are returned to the caller

This avoids silent failures and keeps control flow predictable.

---

## Request Lifecycle (Simulated)

The API simulation follows this exact flow:

1. Receive raw input dictionary
2. Validate and normalize input
3. Create internal `User` object
4. Serialize output
5. Catch validation errors at the boundary
6. Return success or error response

This mirrors the internal behavior of backend frameworks like FastAPI and Django REST Framework.

---

## File Overview

- **user_schema.py**  
  Defines the internal `User` model and handles validation and normalization.

- **serializer.py**  
  Converts internal user objects into JSON-safe dictionaries.

- **main.py**  
  Simple execution example demonstrating validation and serialization.

- **api_simulator.py**  
  Simulates an API endpoint with proper error handling boundaries.

---

## Backend Relevance

The patterns used here appear directly in:
- API request parsing
- schema validation layers
- service boundaries
- response serialization
- input safety enforcement

Understanding this flow is required before using API frameworks.

---

## Day 10 – Testing Strategy
### Writing Backend-Grade Tests That Protect Behavior

---

## Purpose of This Day

Backend code is changed far more often than it is written.

This day focuses on writing tests that:
- protect critical behavior
- prevent invalid data from entering the system
- catch regressions early
- make refactoring safe

Untested backend code is considered unfinished.

---

## What Is Tested (Intentional Scope)

This test suite focuses on **high-risk backend logic**:

### Validation Layer
- User input validation
- Type normalization
- Failure cases for invalid data

### Serialization Layer
- JSON-safe output
- Data exposure control
- Output structure stability

Low-value targets such as printing, logging, or internal implementation details are intentionally not tested.

---

## Validation Tests (Failure-Focused)

The validation tests assert that:

- Valid input produces a clean internal `User` object
- Invalid emails raise `InvalidEmailError`
- Underage users raise `InvalidAgeError`
- Edge cases (strings, negatives, floats) are rejected explicitly

Parameterized tests are used to ensure multiple failure cases are covered without duplicating test code.

This ensures the system **fails early and predictably** when receiving bad input.

---

## Serialization Tests (Data Safety)

Serialization tests verify that:

- Output is JSON-safe (`dict`)
- Only approved fields are exposed
- Internal object state is never leaked

These tests protect against accidental data exposure — a real production risk in API systems.

---

## Regression Test (Test-Driven Fix)

A regression test was added to ensure that:
- Float values for `age` are rejected
- Silent type coercion does not introduce invalid data

This test simulates a real backend bug report:
1. A failing test is written first
2. The implementation is fixed
3. The test suite passes again

This workflow mirrors professional backend development practices.

---

## Testing Philosophy Used

- Tests focus on **behavior**, not implementation
- Failure paths are tested as seriously as success paths
- Each test validates a single responsibility
- Exceptions are asserted explicitly
- Tests remain stable during refactoring

---

## Project Structure

- **tests/test_user_validation.py**  
  Covers valid input, invalid email cases, underage users, and regression scenarios.

- **tests/test_serializer.py**  
  Ensures safe, predictable, and controlled serialization output.

- **test_driven_fix.py**  
  Demonstrates test-first bug fixing to prevent regressions.

---

## Backend Relevance

These testing patterns are directly applicable to:
- API validation layers
- Schema enforcement
- Regression prevention
- Safe refactoring in team environments

This is the baseline expected for backend engineers working on production systems.

---

## Day 11 – Type Hints & Static Thinking
### Writing Safer, Contract-Driven Python Backend Code

---

## Why Type Hints Matter in Backend Systems

Backend systems are maintained by teams, not individuals.

Type hints:
- clarify function contracts
- reduce misuse of APIs
- make intent explicit
- improve long-term maintainability

They are not about verbosity — they are about safety.

---

## Static Thinking in a Dynamic Language

Static thinking means designing code with clear expectations:

- what data is allowed
- what is optional
- what is guaranteed after validation
- what failures look like

Type hints force these decisions early.

---

## Where Types Prevent Bugs

- Preventing missing fields (`Optional`)
- Preventing silent type coercion
- Clarifying untrusted vs trusted data
- Making illegal states obvious

Runtime checks enforce correctness.
Type hints document intent.

---

## Project Structure

- **user_service.py**  
  Defines typed validation boundaries and user creation logic.

- **discount_calculator.py**  
  Demonstrates defensive, type-safe business logic.

- **typed_api_simulator.py**  
  Simulates an API handler using typed contracts and clear error boundaries.

---

## Team Collaboration Benefits

Typed code:
- is easier to review
- is safer to refactor
- reduces onboarding time
- scales better across teams

This is why typed Python is expected in backend roles.

---

## Day 12 – Configuration & Environment Management
### Designing Backend Code That Runs Safely Across Environments

---

## Why Configuration Must Not Live in Code

Backend systems run across multiple environments:
- development
- staging
- production

Hardcoding environment-specific values makes systems fragile and unsafe.

Configuration must be separated from code so behavior remains consistent while environments change.

---

## Centralized Configuration Pattern

This project uses a single configuration module responsible for:
- reading environment variables
- converting types
- validating required values
- failing fast on invalid configuration

All services import configuration instead of redefining it.

---

## Environment Variables and Safety

Environment variables:
- keep secrets out of source control
- allow safe environment switching
- support containerized and cloud deployments

Invalid or missing configuration causes the application to exit immediately.

---

## Startup Fail-Fast Strategy

Configuration errors are handled only at application startup.

The application:
- never starts in an invalid state
- exits with a clear error message
- avoids undefined behavior later in execution

This mirrors real backend application initialization flows.

---

## Project Structure

- **config.py**  
  Centralized configuration loading and validation.

- **database_service.py**  
  Service layer that consumes configuration without redefining it.

- **app.py**  
  Application entry point and startup error boundary.

---

## Backend Relevance

This pattern is used in:
- API servers
- background workers
- microservices
- containerized applications

Separating configuration from code is a non-negotiable backend practice.

---
