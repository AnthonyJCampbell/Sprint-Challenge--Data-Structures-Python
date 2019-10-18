import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# First idea:
# The simplest approach might be to loop over name_1 (O(n))
#   Place name into a cache (if it's not there already - to account for duplicates in the first list)
    # Loop over name_2
        # if name2 is in cache, append to duplicates

duplicates = []
cache = {}
for name_1 in names_1:
    if name_1 not in cache:
        cache[name_1] = name_1

for name_2 in names_2:
    if name_2 in cache:
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

