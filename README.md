# Device Management Algorithms Simulator
This repository shows how these 3 algorithms (First Come First Serve, Shortest Seek Time First, Paging- FIFO replacement) performs scheduling.

## How to run
Using IDE run main.py
Import Scheduling module
```python
from Scheduling import utils
```
From utils find schedule function

Parameters: type, template, data
<br>type = fcfs, sstf, paging
<br>template = sequenced, raw
<br>data = None (user inputs), predefined (dataset input)

### Without Data
```python
utils.schedule(type='fcfs', template='sequenced', data=None)
```

### With Predefined Data
```python
utils.schedule(type='fcfs', template='sequenced', data={
    'request': 0,4,5,7,8,9,2,18,
})
```

## Key Features:

- Dynamic Type Selection
- FCFS, SSTF, PAGING.
- Data input method: predefine, user inputs
- Input Format includes num values separation with commas.
<br>Examples:
<br>(FCFS) 0,4,5,7,8,9,2,18, should be pairs: (arrival, cylinder)
<br>(SSTF) head = 50, requests = 34, 54, 23, 61, 75
<br>(PAGING) number of frames = 6, request = 4,5,7,2,12,7,8,15