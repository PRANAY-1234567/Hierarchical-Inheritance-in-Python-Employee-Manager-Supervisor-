# 👨‍💼 Hierarchical Inheritance in Python (Employee, Manager, Supervisor)

## 📌 Description

This Python program demonstrates **Hierarchical Inheritance** in Object-Oriented Programming (OOP).
Two child classes — `Manager` and `Supervisor` — inherit common properties and methods from the parent class `Employee`.

---

## 🚀 Features

* Demonstrates **hierarchical inheritance**
* Uses `super()` method
* Shows method overriding
* Reuses common employee data

---

## 🛠️ How It Works

### 1️⃣ Parent Class – `Employee`

Contains common employee information:

* `name`
* `code`

Methods:

* `set_data()`
* `put_data()`

---

### 2️⃣ Child Class – `Manager`

Inherits from `Employee`.

Adds:

* `teamsize`

Overrides:

* `set_data()`
* `put_data()`

---

### 3️⃣ Child Class – `Supervisor`

Also inherits from `Employee`.

Adds:

* `discipline`

Overrides:

* `set_data()`
* `put_data()`

---

## 🧬 Inheritance Structure

```text
            Employee
            /      \
           /        \
      Manager    Supervisor
```

---

## 💻 Code

```python id="x7m2pl"

class Employee:
    def __init__(self):
        self.name = ""
        self.code = 0

    def set_data(self, name, code):
        self.name = name
        self.code = code

    def put_data(self):
        print("Name   :", self.name)
        print("Code   :", self.code)


class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.teamsize = 0

    def set_data(self, name, code, teamsize):
        super().set_data(name, code)
        self.teamsize = teamsize

    def put_data(self):
        super().put_data()
        print("Team   :", self.teamsize)


class Supervisor(Employee):
    def __init__(self):
        super().__init__()
        self.discipline = ""

    def set_data(self, name, code, discipline):
        super().set_data(name, code)
        self.discipline = discipline

    def put_data(self):
        super().put_data()
        print("Discipline :", self.discipline)


class Inh6:
    @staticmethod
    def main():
        manager = Manager()
        supervisor = Supervisor()

        manager.set_data("Awez Sheikh", 423, 10)
        supervisor.set_data("Nabil Khan", 877, "Civil constr.")

        print("Manager details")
        print("------------------")
        manager.put_data()

        print("\nSupervisor details")
        print("------------------")
        supervisor.put_data()


# Calling main method
Inh6.main()
```

---

## ▶️ Example Output

```id="p4x8qa"
Manager details
------------------
Name   : Awez Sheikh
Code   : 423
Team   : 10

Supervisor details
------------------
Name   : Nabil Khan
Code   : 877
Discipline : Civil constr.
```

---

## 🧠 Key Concepts

### ✔ Hierarchical Inheritance

Multiple child classes inherit from one parent class.

```text
Employee → Manager
Employee → Supervisor
```

---

### ✔ Method Overriding

Both child classes redefine:

* `set_data()`
* `put_data()`

---

### ✔ `super()` Keyword

Used to access parent class methods:

```python id="j9k3mv"
super().set_data(name, code)
```

---

## 📚 Concepts Used

* Class & Object
* Hierarchical Inheritance
* Method Overriding
* Constructor Inheritance
* `super()` method

---

## 🎯 Advantages

* Reduces code duplication
* Improves code reusability
* Organizes related classes efficiently

---

## 🔧 Future Improvements

* Add salary calculation
* Add employee ID validation
* Use constructor parameters directly
* Store multiple employees in list

---

## 📄 License

This project is open-source and free to use.

<img width="1286" height="846" alt="image" src="https://github.com/user-attachments/assets/983cd530-33bf-4aeb-9ee4-74699574dfe1" />
