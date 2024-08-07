class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        calendar = {'01': 31,
                    '02': 28,
                    '03': 31,
                    '04': 30,
                    '05': 31,
                    '06': 30,
                    '07': 31,
                    '08': 31,
                    '09': 30,
                    '10': 31,
                    '11': 30,
                    '12': 31}

        alice_arrive_month, alice_arrive_day = (int(value) for value in arriveAlice.split('-'))
        alice_leave_month, alice_leave_day = (int(value) for value in leaveAlice.split('-'))
        bob_arrive_month, bob_arrive_day = (int(value) for value in arriveBob.split('-'))
        bob_leave_month, bob_leave_day = (int(value) for value in leaveBob.split('-'))

        alice_start = 0
        for m in range(1, alice_arrive_month):
            alice_start += calendar[str(m).zfill(2)]
        alice_start += alice_arrive_day

        alice_end = 0
        for m in range(1, alice_leave_month):
            alice_end += calendar[str(m).zfill(2)]
        alice_end += alice_leave_day

        bob_start = 0
        for m in range(1, bob_arrive_month):
            bob_start += calendar[str(m).zfill(2)]
        bob_start += bob_arrive_day

        bob_end = 0
        for m in range(1, bob_leave_month):
            bob_end += calendar[str(m).zfill(2)]
        bob_end += bob_leave_day

        return len(set(range(alice_start, alice_end + 1)) & set(range(bob_start, bob_end + 1)))

print(Solution().countDaysTogether(arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"))