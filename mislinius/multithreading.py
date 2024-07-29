
import time
import threading
#import multithreading
class multi_thread:

    """
    Impliment multi threading by Neeraj
    """
    lst = [2,3,4,5,6]
    starttime= time.time()
   
    def get_square(self,lst):
        for i in lst:
            time.sleep(0.5)
            print(f"square : {i*i}")

    def get_cube(self,lst):
        for i in lst:
            time.sleep(0.5)
            print(f"cube : {i**3}")

    def start_thread(self):
        thread_1 = threading.Thread(target=self.get_square,args=(self.lst,))
        thread_2 = threading.Thread(target=self.get_cube,args=(self.lst,))
        print("Thread strat----")
        thread_1.start()
        thread_2.start()
        thread_1.join()
        thread_2.join()
        print("Thread End----")
        #print("dsadasda")

obj = multi_thread()

obj.start_thread()
print("Total timer is : " + str(time.time()- obj.starttime))

