import multiprocessing
import math
import multiprocessing.pool
import time
import sys 
#increase the maximjum number of digits for integer conversion 
sys.set_int_max_str_digits(100000)

def calculate_fact(number):
    print(f"Compute the factorial {number}")
    result=math.factorial(number)
    return result 

if __name__=="__main__":
    numbers=[20,34,15]
    start_time=time.time()

    # create a pool of workers
    with multiprocessing.Pool() as pool:
        results=pool.map(calculate_fact,numbers)
    end_time=time.time()
    print(f"results:{results}")
    print(f"time taken {end_time - start_time}")