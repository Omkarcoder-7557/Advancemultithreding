#write a python programm for demonstating the working flow of multiple threads
import threading,time
def method1():
    print("line--4 method1 executed by {}".format(threading.current_thread().name))
    time.sleep(1)

def method2():
    print("line--7 method2 executed by {}".format(threading.current_thread().name))
    time.sleep(1)

def method3():
    print("line--12 method3 executed by {}".format(threading.current_thread().name))
    time.sleep(1)

def method4():
    print("line--16 method4 executed by {}".format(threading.current_thread().name))
    time.sleep(1)

#main programm
print("programm execution is started from {}".format(threading.current_thread().name))
print("*"*50)
t1=threading.Thread(target=method1)
t1.name="first"
t2=threading.Thread(target=method2)
t2.name="second"
t3=threading.Thread(target=method3)
t3.name="third"
t4=threading.Thread(target=method4)
t4.name="fourth"
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print("*"*50)
print("programm execution is completed {}".format(threading.current_thread().name))