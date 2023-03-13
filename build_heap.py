# python3


def build_heap(data):
    n = len(data)
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    for i in range(n//2):
        if data[2*i] < data[i]:
            return swaps
    for i in range(n//2, -1, -1):
        k = i
        v = data[k]
        heap = False
        while not heap and 2*k < n-1:
            j = 2 * k +1
            if j < n - 1 and data[j] > data[j +1]:
                j +=1
            if v <= data[j]:
                heap = True
            else:
                data[k] = data[j]
                swaps.append((k,j))
                k = j
                data[k] = v

    return swaps


def heap_sort(data):
    n = len(data)
    for i in range(n-1, 0, -1):
        data[0], data[i] = data[i], data[0]
        j = 0
        k = 2 * j +1
        while k < i -1:
            if k + 1 < i - 1 and data[k +1] < data[k]:
                k +=1
            if data[k] < data[j]:
                data[j], data[k] = data[k], data[j]
                j = k
                k = 2 * j +1
            else:
                break
    return data
def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    sorted_data = heap_sort(data)
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
        print(" ".join(str(x) for x in sorted_data))


if __name__ == "__main__":
    main()
