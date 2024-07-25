



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
