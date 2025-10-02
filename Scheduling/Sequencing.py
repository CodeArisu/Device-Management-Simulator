from collections import deque

class Scheduler:
    def __init__(self, requests):
        self.requests = requests


    def fcfs(self):
        '''
        First-Come, First-Served Scheduling
        '''
        self.requests.sort(key=lambda x: x[0])
        
        time = 0
        waiting_time = []
        service_order = []
        
        for arrival, burst in self.requests:
            if time < arrival:
                time = arrival
                
            waiting = time - arrival
            waiting_time.append(waiting)
            
            service_order.append((arrival, burst, time, waiting))
            
            time += burst
            
        avg_waiting_time = sum(waiting_time) / len(waiting_time) if waiting_time else 0
        return service_order, avg_waiting_time


    def sstf(self, head):
        '''
        Shortest Seek Time First Scheduling
        '''
        request = self.requests[:]
        service_order = []
        total_movement = 0
        
        while request:
            minimum = min(request, key=lambda x: abs(x - head))
            
            movement = abs(minimum - head)
            
            total_movement += movement
            service_order.append((minimum, movement))
            
            head = minimum
            request.remove(minimum)
            
        return service_order, total_movement


    def paging(self, num_frames):
        '''
        Paging Scheduling
        '''
        memory = deque(maxlen=num_frames)
        page_faults = 0
        service_order = []
        
        for page in self.requests:
            if page not in memory:
                page_faults += 1
                if len(memory) == num_frames:
                    memory.popleft()
                memory.append(page)
            
            service_order.append(list(memory))
                
        return service_order, page_faults
