# try

import sys
print ('My {1[spam]} runs {0.platform}'.format(sys, {'spam':'laptop'}))
print ('My {config[spam]} runs {sys.platform}'.format(sys = sys, config = {'spam':'laptop'}))