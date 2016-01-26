import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s (%(threadName)-2s) %(message)s',)

def getItemFromSet(sema, s, key):
    logging.debug('Starting user thread')
    with sema:
        if not key in s:
            logging.debug("KEY UNAVAILABLE: \'" + key + "\' not available!")
        else:
            logging.debug("ITEM AVAILABLE: " + key)
            

def setItemFromSet(sema, s, item):
    logging.debug('Starting editor thread')
    with sema:
        logging.debug('Add A KEY: ' + item)

        if item in s:
            logging.debug('KEY ALREADY EXISTS')
        else:
            s.add(item)

def main():
    max_connections = 2
    semaphore = threading.BoundedSemaphore(max_connections)

    s = set()
    print "hel"
    u1 = threading.Thread(name='u1', target=getItemFromSet, args=(semaphore,s,'hello'))
    u2 = threading.Thread(name='u2', target=getItemFromSet, args=(semaphore,s,'hello'))
    u3 = threading.Thread(name='u3', target=getItemFromSet, args=(semaphore,s,'world'))
    u4 = threading.Thread(name='u4', target=getItemFromSet, args=(semaphore,s,'foo'))
    
    e1 = threading.Thread(name='e1', target=setItemFromSet, args=(semaphore,s,'hello'))
    e2 = threading.Thread(name='e2', target=setItemFromSet, args=(semaphore,s,'world'))
    e3 = threading.Thread(name='e3', target=setItemFromSet, args=(semaphore,s,'world'))

    e1.start()
    e2.start()
    e3.start()
    u1.start()
    u2.start()
    u3.start()
    u4.start()
    # time.sleep(2)
    

if __name__ == "__main__":
    main()