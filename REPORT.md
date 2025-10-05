# ANALYSIS REPORT:

For simulation test I used pre-defined data with same requests for the sake of consistency.

```python
data = {
    'requests': "170,43,140,24,16,190",
    'head': 50,
    'num_frames': 3
}
```

## First Come First Serve
```python
utils.schedule(
    type='fcfs', 
    template='sequenced',
    data=data
)
```
### Results:
```
Requests (arrival,cylinder): [(170, 43), (140, 24), (16, 190)]
Sequenced Template Selected
Process (Arrival: 16, Burst: 190) - Start: 16, Waiting: 0
Process (Arrival: 140, Burst: 24) - Start: 206, Waiting: 66
Process (Arrival: 170, Burst: 43) - Start: 230, Waiting: 60
Average Waiting Time: 42.0
```

The Results shows the request queued where for each process has arrival

```
TurnAroundTime = Completion Time - Arrival Time
WaitingTime = TurnAroundTime - BurstTime
```

For every process arrival, burst subtract by start equals the waiting time
then averaged concluding to 42.0s.

## Shortest Seek Time First Scheduling 
```python
utils.schedule(
    type='sstf', 
    template='sequenced',
    data=data
)
```
### Results:
```
Average Waiting Time: 42.0
Initial head position: 50 
Requests (cylinder): [170, 43, 140, 24, 16, 190]
Sequenced Template Selected
Move to Cylinder: 43, Movement: 7
Move to Cylinder: 24, Movement: 19
Move to Cylinder: 16, Movement: 8
Move to Cylinder: 140, Movement: 124
Move to Cylinder: 170, Movement: 30
Move to Cylinder: 190, Movement: 20

Service Sequence: 50 -> 43 -> 24 -> 16 -> 140 -> 170 -> 190
Total Head Movement: 208
```

This process starts by subtracting the head for each processes where finding the least or minimum difference of each values then those picked difference will now be subtracted to the processes until all are sorted.

**Rm = |h - r<sub>n</sub>|**

where R is the minimum difference, h is the current head subtracted to r (requests left).

## Paging
```python
utils.schedule(
    type='paging', 
    template='sequenced',
    data=data
)
```

### Results:
```
Number of frames: 3 
Requests (page numbers): [170, 43, 140, 24, 16, 190]
Sequenced Template Selected
After request 1: Memory State: [170]
After request 2: Memory State: [170, 43]
After request 3: Memory State: [170, 43, 140]
After request 4: Memory State: [43, 140, 24]
After request 5: Memory State: [140, 24, 16]
After request 6: Memory State: [24, 16, 190]
Total Page Faults: 6
```

FIFO replacement "Frame" is the fixed-size block of the physical memory to simulate memory states and "page" replacement. Each requests is treated as a page number that must be in memory to be accessed. A CPU then requests page and it's not in **RAM** a page fault happens. At the end [24, 16, 190] is contained by the frame as these was the last 3 requests.

# Conclusion

```
Results: 

Waiting Time = 42.0
Head Movement = 208
Page Fault = 6
```

In comparison, these results isn't good for comparison as these aren't consistent solutions and isn't solving the same problems, each has pros and cons that wouldn't align with one another. It depends on what the problem is trying to be solved and how it can be solve using a specific algorithm. But for me the in terms on **Time Complexity** of the algorithm **Paging** is not time and resource extensive and does not need a lot of computations. 
