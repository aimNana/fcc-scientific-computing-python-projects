# ⏱️ Time Calculator

A **Python program** built as part of the  
**FreeCodeCamp Scientific Computing with Python certification**.  

This project practices working with **time calculations**,  
adding durations to a given start time and returning the correct new time and day.

### Example
```python
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tuesday")
# Returns: 12:03 AM, Thursday (2 days later)
