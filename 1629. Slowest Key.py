class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        duration = 0
        max_ = 0
        result_keys = []
        for key, dur in zip(keysPressed, releaseTimes):
            duration = dur - duration
            if max_ < duration:
                max_ = duration
                result_keys.clear()
                result_keys.append(key)
            elif max_ == duration:
                max_ = duration
                result_keys.append(key)
            duration = dur
        return sorted(result_keys)[-1]

print(Solution().slowestKey(releaseTimes = [12,23,36,46,62], keysPressed = "spuda"))