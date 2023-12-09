import random
import time

def warmStack(t : list[int]) -> list[int]:
    ans = []
    left = 0
    right = 0
    while left < len(t):
        if right == len(t):
            ans.append(0)
            left += 1
            right = left
            print(len(ans))
        elif t[left] < t[right]:
            ans.append(right - left)
            left += 1
            right = left
            print(len(ans))
        else:
            right += 1
    return ans


def temp_stack(t: list[int]) -> list[int]:
    ans = []
    stack = []
    for i in range(len(t) - 1, -1, -1):
        if stack:
            while True:
                if stack[-1][0] > t[i]:
                    ans.append(stack[-1][1] - i)
                    stack.append((t[i], i))
                    break
                else:
                    stack.pop()
                    if not stack:
                        ans.append(0)
                        stack.append((t[i], i))
                        break
        else:
            ans.append(0)
            stack.append((t[i], i))
    return ans[::-1]

t = [random.randint(0, 30) for _ in range(1000_000)]
#t = [13, 12, 15, 11, 9, 12, 16, 1]
print(t[:100])
start = time.perf_counter()
#print(warmStack(t))
print(temp_stack(t)[:100])
print(time.perf_counter() - start)