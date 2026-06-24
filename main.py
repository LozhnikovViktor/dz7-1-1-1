from user_manager import add_user, remove_user, list_users

def main():
    users = {}  # Словарь для хранения пользователей
    print("🛠️ Управление пользователями")

    while True:
        print("\nДоступные команды:")
        print("• add [имя] [возраст] — добавить пользователя")
        print("• remove [имя] — удалить пользователя")
        print("• list — показать всех пользователей")
        print("• exit — выход")

        command = input("\nВведите команду: ").strip().split()

        if not command:
            print("❌ Введите команду!")
            continue

        cmd = command[0].lower()

        if cmd == "exit":
            print("👋 Выход из программы...")
            break

        elif cmd == "add":
            if len(command) < 3:
                print("❌ Использование: add [имя] [возраст]")
                continue
            name, age = command[1], command[2]
            add_user(users, name, age)

        elif cmd == "remove":
            if len(command) < 2:
                print("❌ Использование: remove [имя]")
                continue
            name = command[1]
            remove_user(users, name)

        elif cmd == "list":
            list_users(users)

        else:
            print("❌ Неизвестная команда. Доступные команды: add, remove, list, exit")

if __name__ == "__main__":
    main()
