import java.util.*;

class Book {
    int id;
    String title;
    String author;
    boolean isAvailable;

    Book(int id, String title, String author) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.isAvailable = true;
    }

    void display() {
        System.out.println(id + ". " + title + " - " + author + 
            (isAvailable ? " [Қолжетімді]" : " [Берілген]"));
    }
}

class User {
    int id;
    String name;

    User(int id, String name) {
        this.id = id;
        this.name = name;
    }
}

class Library {
    List<Book> books = new ArrayList<>();
    List<User> users = new ArrayList<>();
    Scanner sc = new Scanner(System.in);

    void addBook() {
        System.out.print("Кітап атауы: ");
        String title = sc.nextLine();
        System.out.print("Автор: ");
        String author = sc.nextLine();

        books.add(new Book(books.size() + 1, title, author));
        System.out.println("Кітап қосылды!");
    }

    void showBooks() {
        if (books.isEmpty()) {
            System.out.println("Кітап жоқ!");
            return;
        }
        for (Book b : books) {
            b.display();
        }
    }

    void registerUser() {
        System.out.print("Оқырман аты: ");
        String name = sc.nextLine();
        users.add(new User(users.size() + 1, name));
        System.out.println("Оқырман тіркелді!");
    }

    void giveBook() {
        showBooks();
        System.out.print("Кітап ID: ");
        int id = sc.nextInt();
        sc.nextLine();

        if (id <= books.size()) {
            Book b = books.get(id - 1);
            if (b.isAvailable) {
                b.isAvailable = false;
                System.out.println("Кітап берілді!");
            } else {
                System.out.println("Кітап бос емес!");
            }
        }
    }

    void returnBook() {
        showBooks();
        System.out.print("Кітап ID: ");
        int id = sc.nextInt();
        sc.nextLine();

        if (id <= books.size()) {
            Book b = books.get(id - 1);
            b.isAvailable = true;
            System.out.println("Кітап қайтарылды!");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Library lib = new Library();
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n=== КІТАПХАНА ЖҮЙЕСІ ===");
            System.out.println("1. Кітап қосу");
            System.out.println("2. Кітаптарды көру");
            System.out.println("3. Оқырман тіркеу");
            System.out.println("4. Кітап беру");
            System.out.println("5. Кітап қайтару");
            System.out.println("0. Шығу");
            System.out.print("Таңдау: ");

            int choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1 -> lib.addBook();
                case 2 -> lib.showBooks();
                case 3 -> lib.registerUser();
                case 4 -> lib.giveBook();
                case 5 -> lib.returnBook();
                case 0 -> {
                    System.out.println("Бағдарлама аяқталды.");
                    return;
                }
                default -> System.out.println("Қате таңдау!");
            }
        }
    }
}# -
