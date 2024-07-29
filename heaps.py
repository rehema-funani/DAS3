



import heapq

def add_numbers(numbers):
   
    heapq.heapify(numbers)
    
   
    total = 0
    
    while numbers:
        smallest_number = heapq.heappop(numbers)
        
        total += smallest_number
    
    return total

numbers = [5, 10, 15, 20]
total = add_numbers(numbers)
print(total)










def subtract_largest_from_second_smallest(numbers):
   
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers.")
    
    heapq.heapify(numbers)
    
    largest_number = heapq.heappop(numbers)
    
    second_largest_number = heapq.heappop(numbers)
    
    result = largest_number - second_largest_number
    
    return result

numbers = [5, 10, 15, 20]
result = subtract_largest_from_second_smallest(numbers)
print(result)









def multiply_all_numbers(numbers):
   
    heapq.heapify(numbers)
    
    product = 1
    
    while numbers:
        smallest_number = heapq.heappop(numbers)
        
        product *= smallest_number
    
    return product

numbers = [2, 3, 4, 5]
product = multiply_all_numbers(numbers)
print(product)






def divide_first_by_second(numbers):
   
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers.")
    
    heapq.heapify(numbers)
    
    divisor = heapq.heappop(numbers)
    
    dividend = heapq.heappop(numbers)
    
    result = dividend / divisor
    
    return result

numbers = [10, 5, 2, 1]
result = divide_first_by_second(numbers)
print(result)



import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.heap)[-1]

    def peek(self):
        return self.heap[0][-1] if self.heap else None

    def is_empty(self):
        return len(self.heap) == 0
    



def find_max(heap):
    if not heap:
        return None
    return heap[0]


def insert_max_heap(heap, element):
    heap.append(element)
    current = len(heap) - 1
    
    while current > 0 and heap[(current - 1) // 2] < heap[current]:
        heap[current], heap[(current - 1) // 2] = heap[(current - 1) // 2], heap[current]
        current = (current - 1) // 2




def build_heap(self, arr):
    self.heap = arr.copy()
    for start in range((len(arr) - 2) // 2, -1, -1):
        self._heapify_down(start)





import heapq

my_heap = []

heapq.heappush(my_heap, 10)
heapq.heappush(my_heap, 30)
heapq.heappush(my_heap, 20)
heapq.heappush(my_heap, 400)

print( my_heap)

smallest_element = heapq.heappop(my_heap)
print( smallest_element)

print( my_heap)
