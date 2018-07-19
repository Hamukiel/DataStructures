def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a%b)


def printArray(arr, size):
    res = ''
    for i in range(size):
        res += str(arr[i])+' '
    return res


def left_rotate(arr, d, n):
    for i in range(mdc(d, n)):
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

