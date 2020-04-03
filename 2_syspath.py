import sys

print(sys.path)
print(sys.path[0])
print(sys.path[-5:])

sys.path.append("not_searched")
import path_test
path_test.found()
