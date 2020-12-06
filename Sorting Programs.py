Dataset = [3,2,7,3,8,9,4,5]
def BubbleSort(Dataset):
    unsorted = True
    x = len(Dataset)-1
    while unsorted == True:
        unsorted = False
        for i in range (0,x):
            if Dataset[i] > Dataset[i+1]:
                unsorted = True
                temp = Dataset[i]
                Dataset[i] = Dataset[i+1]
                Dataset[i+1] = temp
                print(Dataset)

def InsertionSort(Dataset):
    length = len(Dataset)
    for j in range (0,length):
        current = Dataset[j]
        pos = j
        while pos > 0 and Dataset[pos-1] > current:
            Dataset[pos] = Dataset[pos-1]
            pos = pos-1

        Dataset[pos] = current
        print(Dataset)

def MergeSort(Dataset):
    result = []
    if len(Dataset)<2:
        return Dataset
    mid = len(Dataset)//2
    y = MergeSort(Dataset[:mid])
    z = MergeSort(Dataset[mid:])
    l = 0
    j = 0
    while l < len(y) and j < len(z):
        if y[l]>z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[l])
            l += 1      
    result += y[l:]
    result += z[j:]
    return result
results = MergeSort(Dataset)
print(results)


BubbleSort(Dataset)



























    
    
