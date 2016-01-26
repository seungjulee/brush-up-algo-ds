import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s (%(threadName)-2s) %(message)s',)

def user(cond, dic, key):
    logging.debug('Starting user thread')
    with cond:
        while not key in dic:
            logging.debug("KEY UNAVAILABLE: \'" + key + "\' not available! Waiting...")
            cond.wait()
        logging.debug("KEY AVAILABLE: " + key + ' == ' + dic[key])
            

def editor(cond, dic, key, val):
    logging.debug('Starting editor thread')
    with cond:
        logging.debug('EDIT A KEY: ' + key + ' = ' + val)
        dic[key] = val
        cond.notifyAll()

def main():
    condition = threading.Condition()

    dic = {}

    u1 = threading.Thread(name='u1', target=user, args=(condition,dic,'hello'))
    u2 = threading.Thread(name='u2', target=user, args=(condition,dic,'hello'))
    u3 = threading.Thread(name='u3', target=user, args=(condition,dic,'world'))
    
    e1 = threading.Thread(name='e1', target=editor, args=(condition,dic,'hello','world'))
    e2 = threading.Thread(name='e2', target=editor, args=(condition,dic,'world','hello'))

    u1.start()
    u2.start()
    u3.start()
    # time.sleep(2)
    e1.start()
    e2.start()

if __name__ == "__main__":
    main()