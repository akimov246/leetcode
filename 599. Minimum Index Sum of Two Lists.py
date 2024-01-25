class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        comm_strings = dict()
        for i in range(len(list1)):
            if list1[i] in list2:
                j = list2.index(list1[i])
                comm_strings.setdefault(i + j, set()).add(list1[i])
        return list(comm_strings.get(min(comm_strings.keys())))

list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
print(Solution().findRestaurant(list1, list2))