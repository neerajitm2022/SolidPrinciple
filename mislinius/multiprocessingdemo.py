
#import multiprocessing.process
import time
#import threading
from multiprocessing import Process
#import multithreading
import requests
class multi_thread:

    """
    Impliment multi threading by Neeraj
    """
    lst = [2,3,4,5,6]
    starttime= time.time()
   
    def get_square(self,lst):
        for i in lst:
            time.sleep(0.2)
            print(f"square : {i*i}")

    def get_cube(self,lst):
        for i in lst:
            time.sleep(0.2)
            print(f"cube : {i**3}")

    def start_thread(self):
        #thread_1 = threading.Thread(target=self.get_square,args=(self.lst,))
        thread_1 =  Process(target=self.get_square,args=(self.lst,))
        thread_2 = Process(target=self.get_cube,args=(self.lst,))
        print("Thread strat----")
        thread_1.start()
        thread_2.start()
        thread_1.join()
        thread_2.join()
        print("Thread End----")
        #print("dsadasda")

    def call_apis(self):
        response = requests.get("https://randomuser.me/api")
        print(response.status_code)
        if response.status_code == 200:
            posts = response.json()
            #print(posts)
            with open("demo.txt", 'a') as file:
                file.write(str(posts) + ('\n'))
        else:
            print('Error:', response.status_code)
            return None
        

if __name__ == '__main__':
    obj = multi_thread()

    #obj.start_thread()
    #print("Total timer is : " + str(time.time()- obj.starttime))
    for i in range(10):
        p = Process(target=obj.call_apis)
        p.start()
        p.join()

    for i in range(10):
        p = Process(target=obj.call_apis)
        p.start()
        p.join()
    
    
        #obj.call_apis()
    
    print("Total timer is : " + str(time.time()- obj.starttime))
    

