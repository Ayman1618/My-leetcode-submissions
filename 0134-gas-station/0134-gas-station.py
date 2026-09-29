class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        total_tank = 0
        current_tank = 0
        start_station = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            current_tank += gain

            if current_tank < 0:
                start_station = i + 1
                current_tank = 0

        return start_station