class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        while sandwiches and sandwiches[0] in students:
            if students[0] != sandwiches[0]:
                students.append(students.pop(0))
            else:
                students.pop(0)
                sandwiches.pop(0)
        return len(students)

print(Solution().countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))