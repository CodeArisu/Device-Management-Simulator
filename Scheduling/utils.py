import re
from Scheduling.Sequencing import Scheduler

def matchCharsInputs(input_str: str):
    if not re.fullmatch(r"\s*\d+(\s*,\s*\d+)*\s*", input_str):
        raise ValueError("Invalid input format. Please enter numbers separated by commas.")
    
    return [int(x) for x in input_str.replace(" ", "").split(',')]


def mapToIntegers(input_list):
    try:
        return list(map(int, input_list))
    except ValueError:
        raise ValueError("All inputs must be integers.")


def getRequests(input_list):
    matched = matchCharsInputs(input_list)
    return mapToIntegers(matched)


def setRequests(text):
    return input(text)


def fcfsOutput(requests):
    # shows requests values
    print("Requests (arrival,cylinder):", requests)

    # initialize scheduler
    scheduler = Scheduler(requests)
        
    # run fcfs
    return scheduler.fcfs()


def sstfOutput(requests, head):
    # shows requests values
    print("Initial head position:", head, "\nRequests (cylinder):", requests)

    # initialize scheduler
    scheduler = Scheduler(requests)

    # run sstf
    return scheduler.sstf(head)


def pagingOutput(requests, num_frames):
    # shows requests values
    print("Number of frames:", num_frames, "\nRequests (page numbers):", requests)

    # initialize scheduler
    scheduler = Scheduler(requests)
        
    # run paging
    return scheduler.paging(num_frames)

def schedule(type='fcfs', template='sequenced', data=None):
    
    type = type.lower() # sets type to lowercase for consistency
    template = template.lower() # sets template to lowercase for consistency
    
    try:
        if type == 'fcfs':
            
            # if data has value, use it; otherwise, prompt for input
            if data:
                if data['requests'] is None:
                    raise ValueError("Data must include 'requests' for FCFS.")
                
                requests_input = data['requests']
                nums = getRequests(requests_input)
            else:
                requests_input = setRequests("Enter Requests (arrival,cylinder) separated by commas: ")
                nums = getRequests(requests_input)

            # pair them into (arrival, cylinder)
            requests = [(nums[i], nums[i+1]) for i in range(0, len(nums), 2)]

            # output fcfs
            order, ave_wt = fcfsOutput(requests)

            # prints output based on template
            if template == 'sequenced':
                print("Sequenced Template Selected")

                for arrival, burst, start, waiting in order:
                    print(f"Process (Arrival: {arrival}, Burst: {burst}) - Start: {start}, Waiting: {waiting}")

                print("Average Waiting Time:", ave_wt)

            else:
                print("Raw Template Selected")
                print("Service Order:", order)
                print("Average Waiting Time:", ave_wt)
        elif type == 'sstf':
            
            # if data has value, use it; otherwise, prompt for input
            if data:
                if data['requests'] is None or data['head'] is None:
                    raise ValueError("Data must include 'requests' and 'head' for SSTF.")

                head = data['head']
                requests_input = data['requests']
                requests = getRequests(requests_input)
            else:
                head = int(input("Enter initial head position: "))
                requests_input = setRequests("Enter Requests (cylinder) separated by commas: ")
                requests = getRequests(requests_input)

            # output sstf
            order, total_mv = sstfOutput(requests, head)
            
            # prints output based on template
            if template == 'sequenced':
                print("Sequenced Template Selected")
                
                sequence = ""
                for cylinder, movement in order:
                    sequence += f" -> {cylinder}"
                    print(f"Move to Cylinder: {cylinder}, Movement: {movement}")

                # prints the full sequence
                print(f"Service Sequence: {head}{sequence}")

                print("Total Head Movement:", total_mv)
            else:
                print("Raw Template Selected")
                print("Service Order:", order)
                print("Total Head Movement:", total_mv)
                
        elif type == 'paging':
            # if data has value, use it; otherwise, prompt for input
            
            if data:
                if data['requests'] is None or data['num_frames'] is None:
                    raise ValueError("Data must include 'requests' and 'num_frames' for paging.")

                num_frames = data['num_frames']
                requests_input = data['requests']
                requests = getRequests(requests_input)
            else:
                num_frames = int(input("Enter number of frames: "))
                requests_input = setRequests("Enter Requests (page numbers) separated by commas: ")
                requests = getRequests(requests_input)

            # output paging
            order, faults = pagingOutput(requests, num_frames)

            # prints output based on template
            if template == 'sequenced':
                print("Sequenced Template Selected")

                for i, memory in enumerate(order):
                    print(f"After request {i+1}: Memory State: {memory}")

                print("Total Page Faults:", faults)
            else:
                print("Raw Template Selected")
                print("Service Order:", order)
                print("Total Page Faults:", faults)
                
        elif type == None: # if type is None return error
            raise ValueError("Scheduling type must be provided, (fcfs, sstf, paging)")
        
        else: # invalid type
            raise ValueError("Unsupported scheduling type")
        
    except ValueError as ve:
        print("Error:", ve)
        return