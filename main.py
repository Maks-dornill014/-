from datetime import datetime

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = datetime.strptime(deadline, '%Y-%m-%d')
        self.completed = False

    def mark_as_completed(self):
        
        self.completed = True

    def __str__(self):
        
        status = "Виконано" if self.completed else "Не виконано"
        return f"Назва: {self.title}\nОпис: {self.description}\nДедлайн: {self.deadline.strftime('%Y-%m-%d')}\nСтан: {status}"


class TaskManager:
    def __init__(self):
        
        self.tasks = []

    def add_task(self, title, description, deadline):
       
        try:
            task = Task(title, description, deadline)
            self.tasks.append(task)
            print(f"Завдання '{title}' успішно додано!")
        except ValueError:
            print("Помилка: Некоректний формат дати. Використовуйте 'YYYY-MM-DD'.")

    def remove_task(self, title):
        
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Завдання '{title}' видалено!")
                return
        print(f"Завдання з назвою '{title}' не знайдено!")

    def mark_task_as_completed(self, title):
        
        for task in self.tasks:
            if task.title == title:
                task.mark_as_completed()
                print(f"Завдання '{title}' відмічено як виконане!")
                return
        print(f"Завдання з назвою '{title}' не знайдено!")

    def list_tasks(self):
        
        if not self.tasks:
            print("Список завдань порожній.")
        else:
            print("Список завдань:")
            for i, task in enumerate(self.tasks, 1):
                print(f"\nЗавдання {i}:")
                print(task)



if __name__ == "__main__":
    manager = TaskManager()

    
    manager.add_task("Вивчити Python", "Пройти курс з основ Python", "2024-12-31")
    manager.add_task("Сходити в магазин", "Купити продукти до вечері", "2024-12-15")

    
    manager.list_tasks()

    manager.mark_task_as_completed("Вивчити Python")

   
    manager.remove_task("Сходити в магазин")

    
    manager.list_tasks()
