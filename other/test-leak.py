# This is an example script that leaks memory
#

import os
import time

queue = []

def fill_queue():
    for i in range(1000):
       queue.append(os.urandom(12313))


while True:
  fill_queue()
  time.sleep(2)
