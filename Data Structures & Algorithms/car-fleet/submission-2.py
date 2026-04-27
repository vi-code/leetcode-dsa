class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        last_fleet_time = 0
        fleets = 0
        final = [0] * len(cars)
        for i in range(len(cars)):
            t = ((target - cars[i][0])/cars[i][1])
            if t > last_fleet_time:
                last_fleet_time = t
                fleets+=1
        return fleets