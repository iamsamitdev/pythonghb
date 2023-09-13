import sys, platform, time

a = [1,2,3,4]
b = ['a','b','c','d']

t = tuple(zip(a,b))

print(t)
print(type(t))
print(t[0])
print(t[0][1])

a_list = []
a_tuple = ()

a_list = ["Test", "For", "Memory"]
a_tuple = ("Test", "For", "Memory")

print(sys.getsizeof(a_list), "bytes")
print(sys.getsizeof(a_tuple), "bytes")

v_list = list(range(100000001))
v_tuple = tuple(range(100000001))

# list test performance
start = time.time_ns()
for i in range(len(v_list)):
    a = v_list[i]
end = time.time_ns()
print("Total time for list:", end - start)

# tuple test performance
start = time.time_ns()
for i in range(len(v_tuple)):
    a = v_tuple[i]
end = time.time_ns()
print("Total time for tuple:", end - start)

