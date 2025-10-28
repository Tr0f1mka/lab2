import os
# import io
# import time

os.system('python -m tests.test_check_input')
print('\033[31m========================\033[0m')
print()
# time.sleep(1)

os.system('python -m tests.test_read_funcs')
print('\033[31m========================\033[0m')
print()
# time.sleep(1)

os.system('python -m tests.test_format_funcs')
print('\033[31m========================\033[0m')
print()

os.system('python -m tests.test_archive_funcs')
print('\033[31m========================\033[0m')
print()
# time.sleep(1)python -m unittest discover -s tests -p "test_*"
