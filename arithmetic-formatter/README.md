# ➗ Arithmetic Formatter

**Description**  
Formats a list of arithmetic problems (addition and subtraction) vertically and neatly.  
Supports up to 5 problems. Optionally, results can also be displayed.

---

![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)  


---

## 📂 Example

```python
>>> arithmetic_formatter(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
   32         3801      45      123
+ 698      -     2    + 43    +  49
-----      ------    ----    -----
  730      3799      88      172
```

---

## 🚀 Usage
```bash
python arithmetic_formatter.py
```
Or import the function in another script:
```python
from arithmetic_formatter import arithmetic_formatter
```

---

## 🛠️ Technologies
- Python 3
- String formatting
- Basic error handling
