from random import choice


# step 1: permute colors, step 2: apply case, this covers all aufs
colors = [[0, 1, 2, 3, 4, 5],
          [0, 2, 3, 4, 1, 5],
          [0, 3, 4, 1, 2, 5],
          [0, 4, 1, 2, 3, 5]]

# ----------------------- CLL -----------------------
def s1(): 
	m = choice(colors)
	return [[m[2], m[3], m[4], 5],
	        [m[1], 5, 1, 1],
	        [m[1], 5, 4, 4],
	        [m[4], 5, 3, 3],
	        [m[3], m[2], 2, 2],
	        [0, 0, 0, 0]]

def s2(): 
	m = choice(colors)
	return [[m[2], m[1], m[4], 5],
	        [m[3], 5, 1, 1],
	        [m[1], 5, 4, 4],
	        [m[2], 5, 3, 3],
	        [m[3], m[4], 2, 2],
	        [0, 0, 0, 0]]

def s3(): 
	m = choice(colors)
	return [[m[3], m[1], m[4], 5],
	        [m[2], 5, 1, 1],
	        [m[1], 5, 4, 4],
	        [m[2], 5, 3, 3],
	        [m[4], m[3], 2, 2],
	        [0, 0, 0, 0]]

def s4(): 
	m = choice(colors)
	return [[m[1], m[3], m[4], 5],
	        [m[2], 5, 1, 1],
	        [m[1], 5, 4, 4],
	        [m[4], 5, 3, 3],
	        [m[2], m[3], 2, 2],
	        [0, 0, 0, 0]]

def s5(): 
	m = choice(colors)
	return [[m[3], m[4], m[2], 5],
	        [m[1], 5, 1, 1],
	        [m[3], 5, 4, 4],
	        [m[1], 5, 3, 3],
	        [m[4], m[2], 2, 2],
	        [0, 0, 0, 0]]

def s6(): 
	m = choice(colors)
	return [[m[4], m[3], m[1], 5],
	        [m[2], 5, 1, 1],
	        [m[2], 5, 4, 4],
	        [m[4], 5, 3, 3],
	        [m[1], m[3], 2, 2],
	        [0, 0, 0, 0]]

scll = [s1, s2, s3, s4, s5, s6]


def as1(): 
	m = choice(colors)
	return [[5, m[4], m[1], m[2]],
	        [5, m[4], 1, 1],
	        [5, m[3], 4, 4],
	        [5, m[3], 3, 3],
	        [m[2], m[1], 2, 2],
	        [0, 0, 0, 0]]

def as2(): 
	m = choice(colors)
	return [[5, m[1], m[4], m[3]],
	        [5, m[3], 1, 1],
	        [5, m[4], 4, 4],
	        [5, m[2], 3, 3],
	        [m[1], m[2], 2, 2],
	        [0, 0, 0, 0]]

def as3(): 
	m = choice(colors)
	return [[5, m[2], m[1], m[3]],
	        [5, m[4], 1, 1],
	        [5, m[1], 4, 4],
	        [5, m[4], 3, 3],
	        [m[3], m[2], 2, 2],
	        [0, 0, 0, 0]]

def as4(): 
	m = choice(colors)
	return [[5, m[2], m[3], m[1]],
	        [5, m[2], 1, 1],
	        [5, m[1], 4, 4],
	        [5, m[4], 3, 3],
	        [m[3], m[4], 2, 2],
	        [0, 0, 0, 0]]

def as5(): 
	m = choice(colors)
	return [[5, m[4], m[2], m[3]],
	        [5, m[1], 1, 1],
	        [5, m[3], 4, 4],
	        [5, m[1], 3, 3],
	        [m[4], m[2], 2, 2],
	        [0, 0, 0, 0]]

def as6(): 
	m = choice(colors)
	return [[5, m[1], m[3], m[2]],
	        [5, m[2], 1, 1],
	        [5, m[4], 4, 4],
	        [5, m[4], 3, 3],
	        [m[3], m[1], 2, 2],
	        [0, 0, 0, 0]]

ascll = [as1, as2, as3, as4, as5, as6]


def p1(): 
	m = choice(colors)
	return [[m[1], m[2], m[2], m[3]],
	        [m[4], 5, 1, 1],
	        [m[3], m[1], 4, 4],
	        [5, m[4], 3, 3],
	        [5, 5, 2, 2],
	        [0, 0, 0, 0]]

