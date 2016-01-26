def spiral(l):
    x_end = len(l[0])
    y_end = len(l)
    x_start = 0
    y_start = 0

    while (x_start < x_end and y_start < y_end):
        if x_start < x_end:
            for i in xrange(x_start, x_end):
                print l[y_start][i]
            y_start += 1
        if y_start < y_end:
            for j in xrange(y_start, y_end):
                print l[j][x_end-1]
            x_end -= 1
        if x_start < x_end:
            for i in reversed(xrange(x_start, x_end)):
                print l[y_end-1][i]
            x_start += 1
        if y_start < y_end:
            for j in reversed(xrange(y_start, y_end)):
                print l[j-1][x_end]
            y_end -= 1


l = [[1,2,3],[4,5,6],[7,8,9]]
spiral(l)

123
456
789

123698745