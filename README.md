[![Build Status](https://travis-ci.org/royge/max-valid-time.svg?branch=master)](https://travis-ci.org/royge/max-valid-time)

Problem
=======

Given four digits find the maximum valid time that can be displayed on a digital clock(24 hours format) using those digits. If it's not possible return ```"NOT POSSIBLE```.

Your solution will be:

```python
def max_valid_time(A, B, C, D):
    pass
```

Test cases
----------

1. ```max_valid_time(1, 9, 4, 5)``` should return ```"19:54"```.
2. ```max_valid_time(1, 8, 3, 2)``` should return ```"23:18"```.
3. ```max_valid_time(9, 9, 4, 5)``` should return ```"NOT POSSIBLE"```.
4. ```max_valid_time(6, 9, 8, 5)``` should return ```"NOT POSSIBLE"```.
5. ```max_valid_time(1, 2, 6, 9)``` should return ```"19:26"```.

Run tests
=========

```bash
git clone https://github.com/royge/max-valid-time.git
cd max-valid-time
python -m unittest discover
```
