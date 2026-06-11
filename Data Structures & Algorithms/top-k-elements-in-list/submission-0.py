class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {} 

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        sorted_values = sorted(freq_map.items(), key=lambda x: x[1], reverse = True)
       
        return [item[0] for item in sorted_values[:k]]
