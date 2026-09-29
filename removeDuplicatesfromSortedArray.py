class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1  # points to the index where the next unique number should go

        for r in range(1, len(nums)):  # r scans through the array starting from index 1
            if nums[r] != nums[r - 1]:  # check if current number is different from previous number
                nums[l] = nums[r]  # place the unique number at index l
                l += 1  # move l to the next available position

        return l  # return the number of unique elements