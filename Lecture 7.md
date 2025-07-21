# Lecture 7 - Testing, Debugging, Exceptions and Assertions

In this lecture, we will learn about debugging, testing and exceptions/assertion statements in Python. 

## Testing, Defensive Programming and Eliminating source of the bugs

In the making soup analogy, check the soup for bugs is the **testing** part, where keep the lid closed is the action of **defensive programming** and cleaning the kitchen is **eliminating the source of bugs**.

In programming each of these actions to ensure high quality on the software can be done by following some good practices:

## Defensive Programming

We can achieve **defensive programming** attitude by writing specification for functions, making sure our program is well documented and avoiding unwanted behavior. By modularizing the code, writing it on different blocks and documenting everything that's happening on each block, we will have a better understanding on what's happening on the code and testing/debugging will be easier to perform.

Once we have a program that's modular and well documented, we still have to test it, and we can do it by checking all the conditions on the inputs and outputs. Given an input, if the output is what we expected then we are done with it. If not, then we can proceed to the debugging phase.

## Debugging and Testing

To **debug** a program we need to **study the events** that lead up to an error and check why is it not working and how to fix it. (This part is not as easier)

Test cases : pairs of inputs and outputs that program is expected to do

Once we have it, we can start doing tests. 3 general classes of tests:

1- Unit testing: validate each piece of program by testing each function separately

2- Regression testing: add tests for bugs as you find them, catch reintroduced errors that were previously fixed

3- Integration testing: does overall program work? Do not rush to do this

### Testing Approaches

Intuition