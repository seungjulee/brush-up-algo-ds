# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin
from random import randint

class MedianArray(object):
    def __init__(self):
        self.arr = []
        
    def insert(self, item):
        self.arr.append(item)
        self.reorder_until_median()
    
    def reorder_until_median(self):
        N = len(self.arr)
        compare_idx = N-1
        compare_val = self.arr[N-1]
        
        pivot_idx = randint(0, N-1)
        self.arr[pivot_idx], self.arr[compare_idx] =  self.arr[compare_idx], self.arr[pivot_idx]
        pivot_idx = 0
        
        for idx, val in enumerate(self.arr):
            if val > compare_val:
                self.arr[idx], self.arr[pivot_idx] = self.arr[pivot_idx], self.arr[idx]
                pivot_idx += 1
        self.arr[pivot_idx], self.arr[compare_idx] = self.arr[compare_idx], self.arr[pivot_idx]
        
        mid = len(self.arr) // 2
        if self.is_even():
            if pivot_idx >= mid + 1:
                return
            else:
                return self.reorder_until_median(, arr)
        else:
            if pivot_idx >= mid:
                return
            else:
                return self.reorder_until_median()
                
        
        
    def get_median(self):
        if len(self.arr) == 1:
            return self.arr[0]
        
        mid = len(self.arr) // 2
        if not self.is_even():
            return self.arr[mid]
        else:
            return (self.arr[mid]+self.arr[mid-1]) / 2
        
    def is_even(self):
        return len(self.arr) % 2 == 0
            
def parseInput():
    line_cnt = 0
    N = 0
    arr = MedianArray()
    for line in stdin:
        num = int(line.strip())
        if line_cnt == 0:
            N = num
        else:
            arr.insert(num)
            print arr.get_median()
        line_cnt += 1
parseInput()