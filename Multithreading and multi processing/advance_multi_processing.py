from concurrent.futures import ProcessPoolExecutor
import time 

def squares_numbers(number):
    time.sleep(1)
    return f'the number is {number*number}'


numbers=[1,2,3,4,5,12]
if __name__=='__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(squares_numbers,numbers)

    for result in results: 
        print(result)