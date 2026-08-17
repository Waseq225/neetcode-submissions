class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        total = 0
        for start, end in customers:
            if current_time > start:
                total = total + current_time - start
            else:
                current_time = start
            total += end
            current_time += end
        
        return total/ len(customers)