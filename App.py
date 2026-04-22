# App.py

class Book:
    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display(self):
        status = "Қолжетімді" if self.is_available else "Берілген"
        print(f"{self.id}. {self.title} - {self.author} [{status}]")


class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self):
        title = input("Кітап атауы: ")
        author = input("Автор: ")
        book = Book(len(self.books) + 1, title, author)
        self.books.append(book)
        print("✅ Кітап қосылды!")

    def show_books(self):
        if not self.books:
            print("❌ Кітап жоқ!")
            return
        for book in self.books:
            book.display()

    def register_user(self):
        name = input("Оқырман аты: ")
        user = User(len(self.users) + 1, name)
        self.users.append(user)
        print("✅ Оқырман тіркелді!")

    def give_book(self):
        self.show_books()
        try:
            book_id = int(input("Кітап ID: "))
            book = self.books[book_id - 1]
            if book.is_available:
                book.is_available = False
                print("📖 Кітап берілді!")
            else:
                print("❌ Кітап бос емес!")
        except:
            print("❌ Қате енгізу!")

    def return_book(self):
        self.show_books()
        try:
            book_id = int(input("Кітап ID: "))
            book = self.books[book_id - 1]
            book.is_available = True
            print("🔄 Кітап қайтарылды!")
        except:
            print("❌ Қате енгізу!")


def main():
    library = Library()

    while True:
        print("\n=== КІТАПХАНА ЖҮЙЕСІ ===")
        print("1. Кітап қосу")
        print("2. Кітаптарды көру")
        print("3. Оқырман тіркеу")
        print("4. Кітап беру")
        print("5. Кітап қайтару")
        print("0. Шығу")

        choice = input("Таңдау: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.show_books()
        elif choice == "3":
            library.register_user()
        elif choice == "4":
            library.give_book()
        elif choice == "5":
            library.return_book()
        elif choice == "0":
            print("👋 Бағдарлама аяқталды")
            break
        else:
            print("❌ Қате таңдау!")


if __name__ == "__main__":
    main()
