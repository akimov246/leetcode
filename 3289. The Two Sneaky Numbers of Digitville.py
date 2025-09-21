class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        sneaky_numbers = []
        sneaky_numbers_counter = 0
        number_already_was = {}

        for n in nums:
            if number_already_was.get(n, False):
                sneaky_numbers_counter += 1
                sneaky_numbers.append(n)
            else:
                number_already_was[n] = True
            if sneaky_numbers_counter == 2:
                return sneaky_numbers
        return sneaky_numbers

print(Solution().getSneakyNumbers(nums = [0,1,1,0]))