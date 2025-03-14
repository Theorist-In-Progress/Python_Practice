### multithreading 
import threading
import time 

def print_numbers():
    for i in range(5):
        time.sleep(2) # make this execution sleep for 2 seconds 
        print(f"number :{i}")


def print_letters():
    for ele in "abcde":
        time.sleep(2) ## suppose any I/O is happening here , we are just for the thread to become active or to complete that I/O operation and to come back to this code
        print(f'letter :{ele}')

## now while one program is waiting for I/O resources , we are waiting for this thread to become active ,
## why to wait for second program when we can run that... for this we can create a thread, ri8 now single thread is running , we can create another one 
## so that both of them are responsible for handling different programs.
## create a thread 
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)
t=time.time()
# print_letters()
# print_numbers() now instead of directly calling the function 
## start the threads 
t1.start()
t2.start()

### wait for the threads to complete 
t1.join() 
t2.join()
finished_time=time.time()-t
print(finished_time)