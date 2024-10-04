class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        team_skill = None
        chemistry = 0
        left = 0
        right = len(skill) - 1
        while right - left > 0:
            current = skill[left] + skill[right]
            if team_skill is None:
                team_skill = current
                chemistry += skill[left] * skill[right]
            else:
                if current == team_skill:
                    chemistry += skill[left] * skill[right]
                else:
                    return -1
            left += 1
            right -= 1
        return chemistry


print(Solution().dividePlayers(skill = [3,2,5,1,3,4]))