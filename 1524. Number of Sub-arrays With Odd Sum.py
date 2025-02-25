class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod = 10 ** 9 + 7
        counter = 0
        arr = [1 if value % 2 else 0 for value in arr]
        sum_array = [arr[0]]
        current = sum_array[0]
        if current:
            num_ones = 1
            num_zeros = 0
        else:
            num_ones = 0
            num_zeros = 1
            
        for i in range(1, len(arr)):
            if current != arr[i]:
                sum_array.append(1)
                current = 1
                num_ones += 1
            else:
                sum_array.append(0)
                current = 0
                num_zeros += 1
        #print(sum_array)

        for i in range(len(arr)):
            if arr[i] == sum_array[i]:
                counter += num_ones
            else:
                counter += num_zeros

            if sum_array[i]:
                num_ones -= 1
            else:
                num_zeros -= 1

        return counter % mod


print(Solution().numOfSubarrays(arr = [1,2,3,4,5,6,7]))