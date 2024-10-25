class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        folder = [f.split('/') for f in folder]

        i = 0
        while i < len(folder):
            j = i + 1
            while j < len(folder):
                if folder[j][:len(folder[i])] == folder[i]:
                    folder.pop(j)
                else:
                    j += 1
            i += 1

        folder = ['/'.join(f) for f in folder]

        return folder


print(Solution().removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))