# 💰 Budget App

**Description**  
Implements a budget tracking tool with ledger functionality and a textual spending chart.

---

![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Progress-In%20progress-orange)

---

## 📂 Example

```python
>>> from budget import Category, create_spend_chart
>>> food = Category("Food")
>>> food.deposit(1000, "initial deposit")
>>> food.withdraw(10.15, "groceries")
>>> food.withdraw(15.89, "restaurant and more food")
>>> clothing = Category("Clothing")
>>> clothing.deposit(500, "initial deposit")
>>> clothing.withdraw(25.55, "t-shirt")
>>> print(create_spend_chart([food, clothing]))

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o     
  0| o  o     
    ----------
     F  C  
     o  l  
     o  o  
     d  t  
        h  
        i  
        n  
        g  
```

---

## 🚀 Usage
```python
from budget import Category, create_spend_chart

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")

clothing = Category("Clothing")
clothing.deposit(500, "initial deposit")
clothing.withdraw(25.55, "t-shirt")

print(create_spend_chart([food, clothing]))
```

---

## 🛠️ Technologies
- Python 3
- Classes and OOP
- String manipulation

---

  ## 📄 License
This project is covered by the same license as the root repository.  
See the [LICENSE](../LICENSE) file for details.