def p2(): 
	m = choice(colors)
	return [[m[1], m[4], m[2], m[1]],
	        [m[2], 5, 1, 1],
	        [m[3], m[3], 4, 4],
	        [5, m[4], 3, 3],
	        [5, 5, 2, 2],
	        [0, 0, 0, 0]]

def p3(): 
	m = choice(colors)
	return [[m[4], m[2], m[2], m[4]],
	        [m[1], 5, 1, 1],
	        [m[3], m[1], 4, 4],
	        [5, m[3], 3, 3],
	        [5, 5, 2, 2],
	        [0, 0, 0, 0]]

def p4(): 
	m = choice(colors)
	return [[m[2], m[4], m[2], m[4]],
	        [m[1], 5, 1, 1],
	        [m[3], m[3], 4, 4],
	        [5, m[1], 3, 3],
	        [5, 5, 2, 2],
	        [0, 0, 0, 0]]

def p5(): 
	m = choice(colors)
	return [[m[4], m[1], m[2], m[1]],
	        [m[2], 5, 1, 1],
	        [m[3], m[4], 4, 4],
	        [5, m[3], 3, 3],
	        [5, 5, 2, 2],
	        [0, 0, 0, 0]]

def p6(): 
	m = choice(colors)
	return [[m[3], m[2], m[3], m[4]],
	        [m[1], 5, 1, 1],
	        [m[4], m[1], 4, 4],
	        [5, m[2], 3, 3],
	        [5, 5, 2, 2],
	        [0, 0, 0, 0]]

pcll = [p1, p2, p3, p4, p5, p6]


def u1(): 
	m = choice(colors)
	return [[m[2], 5, 5, m[2]],
	        [m[3], m[4], 1, 1],
	        [m[3], m[1], 4, 4],
	        [m[4], m[1], 3, 3],
	        [5, 5, 2, 2],
	        [0, 0, 0, 0]]

def u2(): 
	m = choice(colors)
	return [[m[3], 5, 5, m[1]],
	        [m[2], m[1], 1, 1],
	        [m[4], m[4], 4, 4],
	        [m[3], m[2], 3, 3],
	        [5, 5, 2, 2],
	        [0, 0, 0, 0]]

def u3(): 
	m = choice(colors)
	return [[m[4], 5, 5, m[4]],
	        [m[1], m[3], 1, 1],
	        [m[2], m[2], 4, 4],
	        [m[1], m[3], 3, 3],
	        [5, 5, 2, 2],
	        [0, 0, 0, 0]]

def u4(): 
	m = choice(colors)
	return [[m[3], 5, 5, m[1]],
	        [m[2], m[4], 1, 1],
	        [m[3], m[1], 4, 4],
	        [m[4], m[2], 3, 3],
	        [5, 5, 2, 2],
	        [0, 0, 0, 0]]

def u5(): 
	m = choice(colors)
	return [[m[3], 5, 5, m[4]],
	        [m[1], m[2], 1, 1],
	        [m[1], m[4], 4, 4],
	        [m[3], m[2], 3, 3],
	        [5, 5, 2, 2],
	        [0, 0, 0, 0]]

def u6(): 
	m = choice(colors)
	return [[m[3], 5, 5, m[4]],
	        [m[1], m[4], 1, 1],
	        [m[3], m[2], 4, 4],
	        [m[1], m[2], 3, 3],
	        [5, 5, 2, 2],
	        [0, 0, 0, 0]]

ucll = [u1, u2, u3, u4, u5, u6]


def l1(): 
	m = choice(colors)
	return [[5, m[1], 5, m[3]],
	        [5, m[4], 1, 1],
	        [m[3], 5, 4, 4],
	        [m[2], m[1], 3, 3],
	        [m[4], m[2], 2, 2],
	        [0, 0, 0, 0]]

def l2(): 
	m = choice(colors)
	return [[5, m[3], 5, m[1]],
	        [5, m[3], 1, 1],
	        [m[2], 5, 4, 4],
	        [m[4], m[2], 3, 3],
	        [m[1], m[4], 2, 2],
	        [0, 0, 0, 0]]

