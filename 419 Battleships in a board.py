'''
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
'''

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count=0
        shiplist=[]
        for i in xrange(0,len(board)):
            for j in xrange(0,len(board[i])):
                if board[i][j]=='X':
                    if self.check_for_ship(i,j,board):
                        if not self.check_list_for_ship(shiplist,i,j):
                            shiplist.append([i,j])
                            #print "ship not on list!",i,j
                            count+=1
                    else:
                        #print "ship not a part of any other!",i,j
                        count+=1
        return count
    def check_for_ship(self,i,j,board):
        
        if i>0 and board[i-1][j]=='X'or i<len(board)-1 and board[i+1][j]=='X' \
        or j>0 and board[i][j-1]=='X' or j<len(board[i])-1 and board[i][j+1]=='X':
            return True
        return False    
            
    def check_list_for_ship(self,shiplist,i,j):
        a = [i-1,j]
        b = [i+1,j]
        c = [i,j-1]
        d = [i,j+1]
        
        for f in xrange(0,len(shiplist)):
            x = shiplist[f]
            if x==a or x==b or x==c or x==d:
                shiplist[f]=[i,j]
                return True
        
        return False     