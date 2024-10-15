# 0x02. Python - Async Comprehension
## Resources
## Read or watch:
- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)
- [Type-hints for generators](https://stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3)
## Asynchronous Comprehensions in Python
- You can traverse an asynchronous generator or asynchronous iterator using an asynchronous comprehension via the “async for” expression.
- An async comprehension is an asynchronous version of a classical comprehension.
- Asyncio supports two types of asynchronous comprehensions, they are the **“async for”** comprehension and the **“await”** comprehension.
- Comprehensions allow data collections like lists, dicts, and sets to be created in a concise way.
- A list comprehension allows a list to be created from a for expression within the new list expression.
```Python
result = [a*2 for a in range(100)]
```
- Comprehensions are also supported for creating dicts and sets.
```Python
# create a dict using a comprehension
result = {a:i for a,i in zip(['a', 'b', 'c'], range(3))}
# create a set using a comprehension
result = {a for a in [1, 2, 3, 2, 3, 1, 5, 4]}
```
- An asynchronous comprehension allows a list, set, or dict to be created using the “async for” expression with an asynchronous iterable.
```Python
# async list comprehension with an async iterator
result = [a async for a in aiterable]
```
- Recall that the “async for” expression may only be used within coroutines and tasks.
- The “await” expression may also be used within a list, set, or dict comprehension, referred to as an await comprehension.
