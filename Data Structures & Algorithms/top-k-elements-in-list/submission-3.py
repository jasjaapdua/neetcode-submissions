class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        freq_list = [[] for _ in (range(len(nums) + 1))]

        for key, value in count.items():
            freq_list[value].append(key)
        
        i = len(freq_list) - 1
        result = []
        while i >= 0 and k > 0:
            while freq_list[i]:
                result.append(freq_list[i].pop())
                k -= 1
            i -= 1
        return result