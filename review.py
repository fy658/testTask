# Review 1
def add_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

# Review Comments:
# Issue: This function uses a mutable default argument (empty list).
# Problem: In Python, default arguments are evaluated once when the function is defined,
# not each time the function is called. This can lead to unexpected behavior.
#
# Fix:
# def add_to_list(value, my_list=None):
#     if my_list is None:
#         my_list = []
#     my_list.append(value)
#     return my_list
#
# Explanation: This fix uses None as the default value and creates a new list
# if no list is provided, avoiding the shared mutable default argument issue.


# Review 2
def format_greeting(name, age):
    return "Hello, my name is {name} and I am {age} years old."

# Review Comments:
# Issue: The function is not using f-string formatting correctly.
# Problem: The current implementation will return the string with literal {name} and {age},
# not the actual values of the variables.
#
# Fix:
# def format_greeting(name, age):
#     return f"Hello, my name is {name} and I am {age} years old."
#
# Explanation: Using an f-string (note the 'f' before the opening quote) allows
# for direct embedding of variables in the string.


# Review 3
class Counter:
    count = 0

    def __init__(self):
        self.count += 1

    def get_count(self):
        return self.count

# Review Comments:
# Issue: The class is using a class variable instead of an instance variable.
# Problem: All instances of Counter will share the same 'count' variable,
# leading to incorrect counting across multiple instances.
#
# Fix:
# class Counter:
#     def __init__(self):
#         self.count = 1
#
#     def get_count(self):
#         return self.count
#
# Explanation: This fix initializes 'count' as an instance variable in __init__,
# ensuring each instance has its own counter.


# Review 4
import threading

class SafeCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

def worker(counter):
    for _ in range(1000):
        counter.increment()

counter = SafeCounter()
threads = []
for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# Review Comments:
# Issue: The SafeCounter class is not thread-safe.
# Problem: Multiple threads incrementing the counter simultaneously can lead to race conditions,
# resulting in lost updates and incorrect final count.
#
# Fix:
# import threading
#
# class SafeCounter:
#     def __init__(self):
#         self.count = 0
#         self.lock = threading.Lock()
#
#     def increment(self):
#         with self.lock:
#             self.count += 1
#
# Explanation: Adding a threading.Lock() ensures that only one thread can increment
# the counter at a time, preventing race conditions.


# Review 5
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] =+ 1
        else:
            counts[item] = 1
    return counts

# Review Comments:
# Issue: Incorrect operator used for incrementing count.
# Problem: The code uses '=+' instead of '+=', which assigns 1 to counts[item]
# instead of incrementing it.
#
# Fix:
# def count_occurrences(lst):
#     counts = {}
#     for item in lst:
#         counts[item] = counts.get(item, 0) + 1
#     return counts
#
# Explanation: This fix uses the correct '+=' operator and simplifies the logic
# using dict.get() method with a default value of 0. This also eliminates the need
# for the if-else statement.
