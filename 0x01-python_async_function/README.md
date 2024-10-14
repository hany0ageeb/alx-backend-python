# 0x01. Python - Async
## Resources
### Read or watch:
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)
## Async IO in Python: A Complete Walkthrough
- Async IO is a concurrent programming design that has received dedicated support in Python, evolving rapidly from Python 3.4 through 3.7, and probably beyond.
### Here’s what you’ll cover:
- **Asynchronous IO (async IO):** a language-agnostic paradigm (model) that has implementations across a host of programming languages
- **async/await:** two new Python keywords that are used to define coroutines
- **asyncio:** the Python package that provides a foundation and API for running and managing coroutines

Coroutines (specialized generator functions) are the heart of async IO in Python, and we’ll dive into them later on.

**Parallelism** consists of performing multiple operations at the same time. Multiprocessing is a means to effect parallelism, and it entails spreading tasks over a computer’s central processing units (CPUs, or cores). Multiprocessing is well-suited for CPU-bound tasks: tightly bound for loops and mathematical computations usually fall into this category.

**Concurrency** is a slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner. (There’s a saying that concurrency does not imply parallelism.)

**Threading** is a concurrent execution model whereby multiple threads take turns executing tasks. One process can contain multiple threads. Python has a complicated relationship with threading thanks to its GIL, but that’s beyond the scope of this article.

What’s important to know about threading is that it’s better for IO-bound tasks. While a CPU-bound task is characterized by the computer’s cores continually working hard from start to finish, an IO-bound job is dominated by a lot of waiting on input/output to complete.

concurrency encompasses both multiprocessing (ideal for CPU-bound tasks) and threading (suited for IO-bound tasks). Multiprocessing is a form of parallelism, with parallelism being a specific type (subset) of concurrency. The Python standard library has offered longstanding support for both of these through its multiprocessing, threading, and concurrent.futures packages.

The asyncio package is billed by the Python documentation as a library to write concurrent code. However, async IO is not threading, nor is it multiprocessing. It is not built on top of either of these.

In fact, async IO is a single-threaded, single-process design: it uses cooperative multitasking, a term that you’ll flesh out by the end of this tutorial. It has been said in other words that async IO gives a feeling of concurrency despite using a single thread in a single process. Coroutines (a central feature of async IO) can be scheduled concurrently, but they are not inherently concurrent.

To reiterate, async IO is a style of concurrent programming, but it is not parallelism. It’s more closely aligned with threading than with multiprocessing but is very much distinct from both of these and is a standalone member in concurrency’s bag of tricks.

That leaves one more term. What does it mean for something to be asynchronous? This isn’t a rigorous definition, but for our purposes here, I can think of two properties:

- Asynchronous routines are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.
- Asynchronous code, through the mechanism above, facilitates concurrent execution. To put it differently, asynchronous code gives the look and feel of concurrency.
## Async IO Explained
Async IO may at first seem counterintuitive and paradoxical. How does something that facilitates concurrent code use a single thread and a single CPU core?

Async IO takes long waiting periods in which functions would otherwise be blocking and allows other functions to run during that downtime. (A function that blocks effectively forbids others from running from the time that it starts until the time that it returns.)

## The asyncio Package and async/await
Now that you have some background on async IO as a design, let’s explore Python’s implementation. Python’s asyncio package (introduced in Python 3.4) and its two keywords, async and await, serve different purposes but come together to help you declare, build, execute, and manage asynchronous code.
## The async/await Syntax and Native Coroutines
At the heart of async IO are coroutines. A coroutine is a specialized version of a Python generator function. Let’s start with a baseline definition and then build off of it as you progress here: a coroutine is a function that can suspend its execution before reaching return, and it can indirectly pass control to another coroutine for some time.

```python
#!/usr/bin/env python3
# countasync.py
import asyncio
async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == '__main__':
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed: 0.2f} seconds")
```
```shell
$ python3 countasync.py
One
One
One
Two
Two
Two
countasync.py executed in 1.01 seconds.
```
The order of this output is the heart of async IO. Talking to each of the calls to count() is a single event loop, or coordinator. When each task reaches await asyncio.sleep(1), the function yells up to the event loop and gives control back to it, saying, “I’m going to be sleeping for 1 second. Go ahead and let something else meaningful be done in the meantime.”

Contrast this to the synchronous version:

