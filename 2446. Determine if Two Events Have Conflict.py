class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:

        def get_range(event):
            start_h, start_m = event[0].split(':')
            start_total = int(start_h) * 60 + int(start_m)
            end_h, end_m = event[1].split(':')
            end_total = int(end_h) * 60 + int(end_m)
            return set(range(start_total, end_total + 1))

        return bool(get_range(event1) & get_range(event2))

print(Solution().haveConflict(event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]))