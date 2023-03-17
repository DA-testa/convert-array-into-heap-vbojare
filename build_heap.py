 # python3

def define_heap(data, n, i, s):
    sma = i
    leftC = 2*i+1
    rightC = 2*i+2

    if leftC < n and data[leftC] < data[sma]:
        sma = leftC
    if rightC < n and data[rightC] < data[sma]:
        sma = rightC

    if sma != i:
        data[i], data[sma] = data[sma], data[i]
        s.append((i, sma))
        define_heap(data, n, sma, s)

def build_heap(data):
    s = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    i = n // 2-1
    while i>= 0:
        define_heap(data, n, i, s)
        i = i-1

    return s


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    text = input()
    if "F" in text:
        filename = input()
        if "a" not in filename:
            path = "./tests/" + filename
            with open(path, "r") as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
    # input from keyboard
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))

   

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    s = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(s))
    for i, j in s:
        print(i, j)


if __name__ == "__main__":
    main()

