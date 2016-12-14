#from __future__ import print_function
import time
from sys import stdout
from IPython.display import clear_output

class ProgressBar: 
    def __init__(self, loop_length, finestep=False):
        self.start = time.time()
        if finestep:
            self.increment_size = 1
        else:
            self.increment_size = 100.0/loop_length
        self.curr_count = 0.0
        self.curr_pct = 0
        self.finestep = finestep
        self.loop_length = loop_length
    
    def increment(self):
        time.time()
        self.curr_count += self.increment_size
        n_bars = 20
        if self.finestep:
            bar_length = int(float(self.curr_count)/self.loop_length*n_bars)
            bar = '>'*bar_length + '-'*(n_bars-bar_length)
            print '\rLoading: '+'|'+bar+'|  '+str(round(self.curr_count/self.loop_length*100,2))+'%'+'  Elapsed time: {:0.1f} seconds'.format(time.time() - self.start),
        else:
            if int(self.curr_count) > self.curr_pct:
                self.curr_pct = int(self.curr_count)
                bar_length = int(float(self.curr_pct)/100*n_bars)
                bar = '>'*bar_length + '-'*(n_bars-bar_length)

                print '\rLoading: '+'|'+bar+'|  '+str(self.curr_pct)+'%'+'  Elapsed time: {:0.1f} seconds'.format(time.time() - self.start),
                #print('\nElapsed time: {:0.1f} seconds.\n'.format(time.time() - self.start))

    def finish(self):
        print '\rComplete! Total Elapsed time: {:0.1f} seconds                        '.format(time.time() - self.start)
