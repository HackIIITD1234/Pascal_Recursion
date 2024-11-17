def pascal(n, l = [1]):
    print(l)
    if len(l) == n:
        return l
    l_ = [1] + [l[i] + l[i+1] for i in range(len(l)-1)] + [1]
    # l_ = []
    # l_.append(l[0])
    # for i in range(len(l)):
    #     l_.append(sum(l[i:i+2]))
    return pascal(n, l_)

pascal(3)
