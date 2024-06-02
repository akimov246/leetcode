class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        population = {}
        for log in logs:
            for year in range(*log):
                population[year] = population.get(year, 0) + 1
        population = dict(sorted(population.items(), key=lambda item: (item[1], item[0])))
        max_ = tuple(population.values())[-1]
        for p in population:
            if population[p] == max_:
                return p

print(Solution().maximumPopulation(logs = [[1950,1961],[1960,1971],[1970,1981]]))