```python
#!/usr/bin/env python3
# countsync.py

import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
```
While using time.sleep() and asyncio.sleep() may seem banal, they are used as stand-ins for any time-intensive processes that involve wait time. (The most mundane thing you can wait on is a sleep() call that does basically nothing.) That is, time.sleep() can represent any time-consuming blocking function call, while asyncio.sleep() is used to stand in for a non-blocking call (but one that also takes some time to complete).

As you’ll see in the next section, the benefit of awaiting something, including asyncio.sleep(), is that the surrounding function can temporarily cede control to another function that’s more readily able to do something immediately. In contrast, time.sleep() or any other blocking call is incompatible with asynchronous Python code, because it will stop everything in its tracks for the duration of the sleep time.

## The Rules of Async IO
At this point, a more formal definition of async, await, and the coroutine functions that they create are in order. This section is a little dense, but getting a hold of async/await is instrumental, so come back to this if you need to:

- The syntax async def introduces either a native coroutine or an asynchronous generator. The expressions async with and async for are also valid, and you’ll see them later on.
- The keyword await passes function control back to the event loop. (It suspends the execution of the surrounding coroutine.) If Python encounters an await f() expression in the scope of g(), this is how await tells the event loop, “Suspend execution of g() until whatever I’m waiting on—the result of f()—is returned. In the meantime, go let something else run.”

In code, that second bullet point looks roughly like this:
```python
async def g():
    # Pause here and come back to g() when f() is ready
    r = await f()
    return r
```
There’s also a strict set of rules around when and how you can and cannot use async/await. These can be handy whether you are still picking up the syntax or already have exposure to using async/await:
- A function that you introduce with async def is a coroutine. It may use await, return, or yield, but all of these are optional. Declaring async def noop(): pass is valid:
    - Using await and/or return creates a coroutine function. To call a coroutine function, you must await it to get its results.
    - It is less common (and only recently legal in Python) to use yield in an async def block. This creates an asynchronous generator, which you iterate over with async for. Forget about async generators for the time being and focus on getting down the syntax for coroutine functions, which use await and/or return.
    - Anything defined with async def may not use yield from, which will raise a SyntaxError.
    - Just like it’s a SyntaxError to use yield outside of a def function, it is a SyntaxError to use await outside of an async def coroutine. You can only use await in the body of coroutines.
    - Finally, when you use await f(), it’s required that f() be an object that is awaitable. Well, that’s not very helpful, is it? For now, just know that an awaitable object is either (1) another coroutine or (2) an object defining an .__await__() dunder method that returns an iterator. If you’re writing a program, for the large majority of purposes, you should only need to worry about case #1.
    ```python
    #!/usr/bin/env python3
    # rand.py
    import asyncio
    import random
    # ANSI colors
    c = (
        "\033[0m", # end of color
        "\033[36m", # Cyan
        "\033[91m", # Red
        "\033[35m", # Magenta
    )
    async def makerandom(idx: int, threshold: int = 6) -> int:
        print(c[idx + 1] + f"Initiated makerandom({idx}).")
        i = random.randint(0, 10)
        while i <= threshold:
            print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
            await asyncio.sleep(idx + 1)
            i = random.randint(0, 10)
        print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
        return i
    async def main():
         res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
        return res
    if __name__ == "__main__":
        random.seed(444)
        r1, r2, r3 = asyncio.run(main())
        print()
        print(f"r1: {r1}, r2: {r2}, r3: {r3}")
    ```
    ## Async IO Design Patterns
    Async IO comes with its own set of possible script designs, which you’ll get introduced to in this section.
    ### Chaining Coroutines
    A key feature of coroutines is that they can be chained together. (Remember, a coroutine object is awaitable, so another coroutine can await it.) This allows you to break programs into smaller, manageable, recyclable coroutines:
```Python
    #!/usr/bin/env python3
# chained.py

import asyncio
import random
import time

async def part1(n: int) -> str:
    i = random.randint(0, 10)
    print(f"part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(f"Returning part1({n}) == {result}.")
    return result

async def part2(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"part2{n, arg} sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(f"Returning part2{n, arg} == {result}.")
    return result

async def chain(n: int) -> None:
    start = time.perf_counter()
    p1 = await part1(n)
    p2 = await part2(n, p1)
    end = time.perf_counter() - start
    print(f"-->Chained result{n} => {p2} (took {end:0.2f} seconds).")

async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))

if __name__ == "__main__":
    import sys
    random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")
```