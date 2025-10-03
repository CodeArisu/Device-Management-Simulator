import math as m
from Scheduling import utils

# inputs:
# type = fcfs, sstf, paging
# template = sequenced, raw
# data = input, predefined

data = {
    'requests': "170,43,140,24,16,190",
    'head': 50,
    'num_frames': 3
}

utils.schedule(
    type='fcfs', 
    template='sequenced',
    data=data
)

utils.schedule(
    type='sstf', 
    template='sequenced',
    data=data
)

utils.schedule(
    type='paging', 
    template='sequenced',
    data=data
)