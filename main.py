users = {}
books = {}
issuedBooks = {}
issueCount = {}


# ---------------- USERS FILE ----------------

def loadUsers():
    try:
        with open("users.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    users[parts[0]] = {"password": parts[1], "role": parts[2]}
    except FileNotFoundError:
        pass


def saveUser(userName, password, role):
    with open("users.txt", "a") as file:
        file.write(f"{userName},{password},{role}\n")


# ---------------- BOOKS CSV ----------------

def loadBooks():
    try:
        with open("books.csv", "r") as file:
            for line in file:
                name, author, qty = line.strip().split(",")
                books[name] = {"author": author, "quantity": int(qty)}
    except FileNotFoundError:
        pass


def saveBooks():
    with open("books.csv", "w") as file:
        for book in books:
            file.write(f"{book},{books[book]['author']},{books[book]['quantity']}\n")


# ---------------- ISSUED CSV ----------------

def loadIssuedBooks():
    try:
        with open("issued.csv", "r") as file:
            for line in file:
                user, book = line.strip().split(",")

                if user not in issuedBooks:
                    issuedBooks[user] = []

                issuedBooks[user].append(book)
                issueCount[book] = issueCount.get(book, 0) + 1
    except FileNotFoundError:
        pass


def saveIssuedBooks():
    with open("issued.csv", "w") as file:
        for user in issuedBooks:
            for book in issuedBooks[user]:
                file.write(f"{user},{book}\n")


# ---------------- AUTH ----------------

def registorUser():
    userName = input("Enter User Name: ")

    if userName in users:
        print("Username already exists!")
        return

    password = input("Enter Password: ")
    users[userName] = {"password": password, "role": "user"}
    saveUser(userName, password, "user")
    print("Registration successful!")


def login():
    userName = input("Enter User Name: ")

    if userName not in users:
        print("User not found!")
        return

    password = input("Enter Password: ")

    if users[userName]["password"] == password:
        if users[userName]["role"] == "admin":
            adminMenu()
        else:
            userMenu(userName)
    else:
        print("Wrong password!")


# ---------------- ADMIN MENU ----------------

def adminMenu():
    while True:
        print("\n== Admin Menu ==")
        print("1. Add Book")
        print("2. View Books")
        print("3. Analytics")
        print("4. Remove Book")
        print("5. View Users")
        print("6. View Issued Books")
        print("7. Search Book")
        print("8. Update Book Quantity")
        print("9. Logout")

        choice = input("Enter Choice: ")

        if choice == "1":
            addBook()
        elif choice == "2":
            viewBooks()
        elif choice == "3":
            showAnalytics()
        elif choice == "4":
            removeBook()
        elif choice == "5":
            viewUsers()
        elif choice == "6":
            viewIssuedBooks()
        elif choice == "7":
            searchBook()
        elif choice == "8":
            updateBookQuantity()
        elif choice == '9':
            break
        else:
            print("Invalid option!")


# ---------------- USER MENU ----------------

def userMenu(userName):
    while True:
        print(f"\n== User Menu ({userName}) ==")
        print("1. View Books")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. My Issued Books")
        print("6. Logout")

        choice = input("Enter Choice: ")

        if choice == "1":
            viewBooks()
        elif choice == "2":
            searchBook()
        elif choice == "3":
            issueBook(userName)
        elif choice == "4":
            returnBook(userName)
        elif choice == "5":
            viewMyBooks(userName)
        elif choice == "6":
            break
        else:
            print("Invalid option!")


# ---------------- BOOK FUNCTIONS ----------------

def addBook():
    bookName = input("Book Name: ")
    author = input("Author Name: ")
    quantity = int(input("Quantity: "))

    books[bookName] = {"author": author, "quantity": quantity}
    saveBooks()
    print("Book added successfully!")


def viewBooks():
    if not books:
        print("No books available!")
        return

    for book in books:
        print(book, "-", books[book]["author"], "-", books[book]["quantity"])


def removeBook():
    bookName = input("Book Name: ")

    if bookName in books:
        del books[bookName]
        saveBooks()
        print("Book removed!")
    else:
        print("Book not found!")


def searchBook():
    keyword = input("Enter book name or author: ").lower()

    for book in books:
        if keyword in book.lower() or keyword in books[book]["author"].lower():
            print(book, "-", books[book]["author"], "-", books[book]["quantity"])




def updateBookQuantity():
    bookName = input("Book Name: ")

    if bookName not in books:
        print("Book not found!")
        return

    quantity = int(input("New Quantity: "))
    books[bookName]["quantity"] = quantity
    saveBooks()
    print("Quantity updated!")



# ---------------- ISSUE / RETURN ----------------

def issueBook(userName):
    if userName not in issuedBooks:
        issuedBooks[userName] = []

    if len(issuedBooks[userName]) >= 2:
        print("Book limit reached!")
        return

    bookName = input("Book Name: ")

    if bookName not in books or books[bookName]["quantity"] == 0:
        print("Book not available!")
        return

    issuedBooks[userName].append(bookName)
    books[bookName]["quantity"] -= 1
    issueCount[bookName] = issueCount.get(bookName, 0) + 1

    saveBooks()
    saveIssuedBooks()
    print("Book issued successfully!")


def returnBook(userName):
    bookName = input("Book Name: ")

    if userName in issuedBooks and bookName in issuedBooks[userName]:
        issuedBooks[userName].remove(bookName)
        books[bookName]["quantity"] += 1

        saveBooks()
        saveIssuedBooks()
        print("Book returned!")
    else:
        print("This book was not issued to you!")


def viewMyBooks(userName):
    print(issuedBooks.get(userName, []))


# ---------------- OTHER ----------------

def viewUsers():
    for user in users:
        print(user, "-", users[user]["role"])


def viewIssuedBooks():
    for user in issuedBooks:
        print(user, "->", issuedBooks[user])


def showAnalytics():
    if not issueCount:
        print("No data for analytics!")
        return

    import matplotlib.pyplot as plt
    plt.bar(issueCount.keys(), issueCount.values())
    plt.xlabel("Books")
    plt.ylabel("Times Issued")
    plt.title("Most Issued Books")
    plt.show()


# ---------------- MAIN ----------------

def main():
    users["admin"] = {"password": "admin123", "role": "admin"}
    loadUsers()
    loadBooks()
    loadIssuedBooks()

    while True:
        print("\n=== Library Management System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            registorUser()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid option!")


main()