def l3(): 
	m = choice(colors)
	return [[5, m[4], 5, m[3]],
	        [5, m[4], 1, 1],
	        [m[3], 5, 4, 4],
	        [m[1], m[2], 3, 3],
	        [m[1], m[2], 2, 2],
	        [0, 0, 0, 0]]

def l4(): 
	m = choice(colors)
	return [[5, m[1], 5, m[4]],
	        [5, m[3], 1, 1],
	        [m[2], 5, 4, 4],
	        [m[2], m[1], 3, 3],
	        [m[4], m[3], 2, 2],
	        [0, 0, 0, 0]]

def l5(): 
	m = choice(colors)
	return [[5, m[1], 5, m[1]],
	        [5, m[3], 1, 1],
	        [m[2], 5, 4, 4],
	        [m[2], m[4], 3, 3],
	        [m[3], m[4], 2, 2],
	        [0, 0, 0, 0]]

def l6(): 
	m = choice(colors)
	return [[5, m[3], 5, m[3]],
	        [5, m[2], 1, 1],
	        [m[1], 5, 4, 4],
	        [m[4], m[1], 3, 3],
	        [m[4], m[2], 2, 2],
	        [0, 0, 0, 0]]

lcll = [l1, l2, l3, l4, l5, l6]


def t1(): 
	m = choice(colors)
	return [[m[3], 5, 5, m[2]],
	        [5, m[3], 1, 1],
	        [m[2], m[1], 4, 4],
	        [m[4], 5, 3, 3],
	        [m[4], m[1], 2, 2],
	        [0, 0, 0, 0]]

def t2(): 
	m = choice(colors)
	return [[m[4], 5, 5, m[3]],
	        [5, m[2], 1, 1],
	        [m[1], m[4], 4, 4],
	        [m[3], 5, 3, 3],
	        [m[1], m[2], 2, 2],
	        [0, 0, 0, 0]]

def t3(): 
	m = choice(colors)
	return [[m[4], 5, 5, m[2]],
	        [5, m[3], 1, 1],
	        [m[2], m[4], 4, 4],
	        [m[3], 5, 3, 3],
	        [m[1], m[1], 2, 2],
	        [0, 0, 0, 0]]

def t4(): 
	m = choice(colors)
	return [[m[1], 5, 5, m[1]],
	        [5, m[4], 1, 1],
	        [m[3], m[3], 4, 4],
	        [m[2], 5, 3, 3],
	        [m[2], m[4], 2, 2],
	        [0, 0, 0, 0]]

def t5(): 
	m = choice(colors)
	return [[m[1], 5, 5, m[1]],
	        [5, m[3], 1, 1],
	        [m[2], m[4], 4, 4],
	        [m[3], 5, 3, 3],
	        [m[2], m[4], 2, 2],
	        [0, 0, 0, 0]]

def t6(): 
	m = choice(colors)
	return [[m[2], 5, 5, m[4]],
	        [5, m[2], 1, 1],
	        [m[1], m[1], 4, 4],
	        [m[4], 5, 3, 3],
	        [m[3], m[3], 2, 2],
	        [0, 0, 0, 0]]

tcll = [t1, t2, t3, t4, t5, t6]


def h1(): 
	m = choice(colors)
	return [[m[3], m[1], m[1], m[3]],
	        [5, 5, 1, 1],
	        [m[2], m[4], 4, 4],
	        [5, 5, 3, 3],
	        [m[4], m[2], 2, 2],
	        [0, 0, 0, 0]]

def h2(): 
	m = choice(colors)
	return [[m[1], m[1], m[3], m[3]],
	        [5, 5, 1, 1],
	        [m[4], m[4], 4, 4],
	        [5, 5, 3, 3],
	        [m[2], m[2], 2, 2],
	        [0, 0, 0, 0]]

def h3(): 
	m = choice(colors)
	return [[m[1], m[3], m[4], m[4]],
	        [5, 5, 1, 1],
	        [m[1], m[2], 4, 4],
	        [5, 5, 3, 3],
	        [m[2], m[3], 2, 2],
	        [0, 0, 0, 0]]

def h4(): 
	m = choice(colors)
	return [[m[2], m[1], m[1], m[4]],
	        [5, 5, 1, 1],
	        [m[2], m[4], 4, 4],
	        [5, 5, 3, 3],
	        [m[3], m[3], 2, 2],
	        [0, 0, 0, 0]]

hcll = [h1, h2, h3, h4]
