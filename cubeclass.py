from random import choice
import algs


class Cube:


    def __init__(self):
        self.solved_state = [[0,0,0,0], [1,1,1,1], [2,2,2,2],
                             [3,3,3,3], [4,4,4,4], [5,5,5,5]]
        self.state = self.solved_state


    def reset(self):
        self.state = self.solved_state


    def scramble(self):
        self.state = self.solved_state
        functions = [self.u_turn, self.u_prime_turn, 
                     self.r_turn, self.r_prime_turn, 
                     self.f_turn, self.f_prime_turn, 
                     self.l_turn, self.l_prime_turn, 
                     self.d_turn, self.d_prime_turn, 
                     self.b_turn, self.b_prime_turn]
        for _ in range(25):
            choice(functions)()


    def u_turn(self):
        self.state = [[self.state[0][3], self.state[0][0], self.state[0][1], self.state[0][2]], 
                      [self.state[2][0], self.state[2][1], self.state[1][2], self.state[1][3]],
                      [self.state[3][0], self.state[3][1], self.state[2][2], self.state[2][3]],
                      [self.state[4][0], self.state[4][1], self.state[3][2], self.state[3][3]],
                      [self.state[1][0], self.state[1][1], self.state[4][2], self.state[4][3]],
                      [self.state[5][0], self.state[5][1], self.state[5][2], self.state[5][3]]]


    def r_turn(self):
        self.state = [[self.state[0][0], self.state[1][1], self.state[1][2], self.state[0][3]],
                      [self.state[1][0], self.state[5][1], self.state[5][2], self.state[1][3]],
                      [self.state[2][3], self.state[2][0], self.state[2][1], self.state[2][2]],
                      [self.state[0][2], self.state[3][1], self.state[3][2], self.state[0][1]],
                      [self.state[4][0], self.state[4][1], self.state[4][2], self.state[4][3]],
                      [self.state[5][0], self.state[3][3], self.state[3][0], self.state[5][3]]]


    def f_turn(self):
        self.state = [[self.state[0][0], self.state[0][1], self.state[4][1], self.state[4][2]],
                      [self.state[1][3], self.state[1][0], self.state[1][1], self.state[1][2]],
                      [self.state[0][3], self.state[2][1], self.state[2][2], self.state[0][2]],
                      [self.state[3][0], self.state[3][1], self.state[3][2], self.state[3][3]],
                      [self.state[4][0], self.state[5][0], self.state[5][1], self.state[4][3]],
                      [self.state[2][3], self.state[2][0], self.state[5][2], self.state[5][3]]]


    def b_turn(self):
        self.state = [[self.state[2][1], self.state[2][2], self.state[0][2], self.state[0][3]],
                      [self.state[1][0], self.state[1][1], self.state[1][2], self.state[1][3]],
                      [self.state[2][0], self.state[5][2], self.state[5][3], self.state[2][3]],
                      [self.state[3][3], self.state[3][0], self.state[3][1], self.state[3][2]],
                      [self.state[0][1], self.state[4][1], self.state[4][2], self.state[0][0]],
                      [self.state[5][0], self.state[5][1], self.state[4][3], self.state[4][0]]]


    def l_turn(self):
        self.state = [[self.state[3][2], self.state[0][1], self.state[0][2], self.state[3][1]],
                      [self.state[0][0], self.state[1][1], self.state[1][2], self.state[0][3]],
                      [self.state[2][0], self.state[2][1], self.state[2][2], self.state[2][3]],
                      [self.state[3][0], self.state[5][3], self.state[5][0], self.state[3][3]],
                      [self.state[4][3], self.state[4][0], self.state[4][1], self.state[4][2]],
                      [self.state[1][0], self.state[5][1], self.state[5][2], self.state[1][3]]]


    def d_turn(self):
        self.state = [[self.state[0][0], self.state[0][1], self.state[0][2], self.state[0][3]],
                      [self.state[1][0], self.state[1][1], self.state[4][2], self.state[4][3]],
                      [self.state[2][0], self.state[2][1], self.state[1][2], self.state[1][3]],
                      [self.state[3][0], self.state[3][1], self.state[2][2], self.state[2][3]],
                      [self.state[4][0], self.state[4][1], self.state[3][2], self.state[3][3]],
                      [self.state[5][3], self.state[5][0], self.state[5][1], self.state[5][2]]]


    def x_rotation(self):
        self.state = [[self.state[1][0], self.state[1][1], self.state[1][2], self.state[1][3]],
                      [self.state[5][0], self.state[5][1], self.state[5][2], self.state[5][3]],
                      [self.state[2][3], self.state[2][0], self.state[2][1], self.state[2][2]],
                      [self.state[0][2], self.state[0][3], self.state[0][0], self.state[0][1]],
                      [self.state[4][1], self.state[4][2], self.state[4][3], self.state[4][0]],
                      [self.state[3][2], self.state[3][3], self.state[3][0], self.state[3][1]]]


    def y_rotation(self):
        self.state = [[self.state[0][3], self.state[0][0], self.state[0][1], self.state[0][2]],
                      [self.state[2][0], self.state[2][1], self.state[2][2], self.state[2][3]],
                      [self.state[3][0], self.state[3][1], self.state[3][2], self.state[3][3]],
                      [self.state[4][0], self.state[4][1], self.state[4][2], self.state[4][3]],
                      [self.state[1][0], self.state[1][1], self.state[1][2], self.state[1][3]],
                      [self.state[5][1], self.state[5][2], self.state[5][3], self.state[5][0]]]


    def z_rotation(self):
        self.state = [[self.state[4][3], self.state[4][0], self.state[4][1], self.state[4][2]],
                      [self.state[1][3], self.state[1][0], self.state[1][1], self.state[1][2]],
                      [self.state[0][3], self.state[0][0], self.state[0][1], self.state[0][2]],
                      [self.state[3][1], self.state[3][2], self.state[3][3], self.state[3][0]],
                      [self.state[5][3], self.state[5][0], self.state[5][1], self.state[5][2]],
                      [self.state[2][3], self.state[2][0], self.state[2][1], self.state[2][2]]]


    def u_prime_turn(self):
        self.state = [[self.state[0][1], self.state[0][2], self.state[0][3], self.state[0][0]],
                      [self.state[4][0], self.state[4][1], self.state[1][2], self.state[1][3]],
                      [self.state[1][0], self.state[1][1], self.state[2][2], self.state[2][3]],
                      [self.state[2][0], self.state[2][1], self.state[3][2], self.state[3][3]],
                      [self.state[3][0], self.state[3][1], self.state[4][2], self.state[4][3]],
                      [self.state[5][0], self.state[5][1], self.state[5][2], self.state[5][3]]]


    def r_prime_turn(self):
        self.state = [[self.state[0][0], self.state[3][3], self.state[3][0], self.state[0][3]],
                      [self.state[1][0], self.state[0][1], self.state[0][2], self.state[1][3]],
                      [self.state[2][1], self.state[2][2], self.state[2][3], self.state[2][0]],
                      [self.state[5][2], self.state[3][1], self.state[3][2], self.state[5][1]],
                      [self.state[4][0], self.state[4][1], self.state[4][2], self.state[4][3]],
                      [self.state[5][0], self.state[1][1], self.state[1][2], self.state[5][3]]]


    def f_prime_turn(self):
        self.state = [[self.state[0][0], self.state[0][1], self.state[2][3], self.state[2][0]],
                      [self.state[1][1], self.state[1][2], self.state[1][3], self.state[1][0]],
                      [self.state[5][1], self.state[2][1], self.state[2][2], self.state[5][0]],
                      [self.state[3][0], self.state[3][1], self.state[3][2], self.state[3][3]],
                      [self.state[4][0], self.state[0][2], self.state[0][3], self.state[4][3]],
                      [self.state[4][1], self.state[4][2], self.state[5][2], self.state[5][3]]]


    def b_prime_turn(self):
        self.state = [[self.state[4][3], self.state[4][0], self.state[0][2], self.state[0][3]],
                      [self.state[1][0], self.state[1][1], self.state[1][2], self.state[1][3]],
                      [self.state[2][0], self.state[0][0], self.state[0][1], self.state[2][3]],
                      [self.state[3][1], self.state[3][2], self.state[3][3], self.state[3][0]],
                      [self.state[5][3], self.state[4][1], self.state[4][2], self.state[5][2]],
                      [self.state[5][0], self.state[5][1], self.state[2][1], self.state[2][2]]]


    def l_prime_turn(self):
        self.state = [[self.state[1][0], self.state[0][1], self.state[0][2], self.state[1][3]],
                      [self.state[5][0], self.state[1][1], self.state[1][2], self.state[5][3]],
                      [self.state[2][0], self.state[2][1], self.state[2][2], self.state[2][3]],
                      [self.state[3][0], self.state[0][3], self.state[0][0], self.state[3][3]],
                      [self.state[4][1], self.state[4][2], self.state[4][3], self.state[4][0]],
                      [self.state[3][2], self.state[5][1], self.state[5][2], self.state[3][1]]]


    def d_prime_turn(self):
        self.state = [[self.state[0][0], self.state[0][1], self.state[0][2], self.state[0][3]],
                      [self.state[1][0], self.state[1][1], self.state[2][2], self.state[2][3]],
                      [self.state[2][0], self.state[2][1], self.state[3][2], self.state[3][3]],
                      [self.state[3][0], self.state[3][1], self.state[4][2], self.state[4][3]],
                      [self.state[4][0], self.state[4][1], self.state[1][2], self.state[1][3]],
                      [self.state[5][1], self.state[5][2], self.state[5][3], self.state[5][0]]]


    def x_prime_rotation(self):
        self.state = [[self.state[3][2], self.state[3][3], self.state[3][0], self.state[3][1]],
                      [self.state[0][0], self.state[0][1], self.state[0][2], self.state[0][3]],
                      [self.state[2][1], self.state[2][2], self.state[2][3], self.state[2][0]],
                      [self.state[5][2], self.state[5][3], self.state[5][0], self.state[5][1]],
                      [self.state[4][3], self.state[4][0], self.state[4][1], self.state[4][2]],
                      [self.state[1][0], self.state[1][1], self.state[1][2], self.state[1][3]]]


    def y_prime_rotation(self):
        self.state = [[self.state[0][1], self.state[0][2], self.state[0][3], self.state[0][0]],
                      [self.state[4][0], self.state[4][1], self.state[4][2], self.state[4][3]],
                      [self.state[1][0], self.state[1][1], self.state[1][2], self.state[1][3]],
                      [self.state[2][0], self.state[2][1], self.state[2][2], self.state[2][3]],
                      [self.state[3][0], self.state[3][1], self.state[3][2], self.state[3][3]],
                      [self.state[5][3], self.state[5][0], self.state[5][1], self.state[5][2]]]
                      

    def z_prime_rotation(self):
        self.state = [[self.state[2][1], self.state[2][2], self.state[2][3], self.state[2][0]],
                      [self.state[1][1], self.state[1][2], self.state[1][3], self.state[1][0]],
                      [self.state[5][1], self.state[5][2], self.state[5][3], self.state[5][0]],
                      [self.state[3][3], self.state[3][0], self.state[3][1], self.state[3][2]],
                      [self.state[0][1], self.state[0][2], self.state[0][3], self.state[0][0]],
                      [self.state[4][1], self.state[4][2], self.state[4][3], self.state[4][0]]]
