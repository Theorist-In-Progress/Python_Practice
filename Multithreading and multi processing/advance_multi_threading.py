### multithreading with advance thread pool executor
from concurrent.futures import ThreadPoolExecutor
import time 

def print_numbers(number):
    time.sleep(1)
    return f'the number is {number}'


numbers=[1,2,3,4,5,12,324,543,6232,3,234,324,34,53,64,45,6,24,4,6,546]
with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_numbers,numbers)

for result in results: 
    print(result)