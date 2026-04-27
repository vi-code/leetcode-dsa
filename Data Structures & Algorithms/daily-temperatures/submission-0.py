class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        unresolved = []
        days_result = [0] * len(temperatures)
        for day, temp in enumerate(temperatures):
            while unresolved and temp > temperatures[unresolved[-1]]:
                prev_index = unresolved.pop()
                days_result[prev_index] = day - prev_index
                
            unresolved.append(day)
        return days_result