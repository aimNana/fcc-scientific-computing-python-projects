# 🎲 Probability Calculator

**Description**  
Simulates drawing balls from a hat to estimate probability outcomes.

---

![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Progress-In%20progress-orange)

---

## 📂 Example

```python
>>> from prob_calculator import Hat, experiment
>>> hat = Hat(blue=4, red=2, green=6)
>>> probability = experiment(
...     hat=hat,
...     expected_balls={"red": 2, "green": 1},
...     num_balls_drawn=5,
...     num_experiments=2000)
>>> print(probability)

0.356
```

---

## 🚀 Usage
```python
from prob_calculator import Hat, experiment

hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000
)
print(probability)
```

---

## 🛠️ Technologies
- Python 3
- Probability and statistics
- Randomization
