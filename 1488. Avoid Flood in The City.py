class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        ans = []
        zeros = []
        lakes = {}

        for i in range(len(rains)):
            lake = rains[i]
            if lake == 0:
                zeros.append(i)
                ans.append(1488)
            else:
                ans.append(-1)
                if lakes.get(lake, None) is None:
                    lakes[lake] = i
                else:
                    for z in zeros:
                        if i > z > lakes[lake]:
                            zeros.remove(z)
                            ans[z] = lake
                            lakes[lake] = i
                            break
                    else:
                        return []

        return ans


print(Solution().avoidFlood([1,1,0,0]))