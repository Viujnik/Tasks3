import random

from src.tasks_functions import create_task, set_task_status


def tasks_creater():
    flag = True
    current_user_id = str(random.randint(1000000, 9999999))
    while flag:
        choice = int(input("Для создания задачи - 1, для смены статуса - 2:\t"))
        if choice == 1:
            create_task(current_user_id)

        elif choice == 2:
            task_type = input("Введите тип задачи, статус которой вы хотите изменить:\t")
            task_id = input("Введите id задачи, статус которой вы хотите изменить:\t")
            task_status = input("Введите новый статус задачи, статус которой вы хотите изменить:\t")
            set_task_status(current_user_id, int(task_id), task_type, task_status)

        new_choice = input("Вы хотите продолжить?(y - да, иначе - любой символ):\t").lower()
        if new_choice != "y":
            flag = False

if __name__ == "__main__":
    tasks_creater()