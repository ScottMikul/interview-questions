class twoSum:
    @staticmethod
    def getTwoSum(nums,target ):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        left = 0
        right = len(nums)-1
        nums.sort()
        while left!=right:
            sum = nums[left]+nums[right]
            if sum==0:
                result += [nums[left],nums[right]]
                left +=1
            elif sum < nums[left]:
                left +=1
            else :
                right-=1
        return result
test =[2,1,0,0,-1,-2]
print(twoSum.getTwoSum(test,0))