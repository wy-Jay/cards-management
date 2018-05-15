import threading

local_school = threading.local()

def process_student():
    std = local_school.name
    print('hello ,name is %s (in %s)' %(std, threading.current_thread().name))

def process_thread(name):
    local_school.name = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('aaa',), name='A')
t2 = threading.Thread(target=process_thread, args=('bbb',), name='B')

t1.start()
t2.start()

t1.join()
t2.join()

