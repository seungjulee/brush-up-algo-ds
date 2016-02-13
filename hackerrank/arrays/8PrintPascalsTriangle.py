
def print_pascals_triangle(N):
    if N == 0:
        print 0
        return
    elif N == 1:
        print 1
        return
    elif N == 2:
        print "1 1"
        return

    print "1"
    print "1 1"
    triangle = [1,1]
    for num in xrange(2,N):
        this_line = [1]+[triangle[i]+triangle[i+1] for i,v in enumerate(triangle[:-1])]+[1]
        print " ".join(map(str,this_line))
        triangle = this_line
        


print_pascals_triangle(6)