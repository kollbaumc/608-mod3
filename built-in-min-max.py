 def max(value1, value2, value3):
...     '''Return maximum value of three values'''
...     max_value = value1
...     if value2 > max_value:
...        max_value = value2
...     if value3 > max_value:
...        max_value = value3
...     return max_value
...
>>> max(12, 27, 36)
36

>>> def min(value1, value2, value3, value4):
...     '''Return the minimum of 4 values'''
...     min_value = value1
...     if value2 < min_value:
...        min_value = value2
...     if value3 < min_value:
...        min_value = value3
...     if value4 < min_value:
...        min_value = value4
...     return min_value
...
>>> min(15, 9, 27, 14)
9
