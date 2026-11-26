# import random

# class Solution:
#     def findKthLargest(self, nums: list[int], k: int) -> int:
#         target = len(nums) - k

#         def partition(left, right):
#             pivot_idx = random.randint(left, right)
#             nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

#             pivot = nums[right]
#             i = left

#             for j in range(left, right):
#                 if nums[j] <= pivot:
#                     nums[i], nums[j] = nums[j], nums[i]
#                     i += 1

#             nums[i], nums[right] = nums[right], nums[i]
#             return i

#         left, right = 0, len(nums) - 1

#         while left <= right:
#             p = partition(left, right)

#             if p == target:
#                 return nums[p]
#             elif p < target:
#                 left = p + 1
#             else:
#                 right = p - 1


import random

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        target = len(nums) - k
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = nums[random.randint(left, right)]

            lt = left
            i = left
            gt = right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1

                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1

                else:
                    i += 1

            if target < lt:
                right = lt - 1
            elif target > gt:
                left = gt + 1
            else:
                return nums[target]