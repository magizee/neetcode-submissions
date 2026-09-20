class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1]
        suffix_products = [1]
        for i in range(1, len(nums)):
            prefix_products.append(prefix_products[i - 1] * nums[i - 1])
        for i in range(1, len(nums)):
            suffix_products.append(suffix_products[i - 1] * nums[-1 - i + 1])
        
        products = []
        for i in range(len(prefix_products)):
            products.append(prefix_products[i] * suffix_products[len(prefix_products) - i - 1])
        
        return products


        
