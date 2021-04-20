# Id : 17201053
# input: 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1

def findValue(memory, queue):
    index = 0  # initially take the lowes index #index for queue index comparison
    for i in range(3):
        try:
            qIndex = queue.index(memory[i])  # index from queue
            if qIndex > index:
                index = qIndex  # index from queue
                valueIndex = i  # index from memory
        except:
            return i  # if that value is not exist than that value should be replaceds
    return valueIndex


queue = input("Enter page numbers: ").split(" ")  # taking queue input
print()  # line gap
queLength = len(queue)
memory = ["/", "/", "/"]

hit = 0  # for hit count
while len(queue) > 0:

    # as we doing queue pop, we always geting next value at queue[0]
    if queue[0] in memory:
        print("Hit")
        hit = hit + 1  # hit count
        queue.pop(0)
        continue

    elif '-' in memory:
        posi = memory.index('-')  # grab the index where no value assigned in memory
        memory[posi] = queue[0]
    else:
        # now for replace the value from memory
        valueIndex = findValue(memory, queue[1:])  # find the index of the value,which should be replaced, from memory
        memory[valueIndex] = queue[0]  # replace

    print(memory)
    queue.pop(0)  # pop a task after finishing

print("Hit :", hit)
print("fault :", queLength - hit)





