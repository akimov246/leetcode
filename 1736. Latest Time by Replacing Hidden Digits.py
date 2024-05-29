class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        for i, t in enumerate(time):
            if t == '?':
                if i == 0:
                    if time[i + 1] in '0123?':
                        time[i] = '2'
                    else:
                        time[i] = '1'
                elif i == 1:
                    if time[i - 1] == '2':
                        time[i] = '3'
                    else:
                        time[i] = '9'
                elif i == 3:
                    time[i] = '5'
                elif i == 4:
                    time[i] = '9'
        return ''.join(time)

#print(Solution().maximumTime(time = "2?:?0"))