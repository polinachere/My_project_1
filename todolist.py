"""
Simple To-Do List
Простой менеджер задач по планированию.
"""
# Define an empty list to store tasks
todo_list = []


def add_task(task):
    """Добавить новое дело."""
    todo_list.append(task)
    print("Задание добавлено!")


def remove_task(task_index):
    """Удалить задание из листа по его индексу."""
    try:
        task_index = int(task_index)
        if task_index >= 1 and task_index <= len(todo_list):
            removed_task = todo_list.pop(task_index - 1)
            print(f"Задание '{removed_task}' удалено!")
        else:
            print("Некорректный индекс")
    except ValueError:
        print("Некореектный индекс")


def view_tasks():
    """Посмотреть задания из списка дел."""
    if not todo_list:
        print("Нет заданий в листе.")
    else:
        print("Список дел:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def main():
    while True:
        print("\n--- СПИСОК ДЕЛ ---")
        print("1. Добавить задание")
        print("2. Удалить задание")
        print("3. Посмотреть задание")
        print("4. Выход")

        choice = input("Ваще действие (1/2/3/4): ")

        if choice == "1":
            task = input("Введите задачу: ")
            add_task(task)
        elif choice == "2":
            task_index = input("Напишите номер задания, которое нужно удалить: ")
            remove_task(task_index)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Выход.")
            break
        else:
            print("Ошибка. Попробуйте снова.")

if __name__ == "__main__":
    main()
