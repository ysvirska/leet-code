# LeetCode in Python

Solutions with problem descriptions and `unittest` tests.

- `easy/` — Easy problems; start here.
- `medium/` — Medium problems.
- `hard/` — Hard problems.

Within each difficulty level, choose problems by popularity on LeetCode, using the number of likes as a guide. Problem numbers are LeetCode IDs, not the solving order.

| # | Problem | Difficulty | Solution | Tests |
| --- | --- | --- | --- | --- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | [Code](easy/two_sum.py) | [Tests](easy/test_two_sum.py) |

Run all tests from the repository root:

```bash
python3 -m unittest discover -v
```

Run tests for a single problem:

```bash
python3 -m unittest easy.test_two_sum -v
```

No additional dependencies are required.
