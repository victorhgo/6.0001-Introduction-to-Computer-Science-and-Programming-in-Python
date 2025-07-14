# Lecture 1: What is Computation?

Introduction to the Theory of Computation. What are the main goals?

- Knowledge of Concepts
- Programming Skills
- Problem Solving 

What does a computer do?

- Calculations
- Remember results
- You can program and tell it what to do!

Types of knowledge:

- *Declarative* is statement of facts:
              "It's raining right now"

- *Imperative* is a _recipe_, "how to"

What is a recipe?

1. Sequence of simple *steps*
2. *flow of control* 
3. a way to *stop* the execution

An algorithm has the same principles, since computers are machines, we need to learn:

- How to capture a recipe in a mechanical process

- Fixed program computer (like a calculator)

- *Stored program* computers

Basic Machine architecture - Central Processing Unit (the "brain")

- Memory (sequence of instructions, data)
- Input/Output
- ALU - Arithmetic Logic Unit (primitive operations)
- Control Unit (program counter)

### Basic Primitives

Alan Turing shows that you can compute anything with 6 primitives: Move Left, Move Right, Read/Write, Scan and Do Nothing. Programming languages provide a set of primitive operations

Programming languages can abstract methods to *create new primitives* and anything computable in one language is computable in any other programming language.

Expressions are complex but legal combination of primitives in a programming language.

Primitive Constructs: in English they are words, in programming languages they are numbers, strings, operators

Where does things go wrong?

Syntactic errors, static semantic errors (can cause unpredictable behavior), program runs forever, crashes or gives a complete different answer than expected.

What is a program? 

A sequence of definitions and commands
 Definitions are evaluated
 Commands are executed in a shell by the interpreter (for instance)

Python commands can be typed directly in the shell.

What is an Object?

In Python, everything is an object, and programs manipulate these data objects.

Objects have a *type* (int, float, char, string) and they can be either scalar (cannot be subdivided) or non-scalar (have internal structure that can be accessed)

Scalar objects are:

- int - integers (1, 2, 3 ...)
- float - real numbers in general (3.14)
- bool - Boolean values (True and False)
- NoneType - special and has one value, None

type() returns the value:

```sh
>>> type(5)
int
>>> type(3.14)
float
>>> type('V')
str
```

We can convert object of one type to another (cast):

_float(3)_ converts integer 3 to float 3.0
int(3.9) truncates float 3.9 to integer 3

Printing to console:

```sh
>>> 3 + 2
5
>>> print(3+2)
5
```

Expressions - Combine objects and operators to form _expressions_ in a way that expressions has a value, therefore has a type.

Operators on int and floats: sym, difference, product, division, the remainder of (%), power of.

_i % j_ the remainder when dividing i by j

Simple operations - Operator precedence: **, *, / + and - (executed to left to right)

Binding variables and values: Using the equal sign to assign a value to a variable:

pi = 3.14159

- Value stored in computer memory
- Retrieve the value by invoking the name

Abstracting Expressions - why give names to values of expressions? To reuse names instead of values, making the code easier to change later.

Programming vs Math - We don't solve for x

```py
pi = 3.14159
radius = 2.2
# area of circle equation <- this is a comment
area = pi * (radius ** 2)
print(area)
```

Exercise > Change the value of Radius










