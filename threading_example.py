import threading
import time

def print_epoch(nameOfThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "-----------", time.time())

def print_cube(num):
    print(f"Cube = {num**3}")

def print_square(num):
    print(f"Square = {num**2}")
if __name__ == "__main__":
    t1 = threading.Thread(target= print_cube, args=(2,))
    t2 = threading.Thread(target= print_square, args=(2,))
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done")
                          
