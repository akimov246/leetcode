import numpy

class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        #matrix = list(numpy.array(matrix).transpose())
        matrix.sort(key=self.my_sort, reverse=True)
        matrix = numpy.array(matrix)
        print(matrix)

        arr = []
        for i in range(len(matrix[0])):
            sum = 0
            for j in range(len(matrix)):
                if matrix[j, i] == 1:
                    sum += 1
                else:
                    break
            arr.append(sum)
        arr.sort()
        arr.reverse()
        print(arr)
        return max([num * i for i, num in enumerate((arr), start=1)])



    def my_sort(self, row):
        return sum([row[i] * (i + 1) for i in range(len(row))])



matrix = [[0,0,1],[1,1,1],[1,0,1]]
#matrix = [[1,0,1,0,1]]
print(Solution().largestSubmatrix(matrix))
# !!! ХЗ, короче
