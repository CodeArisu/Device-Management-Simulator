import math as m
from Sequencing import Sequence

# FCFS device scheduling

def outputFCFSStr(items: list, head):
    # order of servicing
    output = f'{head}'
    for i in range(len(items)):
        output += f' -> {items[i]}'
    
    return output


def solveSSTF(items: list, head):
    # step 1: subtract the head to the sequence
    ischecked = False
    sequence = []
    checkedSequence = []

    if head:
        for _ in items:
            sol = abs(head - _)
            sequence.append(sol)

        isChecked = True

    # step 2: find the smallest solution
    # step 3: use the index sequence with the smallest number for the next iteration of subtraction
    pass

arr_in = []
seq = input("Enter A Sequence of Arrival Time: ").split(",")

for idx in seq:
    arr_in.append(int(idx))

if arr_in:
    head = 0
    head = int(input("Enter Head Time: "))

    print(arr_in, head)
    # print(outputFCFSStr(arr_in, head))
    dma = Sequence(head, arr_in)
    dma.inOrder("fcfs")
