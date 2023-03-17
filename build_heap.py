# python3


def define(data, n, i, s):
    sma = i
    leftC = 2 * i + 1
    rightC = 2 * i + 2

    if leftC < n and data[leftC] < data[sma]:
        sma = leftC
    if rightC < n and data[rightC] < data[sma]:
        sma = rightC

    if sma != i:
        data[i], data[sma] = data[sma], data[i]
        s.append((i, sma))
        define(data, sma, n, s)

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    i = n // 2-1
    while i >= 0:
        define(data, n, i, s)
        i = i-1
    return swaps
    


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    text = input()
    if "F" in text:
        fname = input()
        if "a" not in fname:
            path = "./tests/" + fname
            with open(path, "r") as file:
                n =nint(file.readline())
                data = list(map(int, file.readline().split()))


    # input from keyboard
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
        print(" ".join(str(x) for x in sorted_data))


if __name__ == "__main__":
    main()
