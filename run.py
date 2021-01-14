

import sys
import time
import importlib
start_time = time.time()
importlib.import_module(sys.argv[1])
print("Process finished --- %s seconds ---" % (time.time() - start_time))