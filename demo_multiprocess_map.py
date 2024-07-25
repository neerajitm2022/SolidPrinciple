import time
from multiprocessing import Pool

def get_sum_nnumbers(num):
    sum = 0
    for i in range(1000):
        sum +=i*i
    return sum



if __name__ == "__main__":
    t1 = time.time()
    result = []

    for x in range(100000):
        result.append(get_sum_nnumbers(x))
    
    print(time.time() - t1)
    #print(result)


    p = Pool(processes=2)
    t1 = time.time()
    result = p.map(get_sum_nnumbers, range(100000))
    p.close()
    p.join()
    print(time.time() - t1)
    #print(result)
