class task:
    def __init__(self , task  , status):
        self.task = task
        self.status = status


task1 = task("task1" , "pending")
task2 = task("task2" , "pending")
task3 = task("task3" , "done")

print(task1.status)
print(task2.status)
print(task3.status)