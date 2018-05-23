import time, threading
def loop():
    print(" thread %s is begin runging" %(threading.current_thread().name))
    print(" thread %s run %d" % (threading.current_thread().name,i))
    time.sleep(1)
    print(" thread %s run %d end" % (threading.current_thread().name,i))
if __name__ =='__main__':
    print(" thread %s is begin runging" %(threading.current_thread().name))
    for i in range(3):
        t=threading.Thread(target=loop,name='childThread')
        t.start()
        t.join()
    print(" thread %s is end" %(threading.current_thread().name))


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n
    print('current balance:%d'%(balance))

balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(10000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
run_thread(10)