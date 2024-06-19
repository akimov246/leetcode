class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        moves = 0
        for seat, student in zip(sorted(seats), sorted(students)):
            moves += abs(seat - student)
        return moves

print(Solution().minMovesToSeat(seats = [3,1,5], students = [2,7,4]))