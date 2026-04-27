class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))
        print(self.store)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        result = ""
        timeline = self.store[key]

        left, right = 0, len(timeline)-1

        while left <= right:
            mid = (left+right)//2
            if timeline[mid][0] <= timestamp:
                result = timeline[mid][1]
                left = mid+1
            else:
                right = mid-1
        return result