class Solution:
    def countTime(self, time: str) -> int:
        answer = 0
        questions_idxs = []
        for i in range(len(time)):
            if time[i] == '?':
                questions_idxs.append(i)
        for minute in range(1440):
            hh, mm = minute // 60, minute % 60
            strftime = list(str(str(hh).zfill(2) + ':' + str(mm).zfill(2)))
            for i in questions_idxs:
                strftime[i] = '?'
            strftime = ''.join(strftime)
            if strftime == time:
                answer += 1

        return answer

print(Solution().countTime(time = "??:??"))