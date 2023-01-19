import sys
import time
import importlib

print("\033[32mRunning solution...\033[0m")
print("-" * 20)
start_time = time.time()
module_name = sys.argv[1]
if "test" not in module_name:
    if module_name.endswith(".py"):
        module_name = module_name[:-3]
    if not module_name.startswith("p00") and len(module_name) == 1:
        module_name = "p00" + module_name
    if not module_name.startswith("p0") and len(module_name) == 2:
        module_name = "p0" + module_name
    if not module_name.startswith("p"):
        module_name = "p" + module_name
try:
    importlib.import_module(module_name)
except ModuleNotFoundError:
    print(f"\033[31;1mModule {module_name} not found.\033[0m\n")
else:
    print("-" * 20)
    runtime = time.time() - start_time
    print(
        f"\033[32mProcess finished in --- \033[36m{runtime}\033[32m seconds ---\033[0m"
    )
    if runtime > 60:
        print(
            "\033[33mConsider optimizing: Solution doesn't meet 1 min rule for Project Euler.\033[0m"
        )
