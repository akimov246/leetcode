class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        correct_hours, correct_minutes = correct.split(':')
        current_hours, current_minutes = current.split(':')
        correct_time = int(correct_hours) * 60 + int(correct_minutes)
        current_time = int(current_hours) * 60 + int(current_minutes)
        operations = 0
        diff_time = correct_time - current_time
        while diff_time:
            if diff_time // 60:
                diff_time -= 60
            elif diff_time // 15:
                diff_time -= 15
            elif diff_time // 5:
                diff_time -= 5
            else:
                diff_time -= 1
            operations += 1

        return operations

print(Solution().convertTime(current = "02:30", correct = "04:35"))