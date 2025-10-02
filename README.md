# Device Management Algorithms Simulator
This repository shows how these 3 algorithms (First Come First Serve, Shortest Seek Time First, Paging- FIFO replacement) performs scheduling.

## How to run
* Using IDE run main.py
* import Scheduling module
```python
from Scheduling import utils
```
* from utils find schedule function

* parameters: type, template, data
<br>type = fcfs, sstf, paging
<br>template = sequenced, raw
<br>data = None (user inputs), predefined (dataset input)
```python
utils.schedule(type='paging', template='sequenced', data=None)
```