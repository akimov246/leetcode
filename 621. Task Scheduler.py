from dataclasses import dataclass

@dataclass
class Task:

    __slots__ = ('name', 'number', 'cooldown')

    name: str
    number: int
    cooldown: int

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        intervals = 0
        tasks_left = len(tasks)
        tnc = [] # task_number_cooldown
        for task in set(tasks):
            tnc.append(Task(task, tasks.count(task), 0))
        tnc.sort(key=lambda item: item.number, reverse=True)

        while True:
            check = False
            for i, task in enumerate(tnc):
                if task.number != 0:
                    if task.cooldown == 0:
                        task.number -= 1
                        task.cooldown = n
                        tasks_left -= 1
                        intervals += 1
                        for j in range(len(tnc)):
                            if j != i and tnc[j].cooldown != 0:
                                tnc[j].cooldown -= 1
                        check = True
                        # if task.number == 0:
                        #     tnc.remove(task)
                        tnc.sort(key=lambda item: item.number, reverse=True)
                        break

            if tasks_left == 0:
                return intervals

            if not check:
                for j in range(len(tnc)):
                    if tnc[j].cooldown != 0:
                        tnc[j].cooldown -= 1
                intervals += 1


print(Solution().leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))