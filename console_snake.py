
import time
import os
import random
from pynput import keyboard
import sys
import queue


class Field():
    delay = 0.15
    field = [
        ['.','*','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','*','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
    ]

    def sleep(delay):
        time.sleep(delay)

    def dec_delay(dec):
        if (Field.delay - dec) < 0:
            pass
        else:
            Field.delay -= dec

    @staticmethod
    def view_field():
        os.system('cls')
        s = ''
        for i in range(len(Field.field)):
            for j in range(len(Field.field[0])):
                s += Field.field[i][j]
                s += '  '
            s += '\n'
        print(s)
        print('score: ', Score.score)
        Field.sleep(Field.delay)
        


class Stuff():

    stuff_coord = [0, 0]

    @staticmethod
    def make_stuff():

        is_norm = True
        while is_norm:

            x1 = int(random.uniform(1, len(Field.field) - 1))
            y1 = int(random.uniform(1, len(Field.field[0]) - 1))

            if Field.field[x1][y1] == '*':
                continue
            else:
                Field.field[x1][y1] = '*'
                Stuff.stuff_coord[0], Stuff.stuff_coord[1] = x1, y1
                is_norm = False

    @staticmethod
    def its_coord_stuff(current_soord, stuff_coord):
        if current_soord == stuff_coord:
            return True
        else:
            return False


class Snake():

    z = ['*','*']

    coord_for_seconds_move = [['just']]

    ls_for_seconds_moves = [len(z)]

    

    global_y1 = 1
    global_x1 = 1

    def dec_for_clash(func):
        def wrap(*args):
            try:
                func(*args)
            except:
                os.system('cls')
                print('YOU DIED!!!1', 'YOUR SCORE: {}\n'.format(Score.score), sep='\n')
                #input()
                sys.exit()
        return wrap

    @dec_for_clash
    def fhr(len_section, coord_kor, flag_for_seconds_or_main_foo):

        x1 = coord_kor[0]
        y1 = coord_kor[1]

        stuff = False

        if Field.field[x1][y1 + 1] == '*' and flag_for_seconds_or_main_foo:

            if Stuff.its_coord_stuff([x1, y1 + 1], Stuff.stuff_coord):
                y1 += 1
                len_section += 1
                Snake.z.append('*')
                Snake.ls_for_seconds_moves[0] = len(Snake.z)
                stuff = True
                Stuff.make_stuff()
                Score.inc_score()
            else:
                raise Exception 
        
        Field.field[x1][y1 + 1], Field.field[x1][y1 - (len_section - 1)] = Field.field[x1][y1 - (len_section - 1)], Field.field[x1][y1 + 1]
            
        if flag_for_seconds_or_main_foo:
            Snake.global_y1 += 1

        if stuff:
            Snake.global_y1 += 1

    
    @dec_for_clash
    def fhl(len_section, coord_kor, flag_for_seconds_or_main_foo):

        x1 = coord_kor[0]
        y1 = coord_kor[1]
        
        stuff = False

        if Field.field[x1][y1 - 1] == '*' and flag_for_seconds_or_main_foo:

            if Stuff.its_coord_stuff([x1, y1 - 1], Stuff.stuff_coord):
                y1 -= 1
                len_section += 1
                Snake.z.append('*')
                Snake.ls_for_seconds_moves[0] = len(Snake.z)
                stuff = True
                Stuff.make_stuff()
                Score.inc_score()
            else:
                raise Exception

        if y1 == 0:
            raise Exception

        Field.field[x1][y1 - 1], Field.field[x1][y1 + (len_section - 1)] = Field.field[x1][y1 + (len_section - 1)], Field.field[x1][y1 - 1]
            
        if flag_for_seconds_or_main_foo:
            Snake.global_y1 -= 1

        if stuff:
            Snake.global_y1 -= 1    


    @dec_for_clash
    def fvd(len_section, coord_kor, flag_for_seconds_or_main_foo):

        x1 = coord_kor[0]
        y1 = coord_kor[1]

        stuff = False

        if Field.field[x1 + 1][y1] == '*' and flag_for_seconds_or_main_foo:

            if Stuff.its_coord_stuff([x1 + 1, y1], Stuff.stuff_coord):
                x1 += 1
                len_section += 1
                Snake.z.append('*')
                Snake.ls_for_seconds_moves[0] = len(Snake.z)
                stuff = True
                Stuff.make_stuff()
                Score.inc_score()
            else:
                raise Exception

        Field.field[x1 + 1][y1], Field.field[x1 - (len_section - 1)][y1] = Field.field[x1 - (len_section - 1)][y1], Field.field[x1 + 1][y1]
            
        if flag_for_seconds_or_main_foo:
            Snake.global_x1 += 1

        if stuff:
            Snake.global_x1 += 1
    

    @dec_for_clash
    def fvu(len_section, coord_kor, flag_for_seconds_or_main_foo):

        x1 = coord_kor[0]
        y1 = coord_kor[1]

        stuff = False

        if Field.field[x1 - 1][y1] == '*' and flag_for_seconds_or_main_foo:

            if Stuff.its_coord_stuff([x1 - 1, y1], Stuff.stuff_coord):
                x1 -= 1
                len_section += 1
                Snake.z.append('*')
                Snake.ls_for_seconds_moves[0] = len(Snake.z)
                stuff = True
                Stuff.make_stuff()
                Score.inc_score()
            else:
                raise Exception

        if x1 == 0:
            raise Exception

        Field.field[x1 - 1][y1], Field.field[x1 + (len_section - 1)][y1] = Field.field[x1 + (len_section - 1)][y1], Field.field[x1 - 1][y1]
            
        if flag_for_seconds_or_main_foo:
            Snake.global_x1 -= 1

        if stuff:
            Snake.global_x1 -= 1

    def previous_coord(self, move, previous_move):

        if (move == Snake.fhr or move == Snake.fhl) and previous_move == Snake.fvd:
            Snake.coord_for_seconds_move.append([Snake.global_x1 - 1, Snake.global_y1])

        if (move == Snake.fhr or move == Snake.fhl) and previous_move == Snake.fvu:
            Snake.coord_for_seconds_move.append([Snake.global_x1 + 1, Snake.global_y1])

        if (move == Snake.fvu or move == Snake.fvd) and previous_move == Snake.fhr:
            Snake.coord_for_seconds_move.append([Snake.global_x1, Snake.global_y1 - 1])

        if (move == Snake.fvu or move == Snake.fvd) and previous_move == Snake.fhl:
            Snake.coord_for_seconds_move.append([Snake.global_x1, Snake.global_y1 + 1])
    
    def make_move(self, move):
        # проверка на то, чтобы не было поторяющихся ходов и ходов в разных направлениях
        if (Moves.dict_moves[move] != Moves.move_list[-1]) and Moves.def_opposite_move(Moves.dict_moves[move], Moves.move_list[-1]):
            move = Moves.dict_moves[move]
            Moves.move_list.append(move)

            # так как ходы вставляются в конец, то мне нужно проверить послдний и предпоследний вставленные элементы
            # чтобы правильным образом вычислить координаты где происходит поворот частей змеи
            Snake.previous_coord(self, move, Moves.move_list[-2])

            if len(Moves.move_list) == 2:
                ls_for_more_seconds_moves = Snake.ls_for_seconds_moves[0] - 1
                Snake.ls_for_seconds_moves.append(ls_for_more_seconds_moves)
                    
            else:
                ls_for_more_seconds_moves = len(Snake.z) - sum(Snake.ls_for_seconds_moves[1:]) - 1
                Snake.ls_for_seconds_moves.append(ls_for_more_seconds_moves)

        count_for_seconds_move = len(Moves.move_list)

        for i in range(len(Moves.move_list) - 1, -1, -1):
        
            ls_for_head = len(Snake.z) - sum(Snake.ls_for_seconds_moves[1:])

            if i == len(Moves.move_list) - 1:
                foo = Moves.move_list[i]
                foo(ls_for_head, [Snake.global_x1, Snake.global_y1], True) 

            else:
                # счетчик для получения длин и координат не главных секций
                count_for_seconds_move -= 1
                foo = Moves.move_list[i]
                foo(Snake.ls_for_seconds_moves[count_for_seconds_move], Snake.coord_for_seconds_move[count_for_seconds_move], False)

                if i == 0:
                    # в конце цикла проверяется длина самой последней секции, (только она декрементится) если она нулевая то удаляется все связанные с ней вещи 
                    Snake.ls_for_seconds_moves[count_for_seconds_move] -= 1

                    if Snake.ls_for_seconds_moves[count_for_seconds_move] == 0:
                        del Moves.move_list[i]
                        del Snake.coord_for_seconds_move[count_for_seconds_move]
                        del Snake.ls_for_seconds_moves[count_for_seconds_move]

class Score():
    score = len(Snake.z)
    def inc_score():
        Score.score += 1
        if not (Score.score % 5):
            Field.dec_delay(0.05)

class Moves():

    move_list = [Snake.fvd]

    dict_moves = {'d':Snake.fhr, 's':Snake.fvd, 'w':Snake.fvu, 'a':Snake.fhl}
    
    @staticmethod
    def def_opposite_move(one, two):

        op_1 = (Snake.fhr, Snake.fhl)
        op_2 = (Snake.fvu, Snake.fvd)

        if one in op_1 and two in op_1:
            return False

        if one in op_2 and two in op_2:
            return False
        
        return True

    

class Qeue():

    qeue = ['s']
    fl_for_qeue = False

    def ap_qeue(key):

        if Qeue.fl_for_qeue and Qeue.qeue[0] != key and Moves.def_opposite_move(Moves.dict_moves[key], Moves.dict_moves[Qeue.qeue[0]]):
            Qeue.qeue.insert(0, key)

        if not Qeue.fl_for_qeue and Moves.def_opposite_move(Moves.dict_moves[key], Moves.dict_moves[Qeue.qeue[0]]):
            Qeue.qeue[0] = key
            Qeue.fl_for_qeue = True
    
    def get_move(self):
        move = None
        if len(Qeue.qeue) > 1:
            move = Qeue.qeue.pop()

            if len(Qeue.qeue) == 1:
                Qeue.fl_for_qeue = False

        else:
            move = Qeue.qeue[0]
            Qeue.fl_for_qeue = False

        return move

class KeyProcess():
    def __init__(self, keyboard):
        self.listener = keyboard.Listener(on_press=KeyProcess.onPress)
        self.listener.start()

    def onPress(key):
    
        if key == keyboard.Key.up:
            Qeue.ap_qeue('w')

        if key == keyboard.Key.down:
            Qeue.ap_qeue('s')

        if key == keyboard.Key.right:
           Qeue.ap_qeue('d')

        if key == keyboard.Key.left:
            Qeue.ap_qeue('a')

 
key = KeyProcess(keyboard)  
qeue = Qeue()
snake = Snake()
Stuff.make_stuff()

while True:
    move = qeue.get_move()
    snake.make_move(move)
    Field.view_field()
    