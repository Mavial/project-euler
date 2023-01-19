import sys
import time
import importlib

print("Starting process...")
start_time = time.time()
module_name = sys.argv[1]
if "test" not in module_name:
    if module_name.endswith(".py"):
        module_name = module_name[:-3]
    if module_name.startswith("p00") and len(module_name) == 1:
        module_name = "p00" + module_name
    if not module_name.startswith("p0") and len(module_name) == 2:
        module_name = "p0" + module_name
    if not module_name.startswith("p"):
        module_name = "p" + module_name
importlib.import_module(module_name)
print("Process finished --- %s seconds ---" % (time.time() - start_time))
