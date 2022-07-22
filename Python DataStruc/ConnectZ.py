import os
import numpy as np
import sys

class ConnectZ:
    
    def __init__(self):
        self.status = None
        
    def reset(self):
        dic = vars(self)
        for i in dic.keys():
            dic[i] = None

    def initial_checks(self, first_line, move_details):
    
        def check_1stline(first_line):
            if len(first_line) > 3:
                self.status = "8"
#             elif len(first_line) < 3:
#                 self.status = "8"
            else:
                for element in first_line:
                    for char in element:
                        if element.isalpha():
                            self.status = "8"
                            break
                        else:
                            continue
        
        def check_solvability(x,y,z):
            if z > x and z > y:
                self.status = "7"
        
        def check_moves(move_details):
            if len(move_details) == 0:
                self.status = "7"
                
        def check_length_sequence(x, y, move_details):
            size_matrix = int(x) * int(y)
            if len(move_details) > size_matrix:
                self.status = "7"
    
        def check_illegal_column(x, move_details):
            if int(max(move_details)) > x:
                self.status = "6"
    
        def check_illegal_row(x,y, move_details):
            size_matrix = int(x) * int(y)
            moves_frequency_dict = {}
            for move in move_details:
                if move not in moves_frequency_dict:
                    moves_frequency_dict[move] = 1
                else:
                    moves_frequency_dict[move] += 1
    
            for column, value in moves_frequency_dict.items():
                if value > y:
                    if size_matrix > len(move_details):
                        self.status = "5"
                    else:
                        continue
                else:
                    continue
        
        check_1stline(first_line)
        if self.status != "8":
            x,y,z = int(first_line[0]),int(first_line[1]),int(first_line[2])
            check_solvability(x,y,z)
            check_moves(move_details)
            check_length_sequence(x, y, move_details)
            check_illegal_column(x, move_details)
            check_illegal_row(x, y, move_details)

            return x,y,z
        else:
            x,y,z = None,None,None
            return x,y,z
    
    def init_matrix(self,x,y):
    
        val = [0]*(int(y)*int(x))
        matrix = np.array(val).reshape(int(y),int(x))
        return matrix  
    
    def add_moves(self, matrix, move_details):
        
        player_1_move = None
        player_2_move = None
        
        #check if game is already won
        if self.status == 1 or self.status == 2:    
            self.status = "4"
    
        for move in move_details:
            result = np.where(matrix[:,int(move)-1] == 0) #row index
            row_index = max(max(result))
            if player_1_move == None and player_2_move == None:
                matrix[:,int(move)-1][row_index] = 1
                player_1_move = False
                player_2_move = True
            elif player_1_move == False:
                matrix[:,int(move)-1][row_index] = 2
                player_1_move = True
                player_2_move = False
            elif player_1_move == True:
                matrix[:,int(move)-1][row_index] = 1
                player_1_move = False
                player_2_move = True
        
            col_index = move
            self.check_game_status(matrix, row_index, col_index, z)
            
        return matrix
    
    def check_game_status(self, matrix, row_index, col_index, z, playerlst = [1,2]):
        
        def check_player_win(matrix, row_index, col_index, z, playerlst):
            for player in playerlst:
                # check for horizontal wins
                horizontal = matrix[row_index]
                horizontal_list = np.where(horizontal == player)
                if len(horizontal_list[0]) >= z:
                    result = check_consecutive(horizontal_list[0])
                    if result == True:
                        if player == 1:
                            if self.status == "2":
                                self.status = "4"
                            else:
                                self.status = "1"
                        elif player == 2:
                            if self.status == "1":
                                self.status = "4"
                            else:
                                self.status = "2"

                # check for vertical wins
                vertical = matrix[:,int(col_index)-1]
                vertical_list = np.where(vertical == player)
                if len(vertical_list[0]) >= z:
                    result = check_consecutive(vertical_list[0])
                    if result == True:
                        if player == 1:
                            if self.status == "2":
                                self.status = "4"
                            else:
                                self.player1_win = True
                                self.status = "1"
                        elif player == 2:
                            if self.status == "1":
                                self.status = "4"
                            else:
                                self.player2_win = True
                                self.status = "2"
                
                # check for diagonal wins
                diagonal_lst = get_diagonals(matrix)
                diagonal_lst = [diagonal for diagonal in diagonal_lst if player in diagonal and len(diagonal) >= z]
                for lst in diagonal_lst:
                    lst = np.where(np.array(lst) == player)
                    if len(lst[0]) >= z:
                        result = check_consecutive(lst)
                        if result.any():
                            if player == 1:
                                self.player1_win = True
                                self.status = "1" 
                            else:
                                self.player2_win = True
                                self.status = "2"
                            break
                    else:
                        continue
         
        def get_diagonals(matrix):
            diags = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1,matrix.shape[1])]
            diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1,-matrix.shape[0],-1))
            diags = [n.tolist() for n in diags]
            return diags
    
        def check_consecutive(lst):
            n = len(lst) - 1
            return (sum(np.diff(sorted(lst)) == 1) >= n) 
        
        def check_consecutive_naive(lst):
            first_element = lst[0]
            print(first_element)
            for i in range(1,len(lst)):
                if lst[i] != first_element:
                    return []
            return lst
        
        check_player_win(matrix, row_index, col_index, z, playerlst)
                        
if __name__=="__main__":
    
    obj = ConnectZ()
    directory = "C:\\Users\\jcauchi\\Desktop\\Python Scripts\\ConnectZ\\test\\"
    if os.path.isdir(directory) == True:
        test_files = [file for file in os.listdir(directory)]
        for test_file in test_files:
            #reset class instance attributes
            obj.reset()
            with open(directory+test_file, 'r') as f:
                print(test_file)
                first_line = f.readline()
                first_line = first_line.split()

                move_details = f.read()
                move_details = move_details.split()

                x,y,z = obj.initial_checks(first_line, move_details)
                if obj.status is not None:
                    print(obj.status)
                else:
                    matrix = obj.init_matrix(x,y)
                    matrix = obj.add_moves(matrix, move_details)
                    empty_slots = np.where(matrix == 0)
                    if obj.status is None:
                        if len(empty_slots[0]) > 0:
                            if obj.status == None: 
                                print("3")
                        else:
                            if obj.status == None: 
                                print("0")
                    else:
                        print(obj.status)
    elif os.path.isdir(directory) == False:
        print(directory)
        print('9')
        
        
