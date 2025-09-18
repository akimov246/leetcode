import heapq

class TaskManager:

    def __init__(self, tasks: list[list[int]]):
        # userId, taskId, priority
        self.tid__uid_p = {tid: [uid, p] for uid, tid, p in tasks}
        self.heap = [(-p, -tid, uid) for tid, (uid, p) in self.tid__uid_p.items()]
        heapq.heapify(self.heap)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tid__uid_p[taskId] = [userId, priority]
        heapq.heappush(self.heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        uid, _ = self.tid__uid_p[taskId]
        self.tid__uid_p[taskId] = [uid, newPriority]
        heapq.heappush(self.heap, (-newPriority, -taskId, uid))

    def rmv(self, taskId: int) -> None:
        self.tid__uid_p.pop(taskId)

    def execTop(self) -> int:
        if self.tid__uid_p:
            while self.heap:
                p, tid, uid = heapq.heappop(self.heap)
                if self.tid__uid_p.get(-tid, None) == [uid, -p]:
                    self.tid__uid_p.pop(-tid)
                    return uid
        return -1

# Your TaskManager object will be instantiated and called as such:
# task_manager = TaskManager([[1,101,8],[2,102,20],[3,103,5]])
# task_manager.add(4,104,5)
# task_manager.edit(102,9)
# print(task_manager.execTop())
# task_manager.rmv(101)
# task_manager.add(50,101,8)
# print(task_manager.execTop())

task_manager = TaskManager([[9,5,8],[0,7,36]])
task_manager.rmv(7)
print(task_manager.execTop())