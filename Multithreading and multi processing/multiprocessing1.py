## allows us to create processes that runs in parallel 
## when to use 
#1. CPU bound task.. (i.e heavy on cpu usages)
## 2. parallel execution - TO use multiple cores of the CPU 

import multiprocessing
import time 
def sq_of_num():
    for i in range(5):
        time.sleep(1)
        print(f"the sq is {i*i}")

def cube_of_num():
    for i in range(5):
        time.sleep(1.5)
        print(f"the cube is {i*i*i}")
if __name__=="__main__":

    t1=time.time()
    ## create two processes 
    p1=multiprocessing.Process(target=sq_of_num)
    p2=multiprocessing.Process(target=cube_of_num)

    p1.start()
    p2.start()

    # wait for the process to complete 
    p1.join()
    p2.join()

    finished_time=time.time()-t1
    print(finished_time)


