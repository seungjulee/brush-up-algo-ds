import heapq

def sliding_window_max(A, w):

    heap = []
    for val in A:
        if len(heap) == w and heap[w-1] < val:
            heapq.heappop(heap)
        heapq.heappush(heap, val)

    return sorted(heap)

        