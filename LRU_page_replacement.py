# Id : 17201053
# input: 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
memoryIndex = [0, 1, 2]  # to keep trac on memory which value is lastly used


# 0 means ready to replace
def lastUsedIndex(lastUsedMemoryIndex):
    if memoryIndex[lastUsedMemoryIndex] == 2:
        return

    one = memoryIndex.index(1)
    two = memoryIndex.index(2)
    memoryIndex[one] = 0
    memoryIndex[two] = 1
    memoryIndex[lastUsedMemoryIndex] = 2  # making last used value from memory, set to priority 2
    return


queue = input("Enter page numbers: ").split(" ")  # taking queue input
print()  # line gap

memory = ["/", "/", "/"]

hit = 0  # hit count
for i in queue:
    if i in memory:
        print("Hit")
        hit = hit + 1
        lastUsedIndex(memory.index(i))  # calling function to make that index as
        continue
    zero = memoryIndex.index(0)
    memory[zero] = i
    lastUsedIndex(zero)
    print(memory)

print("Hit :", hit)
print("fault :", len(queue) - hit)





