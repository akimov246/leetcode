class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        paths = dict(paths)

        def helper(path: str):
            if paths.get(path):
                return helper(paths[path])
            return path

        return helper(list(paths)[0])

print(Solution().destCity(paths = [["London","New York"],
                                   ["New York","Lima"],
                                   ["Lima","Sao Paulo"]]))