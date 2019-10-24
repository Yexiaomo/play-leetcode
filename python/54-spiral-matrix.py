class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rst = []
        if(not matrix):
            return rst
        mr = len(matrix)
        nr = len(matrix[0])
        circles = 1 if(mr == 1 or nr ==1) else (min(mr,nr)//2 +1)
        len_matrix = mr*nr
        for i in range(circles):
            ml = i
            nl = i
            while(nl < nr-1):
                rst.append(matrix[ml][nl])
                nl+=1
            while(ml < mr-1):
                rst.append(matrix[ml][nl])
                ml+=1
            while(nl > i):
                rst.append(matrix[ml][nl])
                nl-=1
            while(ml > i):
                rst.append(matrix[ml][nl])
                ml-=1
            mr -= 1
            nr -= 1
        flag = len(rst) - len_matrix
        if(flag<0):
            rst.append(matrix[ml][nl])
        elif(flag > 0):
            for i in range(flag):
                rst.pop()
        return rst