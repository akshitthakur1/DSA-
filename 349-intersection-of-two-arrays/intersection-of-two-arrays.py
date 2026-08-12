class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
     l = len(nums1)
     k= len(nums2)
     t = []
     for i in range(l):
        for j in range(k):
            if nums1[i] == nums2[j]:
                if nums1[i] not in t:
                 t.append(nums1[i])
     return t        
     