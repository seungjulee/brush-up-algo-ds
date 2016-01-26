def three_sum(self, array, target):
        if len(array)<3:
            return None
        # Sort the input array first
        array=sorted(array)
        # Stores three_sum solutions
        retvalue=[]
        for i in range(len(array)):
            # Skip duplicates in input array
            if i==0 or array[i]>array[i-1]:
                # Find pair of numbers array[m], array[n], 
                # so that array[i]+array[m]+array[n] == 'target'
                ret=self.two_sum(array, -array[i], i+1, len(array)-1)
                
                # For each two_sum solution, append array[i]
                for j in range(len(ret)):
                    retvalue.append([array[i], ret[j][0], ret[j][1]])
        # Convert solution lists to array of strings
        return retvalue
​
    # Find two numbers, array[i]+array[j]==target
    def two_sum(self, array, target, i, j):
        if len(array)<2:
            return None
        array=sorted(array)
        ret=[]
        while(i<j):
            sum=array[i]+array[j]
            if sum==target:
                # Pair of numbers summing up to 'target' found
                ret.append([array[i], array[j]])
                # 'Move' i to right & j to left
                i+=1
                j-=1
                # Skip duplicates
                while i<j and array[j]==array[j+1]:
                    j-=1
                # Skip duplicates
                while i<j and array[i]==array[i-1]:
                    i+=1
            elif sum<target:
                # Pair sum smaller than 'target' so 'move' i to right
                i+=1
            else:
                # Pair sum larger than 'target' so 'move' j to left
                j-=1
        return ret
​