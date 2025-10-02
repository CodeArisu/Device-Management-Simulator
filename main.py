import math as m
from Scheduling import utils

# inputs:
# type = fcfs, sstf, paging
# template = sequenced, raw
# data = input, predefined

utils.schedule(
    type='paging', 
    template='sequenced'
)