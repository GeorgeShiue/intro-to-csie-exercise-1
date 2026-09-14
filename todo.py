tasks = []

def add_task(name):
    tasks.append(name)

def show_tasks():
    print("=== 待辦清單 ===")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def main():
    add_task("學習 Git")
    show_tasks()

if __name__ == "__main__":
    main()
