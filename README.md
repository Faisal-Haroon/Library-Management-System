# 📚 Library Management System (Python)

This project is a **command-line based Library Management System** developed in Python.
It helps manage books, users, and issued records in a simple and organized way using files.

The system supports **Admin (Librarian)** and **User (Student)** roles with different features.

---

## 🎯 Project Objective

The main goal of this project is to:

* Automate basic library operations
* Reduce manual record keeping
* Practice Python concepts like file handling, functions, dictionaries, and loops

---

## 🔐 Login & Registration

* New users can **register** with username and password
* Users can **login** after registration
* Role-based access:

  * **Admin**
  * **User**
* User data is stored in `users.txt`

---

## 👨‍🎓 User (Student) Features

* View all available books
* Search books by **name** or **author**
* Issue (borrow) a book
* Return issued book
* View own issued books
* Maximum **2 books** can be issued per user
* Logout option

---

## 👨‍💼 Admin (Librarian) Features

* Add new books
* Remove books
* Update book quantity
* View all books
* View all registered users
* View all issued books
* Search books
* View analytics (most issued books graph)
* Logout option

---

## 📊 Analytics

* Shows **most issued books**
* Bar graph visualization using **matplotlib**
* Helps identify popular books

---

## 💾 Data Storage

The project uses file handling for permanent storage:

* `users.txt` → stores users and roles
* `books.csv` → stores book name, author, quantity
* `issued.csv` → stores issued books record
* Data loads automatically when program starts
* Data updates when changes are made

---

## ⚙️ Technologies Used

* Python
* File Handling (TXT, CSV)
* Dictionaries & Lists
* Functions & Loops
* Matplotlib (for graphs)
* Command Line Interface (CLI)

---

## 📌 System Features

* Menu-driven program
* Input validation
* Book availability check
* Auto quantity update on issue/return
* Simple and clean console output

---

## 🚀 How to Run

1. Make sure Python is installed
2. Install matplotlib (if its not installed):

   ```
   pip install matplotlib
   ```
3. Run the program:

   ```
   python main.py
   ```

---

## 📈 Future Improvements

* GUI version
* Database integration
* Fine calculation for late returns
* Book categories

---

## ✅ Conclusion

This project is a beginner-friendly Python application that demonstrates real-world use of:

* File handling
* Role-based access
* Data management
* Basic analytics

It is suitable for academic projects and learning purposes.
