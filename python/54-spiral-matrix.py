class Solution:
    # 测试用例
    # []
    # [[1]]
    # [[1,2]]
    # [[1],[2]]
    # [[1,2],[3,4]]
    # [[1, 2, 3, 4, 5],[1, 2, 3, 4, 5],[1, 2, 3, 4, 5],[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]]
    # [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    # 基本思路都是一样的
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if(not matrix): return []
        ml , mr = 0, len(matrix)-1
        nl, nr = 0, len(matrix[0])-1
        len_matrix = (mr+1)*(nr+1)
        if(len_matrix <= 1): return matrix[0]
        output = []
        circles = 1 if(mr == 1 or nr ==1) else ((min(mr,nr)+1)//2 +1)
        for i in range(circles):
            mi,ni = ml, nl
            while(ni < nr):# 1< 2-1
                if(matrix[mi][ni] != None):
                    output.append(matrix[mi][ni])
                    matrix[mi][ni] = None
                ni+=1
            while(mi < mr):# 1< 2-1
                if(matrix[mi][ni] != None):
                    output.append(matrix[mi][ni])
                    matrix[mi][ni] = None
                mi+=1
            while(ni > nl):# 1 > 0
                if(matrix[mi][ni] != None):
                    output.append(matrix[mi][ni])
                    matrix[mi][ni] = None
                ni-=1
            while(mi > ml):
                if(matrix[mi][ni] != None):
                    output.append(matrix[mi][ni])
                    matrix[mi][ni] = None
                mi-=1
            mr -= 1
            nr -= 1
            ml += 1
            nl += 1
        if(len(output) > len_matrix):
            output.pop()
        elif(len(output) < len_matrix):
            output.append(matrix[mi][ni])
        return output

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