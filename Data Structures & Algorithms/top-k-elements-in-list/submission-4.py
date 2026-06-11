class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {} 
        max_freq = - float('inf')

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
            max_freq = max(max_freq, freq_map[num])
        
        buckets = [[] for _ in range(max_freq + 1)]
        for v, f in freq_map.items():
            buckets[f].append(v)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        