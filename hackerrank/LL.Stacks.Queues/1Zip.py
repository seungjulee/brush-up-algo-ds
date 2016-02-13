#For your reference:
#LinkedListNode {
#    int val
#    LinkedListNode next
#}

def  Zip( root):
    if not root or not root.next:
        return root
    stack = []
    while root.next:
        stack.append(root)
        root = root.next
    stack.append(root)
    N = len(stack)
    first_stack = stack[:N//2]
    second_stack = list(reversed(stack[N//2:]))
    del stack[:]
    for first_item, second_item in zip(first_stack, second_stack):
        stack.append(first_stack.pop(0))
        stack.append(second_stack.pop(0))

    if second_stack:
        stack.append(second_stack.pop())
    for idx, val in enumerate(stack):
        if idx != N-1:
            val.next = stack[idx+1]
        else:
            val.next = None

    return stack[0]
    # if N % 2 == 1:
    #     is_odd = True
    # else:
    #     is_odd = False

    # for i in range(N//2):
    #     last_item = second_stack.pop()
    #     first_item = first_stack[i]
    #     first_item.next = last_item
    #     if i == N//2 - 1:
    #         if is_odd:
    #             last_item.next = second_stack[0]
    #             second_stack[0].next = None
    #         else:
    #             last_item.next = None
    #     else:
    #         last_item.next = first_stack[i+1]

    # return first_stack[0]
        
        
