'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for i in range(0,n)] for k in range(0,n)]

        #matrix[0][0]=1
        current_direction=0
        x = 0
        y = 0
        for i in range(0,n*n):
            count= i+1
            print count
            turn = False

            matrix[y][x]=count

            if matrix[y][x]>0:
                turn = True

        return matrix
    def getCoordinates(self,x,y,matrix):

        return [2,2]

    def goRight(self,matrix,y,x,count):
        matrix[y][x+1]=count
    def goLeft(self,matrix,y,x,count):
        matrix[y][x-1]=count
    def goUp(self,matrix,y,x,count):
        matrix[y-1][x]=count
    def goDown(self,matrix,y,x,count):
        matrix[y+1][x]=count

    def direction(self,current_direction,matrix,y,x,n):
        if current_direction==0:
            if x<n and matrix[y][x]!=1:
                return 0
            else:
                return 1
        elif current_direction==1:
            if y<n and matrix[y][x]!=1:
                return 1
            else:
                return 2
        elif current_direction==2:
            if x>=0 and matrix[y][x]!=1:
                return 2
            else:
                return 3
        elif current_direction==3:
            if y>=0 and matrix[y][x]!=1:
                return 3
            else:
                return 1
        else:
            print "error!"

k = Solution()
print k.generateMatrix(3)
