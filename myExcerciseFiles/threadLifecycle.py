#!/usr/bin/env python3
""" Two threads cooking soup """

import threading
import time

'''
To use an Object oriented approach towards creating a new thread, we can declare a new class that inherits from the Thread class of the threading module. Then, we can override its run method.
'''
class ChefOlivia(threading.Thread):

    ##Important to initialize the threading class's Thread
    def __init__(self):
        super().__init__()

    ##Override the run method of the threading.Thread class.
    def run(self):
        print('Olivia started & waiting for sausage to thaw...')
        time.sleep(3)
        print('Olivia is done cutting sausage.')

# main thread a.k.a. Barron
if __name__ == '__main__':
    print("Barron started & requesting Olivia's help.")
    olivia = ChefOlivia()

    print("Olivia alive?, ", olivia.is_alive())

    print('Barron tells Olivia to start.')
    olivia.start()
    print("Olivia alive?, ", olivia.is_alive())

    print('Barron continues cooking soup.')
    time.sleep(0.5)
    print("Olivia alive?, ", olivia.is_alive())

    print('Barron patiently waits for Olivia to finish and join...')
    olivia.join()
    print("Olivia alive?, ", olivia.is_alive())

    print('Barron and Olivia are both done!')
