# LeetCode in Python

Python 3.9+ solutions to LeetCode problems, with problem descriptions and standard-library `unittest` tests.

- `easy/` — Easy problems.
- `medium/` — Medium problems.
- `hard/` — Hard problems.

Create a local virtual environment and run all tests from the repository root:

```bash
python3 -m venv .venv
.venv/bin/python -m unittest discover -v
```

In PyCharm, open the repository and select `.venv` as the project interpreter. The shared **All Tests** configuration uses `.venv/bin/python`. No additional dependencies are required.
