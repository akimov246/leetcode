class Solution:
    def minNumberOfHours(self, initialEnergy: int,
                         initialExperience: int,
                         energy: list[int],
                         experience: list[int]) -> int:
        training = 0
        for enrg, exp in zip(energy, experience):
            if initialEnergy <= enrg:
                training += enrg - initialEnergy + 1
                initialEnergy += enrg - initialEnergy + 1
            initialEnergy -= enrg

            if initialExperience <= exp:
                training += exp - initialExperience + 1
                initialExperience += exp - initialExperience + 1
            initialExperience += exp

        return training

print(Solution().minNumberOfHours(initialEnergy = 1, initialExperience = 1, energy = [1,1,1,1], experience = [1,1,1,50]))