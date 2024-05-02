import pygame
from sys import exit
from cubeclass import Cube
import algs
from random import choice, randint


# TODO: Add cube turning sounds
# 		Fix controls mismatch

# create an instance of our cube
cube = Cube()


# initialize pygame
pygame.init()
screen = pygame.display.set_mode((1000,800), flags=pygame.SCALED, vsync=1)
pygame.display.set_caption('2x2 Cube Trainer')
clock = pygame.time.Clock()

# create background surface
background_surface = pygame.Surface((1000,800))
background_surface.fill("White")

# -------------------- Text ------------------
title_font = pygame.font.Font("font/Pixeltype.ttf", 60)
body_font = pygame.font.Font("font/Pixeltype.ttf", 40)
body_2_font = pygame.font.SysFont("Arial", 24)

title_surface = title_font.render("Pocket Cube Simulator", False, "Black")
title_rect = title_surface.get_rect(midtop = (360,90))

scramble_pos_x, scramble_pos_y = 720+73, 400 
scramble_surf = body_font.render("Scramble", False, "White")
scramble_rect = scramble_surf.get_rect(center = (scramble_pos_x, scramble_pos_y+3))

reset_pos_x, reset_pos_y = 720+73, 475 
reset_surf = body_font.render("Reset", False, "White")
reset_rect = reset_surf.get_rect(center = (reset_pos_x, reset_pos_y+3))

cll_pos_x, cll_pos_y = 720+73, 550 
cll_surf = body_font.render("CLL Case", False, "White")
cll_rect = cll_surf.get_rect(center = (cll_pos_x, cll_pos_y+3))

controls_surface = pygame.image.load("graphics/cube-controls.png").convert()

cll_selector_x, cll_selector_y = 360, 700
cll_selector_surf = body_2_font.render("Select subsets to practice:", True, "Black")
cll_selector_rect = cll_selector_surf.get_rect(center = (cll_selector_x, cll_selector_y))
cll_labels_surf = body_2_font.render("S      AS      P      U      L      T      H", True, "Black")
cll_labels_rect = cll_labels_surf.get_rect(center = (cll_selector_x, cll_selector_y + 40))


# ----------------- Button Class ---------------
# load button images
button_img = pygame.image.load("graphics/button.png").convert_alpha()
checkbox_img = pygame.image.load("graphics/checkbox-copy.png").convert_alpha()

class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False

	def draw(self):
		action = False
		# get mouse position
		pos = pygame.mouse.get_pos()
		# check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		# draw button on screen
		screen.blit(self.image, (self.rect.x, self.rect.y))
		return action

# create button instances
scramble_button = Button(scramble_pos_x, scramble_pos_y, button_img)
reset_button = Button(reset_pos_x, reset_pos_y, button_img)
cll_button = Button(cll_pos_x, cll_pos_y, button_img)

# checkmark setup
checkmark_img = pygame.image.load("graphics/checkmark-copy.png").convert_alpha()

# don't change these values! positioning can be done by changing cll_selector_x/y on line 49
pos_s_x, pos_s_y = cll_selector_x - 153, cll_selector_y + 40
pos_as_x, pos_as_y = cll_selector_x - 82, cll_selector_y + 40
pos_p_x, pos_p_y = cll_selector_x - 23, cll_selector_y + 40
pos_u_x, pos_u_y = cll_selector_x + 36, cll_selector_y + 40
pos_l_x, pos_l_y = cll_selector_x + 90, cll_selector_y + 40
pos_t_x, pos_t_y = cll_selector_x + 145, cll_selector_y + 40
pos_h_x, pos_h_y = cll_selector_x + 204, cll_selector_y + 40

checkbox_scll = Button(pos_s_x, pos_s_y, checkbox_img)
checkbox_ascll = Button(pos_as_x, pos_as_y, checkbox_img)
checkbox_pcll = Button(pos_p_x, pos_p_y, checkbox_img)
checkbox_ucll = Button(pos_u_x, pos_u_y, checkbox_img)
checkbox_lcll = Button(pos_l_x, pos_l_y, checkbox_img)
checkbox_tcll = Button(pos_t_x, pos_t_y, checkbox_img)
checkbox_hcll = Button(pos_h_x, pos_h_y, checkbox_img)

checkmark_s_rect = checkmark_img.get_rect(center = (pos_s_x+3, pos_s_y-4))
checkmark_as_rect = checkmark_img.get_rect(center = (pos_as_x+3, pos_as_y-4))
checkmark_p_rect = checkmark_img.get_rect(center = (pos_p_x+3, pos_p_y-4))
checkmark_u_rect = checkmark_img.get_rect(center = (pos_u_x+3, pos_u_y-4))
checkmark_l_rect = checkmark_img.get_rect(center = (pos_l_x+3, pos_l_y-4))
checkmark_t_rect = checkmark_img.get_rect(center = (pos_t_x+3, pos_t_y-4))
checkmark_h_rect = checkmark_img.get_rect(center = (pos_h_x+3, pos_h_y-4))


# -------------------------Drawing Cube -----------------------------
cube_pos_x = 160
cube_pos_y = 200

cube_surface = pygame.image.load("graphics/my-cube.png").convert_alpha()

pos_00 = (cube_pos_x+122, cube_pos_y+14)
pos_01 = (cube_pos_x+245,cube_pos_y+36)
pos_02 = (cube_pos_x+157,cube_pos_y+87)
pos_03 = (cube_pos_x+30,cube_pos_y+58)

pos_10 = (cube_pos_x+17, cube_pos_y+126)
pos_11 = (cube_pos_x+142, cube_pos_y+162)
pos_12 = (cube_pos_x+152, cube_pos_y+291)
pos_13 = (cube_pos_x+32, cube_pos_y+246)

pos_20 = (cube_pos_x+283, cube_pos_y+139)
pos_21 = (cube_pos_x+346, cube_pos_y+80)
pos_22 = (cube_pos_x+342, cube_pos_y+191)
pos_23 = (cube_pos_x+283, cube_pos_y+261)

# tile surfaces
tile_00_white = pygame.image.load("graphics/tiles/00white.png").convert_alpha()
tile_00_green = pygame.image.load("graphics/tiles/00green.png").convert_alpha()
tile_00_red = pygame.image.load("graphics/tiles/00red.png").convert_alpha()
tile_00_blue = pygame.image.load("graphics/tiles/00blue.png").convert_alpha()
tile_00_orange = pygame.image.load("graphics/tiles/00orange.png").convert_alpha()
tile_00_yellow = pygame.image.load("graphics/tiles/00yellow.png").convert_alpha()
tiles_of_00 = [tile_00_white, tile_00_green, tile_00_red, tile_00_blue, tile_00_orange, tile_00_yellow]

tile_01_white = pygame.image.load("graphics/tiles/01white.png").convert_alpha()
tile_01_green = pygame.image.load("graphics/tiles/01green.png").convert_alpha()
tile_01_red = pygame.image.load("graphics/tiles/01red.png").convert_alpha()
tile_01_blue = pygame.image.load("graphics/tiles/01blue.png").convert_alpha()
tile_01_orange = pygame.image.load("graphics/tiles/01orange.png").convert_alpha()
tile_01_yellow = pygame.image.load("graphics/tiles/01yellow.png").convert_alpha()
tiles_of_01 = [tile_01_white, tile_01_green, tile_01_red, tile_01_blue, tile_01_orange, tile_01_yellow]

tile_02_white = pygame.image.load("graphics/tiles/02white.png").convert_alpha()
tile_02_green = pygame.image.load("graphics/tiles/02green.png").convert_alpha()
tile_02_red = pygame.image.load("graphics/tiles/02red.png").convert_alpha()
tile_02_blue = pygame.image.load("graphics/tiles/02blue.png").convert_alpha()
tile_02_orange = pygame.image.load("graphics/tiles/02orange.png").convert_alpha()
tile_02_yellow = pygame.image.load("graphics/tiles/02yellow.png").convert_alpha()
tiles_of_02 = [tile_02_white, tile_02_green, tile_02_red, tile_02_blue, tile_02_orange, tile_02_yellow]

tile_03_white = pygame.image.load("graphics/tiles/03white.png").convert_alpha()
tile_03_green = pygame.image.load("graphics/tiles/03green.png").convert_alpha()
tile_03_red = pygame.image.load("graphics/tiles/03red.png").convert_alpha()
tile_03_blue = pygame.image.load("graphics/tiles/03blue.png").convert_alpha()
tile_03_orange = pygame.image.load("graphics/tiles/03orange.png").convert_alpha()
tile_03_yellow = pygame.image.load("graphics/tiles/03yellow.png").convert_alpha()
tiles_of_03 = [tile_03_white, tile_03_green, tile_03_red, tile_03_blue, tile_03_orange, tile_03_yellow]

tile_10_white = pygame.image.load("graphics/tiles/10white.png").convert_alpha()
tile_10_green = pygame.image.load("graphics/tiles/10green.png").convert_alpha()
tile_10_red = pygame.image.load("graphics/tiles/10red.png").convert_alpha()
tile_10_blue = pygame.image.load("graphics/tiles/10blue.png").convert_alpha()
tile_10_orange = pygame.image.load("graphics/tiles/10orange.png").convert_alpha()
tile_10_yellow = pygame.image.load("graphics/tiles/10yellow.png").convert_alpha()
tiles_of_10 = [tile_10_white, tile_10_green, tile_10_red, tile_10_blue, tile_10_orange, tile_10_yellow]

tile_11_white = pygame.image.load("graphics/tiles/11white.png").convert_alpha()
tile_11_green = pygame.image.load("graphics/tiles/11green.png").convert_alpha()
tile_11_red = pygame.image.load("graphics/tiles/11red.png").convert_alpha()
tile_11_blue = pygame.image.load("graphics/tiles/11blue.png").convert_alpha()
tile_11_orange = pygame.image.load("graphics/tiles/11orange.png").convert_alpha()
tile_11_yellow = pygame.image.load("graphics/tiles/11yellow.png").convert_alpha()
tiles_of_11 = [tile_11_white, tile_11_green, tile_11_red, tile_11_blue, tile_11_orange, tile_11_yellow]

tile_12_white = pygame.image.load("graphics/tiles/12white.png").convert_alpha()
tile_12_green = pygame.image.load("graphics/tiles/12green.png").convert_alpha()
tile_12_red = pygame.image.load("graphics/tiles/12red.png").convert_alpha()
tile_12_blue = pygame.image.load("graphics/tiles/12blue.png").convert_alpha()
tile_12_orange = pygame.image.load("graphics/tiles/12orange.png").convert_alpha()
tile_12_yellow = pygame.image.load("graphics/tiles/12yellow.png").convert_alpha()
tiles_of_12 = [tile_12_white, tile_12_green, tile_12_red, tile_12_blue, tile_12_orange, tile_12_yellow]

tile_13_white = pygame.image.load("graphics/tiles/13white.png").convert_alpha()
tile_13_green = pygame.image.load("graphics/tiles/13green.png").convert_alpha()
tile_13_red = pygame.image.load("graphics/tiles/13red.png").convert_alpha()
tile_13_blue = pygame.image.load("graphics/tiles/13blue.png").convert_alpha()
tile_13_orange = pygame.image.load("graphics/tiles/13orange.png").convert_alpha()
tile_13_yellow = pygame.image.load("graphics/tiles/13yellow.png").convert_alpha()
tiles_of_13 = [tile_13_white, tile_13_green, tile_13_red, tile_13_blue, tile_13_orange, tile_13_yellow]

tile_20_white = pygame.image.load("graphics/tiles/20white.png").convert_alpha()
tile_20_green = pygame.image.load("graphics/tiles/20green.png").convert_alpha()
tile_20_red = pygame.image.load("graphics/tiles/20red.png").convert_alpha()
tile_20_blue = pygame.image.load("graphics/tiles/20blue.png").convert_alpha()
tile_20_orange = pygame.image.load("graphics/tiles/20orange.png").convert_alpha()
tile_20_yellow = pygame.image.load("graphics/tiles/20yellow.png").convert_alpha()
tiles_of_20 = [tile_20_white, tile_20_green, tile_20_red, tile_20_blue, tile_20_orange, tile_20_yellow]

tile_21_white = pygame.image.load("graphics/tiles/21white.png").convert_alpha()
tile_21_green = pygame.image.load("graphics/tiles/21green.png").convert_alpha()
tile_21_red = pygame.image.load("graphics/tiles/21red.png").convert_alpha()
tile_21_blue = pygame.image.load("graphics/tiles/21blue.png").convert_alpha()
tile_21_orange = pygame.image.load("graphics/tiles/21orange.png").convert_alpha()
tile_21_yellow = pygame.image.load("graphics/tiles/21yellow.png").convert_alpha()
tiles_of_21 = [tile_21_white, tile_21_green, tile_21_red, tile_21_blue, tile_21_orange, tile_21_yellow]


tile_22_white = pygame.image.load("graphics/tiles/22white.png").convert_alpha()
tile_22_green = pygame.image.load("graphics/tiles/22green.png").convert_alpha()
tile_22_red = pygame.image.load("graphics/tiles/22red.png").convert_alpha()
tile_22_blue = pygame.image.load("graphics/tiles/22blue.png").convert_alpha()
tile_22_orange = pygame.image.load("graphics/tiles/22orange.png").convert_alpha()
tile_22_yellow = pygame.image.load("graphics/tiles/22yellow.png").convert_alpha()
tiles_of_22 = [tile_22_white, tile_22_green, tile_22_red, tile_22_blue, tile_22_orange, tile_22_yellow]


tile_23_white = pygame.image.load("graphics/tiles/23white.png").convert_alpha()
tile_23_green = pygame.image.load("graphics/tiles/23green.png").convert_alpha()
tile_23_red = pygame.image.load("graphics/tiles/23red.png").convert_alpha()
tile_23_blue = pygame.image.load("graphics/tiles/23blue.png").convert_alpha()
tile_23_orange = pygame.image.load("graphics/tiles/23orange.png").convert_alpha()
tile_23_yellow = pygame.image.load("graphics/tiles/23yellow.png").convert_alpha()
tiles_of_23 = [tile_23_white, tile_23_green, tile_23_red, tile_23_blue, tile_23_orange, tile_23_yellow]


# ----------------------------- Game loop functionality below -------------------------
s_selected = True
as_selected = True
p_selected = True
u_selected = True
l_selected = True
t_selected = True
h_selected = True

algs_to_show = []
algset = [algs.scll, algs.ascll, algs.pcll, algs.ucll, algs.lcll, algs.tcll, algs.hcll]
for subset in algset:
	for element in subset:
		algs_to_show.append(element)


# game loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				pass
			if event.key == pygame.K_f:
				cube.u_turn()
			elif event.key == pygame.K_r:
				cube.u_prime_turn()
			elif event.key == pygame.K_j:
				cube.r_turn()
			elif event.key == pygame.K_u:
				cube.r_prime_turn()    
			elif event.key == pygame.K_d:
				cube.f_turn()
			elif event.key == pygame.K_e:
				cube.f_prime_turn()
			elif event.key == pygame.K_s:
				cube.b_turn()
			elif event.key == pygame.K_w:
				cube.b_prime_turn()    
			elif event.key == pygame.K_k:
				cube.l_turn()
			elif event.key == pygame.K_i:
				cube.l_prime_turn()
			elif event.key == pygame.K_l:
				cube.d_turn()
			elif event.key == pygame.K_o:
				cube.d_prime_turn()
			# TODO: add x, y and z prime rotations    
			elif event.key == pygame.K_x:
				cube.x_rotation()
			elif event.key == pygame.K_y:
				cube.y_rotation()
			elif event.key == pygame.K_z:
				cube.z_rotation()
	
	screen.blit(background_surface, (0, 0))

	# blit cube and tiles
	screen.blit(cube_surface, (cube_pos_x,cube_pos_y))

	screen.blit(tiles_of_00[cube.state[0][0]], pos_00)
	screen.blit(tiles_of_01[cube.state[0][1]], pos_01)
	screen.blit(tiles_of_02[cube.state[0][2]], pos_02)
	screen.blit(tiles_of_03[cube.state[0][3]], pos_03)

	screen.blit(tiles_of_10[cube.state[1][0]], pos_10)
	screen.blit(tiles_of_11[cube.state[1][1]], pos_11)
	screen.blit(tiles_of_12[cube.state[1][2]], pos_12)
	screen.blit(tiles_of_13[cube.state[1][3]], pos_13)

	screen.blit(tiles_of_20[cube.state[2][0]], pos_20)
	screen.blit(tiles_of_21[cube.state[2][1]], pos_21)
	screen.blit(tiles_of_22[cube.state[2][2]], pos_22)
	screen.blit(tiles_of_23[cube.state[2][3]], pos_23)

	# blit texts
	screen.blit(title_surface, title_rect)
	screen.blit(controls_surface, (720, 100))

	# blit buttons and checkmarks
	if scramble_button.draw():
		cube.scramble()
	if reset_button.draw():
		cube.reset()
	if cll_button.draw():
		try:
			my_fun = choice(algs_to_show)
			cube.state = my_fun()
			auf = randint(0, 3)
			for _ in range(auf):
				cube.u_turn()
		# below we handle the case when no checkboxes are selected
		except IndexError:
			cube.state = cube.solved_state
			# perhaps blit an error message here... like: Please select at least one alg subset

	# creating checkbox button behavior
	# TODO: code is repeating, create a function to handle this cleanly
	if checkbox_scll.draw():
		s_selected = not s_selected
		if not s_selected:
			for alg in algs.scll:
				algs_to_show.remove(alg)
		if s_selected:
			for alg in algs.scll:
				algs_to_show.append(alg)

	if checkbox_ascll.draw():
		as_selected = not as_selected
		if not as_selected:
			for alg in algs.ascll:
				algs_to_show.remove(alg)
		if as_selected:
			for alg in algs.ascll:
				algs_to_show.append(alg)

	if checkbox_pcll.draw():
		p_selected = not p_selected
		if not p_selected:
			for alg in algs.pcll:
				algs_to_show.remove(alg)
		if p_selected:
			for alg in algs.pcll:
				algs_to_show.append(alg)

	if checkbox_ucll.draw():
		u_selected = not u_selected
		if not u_selected:
			for alg in algs.ucll:
				algs_to_show.remove(alg)
		if u_selected:
			for alg in algs.ucll:
				algs_to_show.append(alg)

	if checkbox_lcll.draw():
		l_selected = not l_selected
		if not l_selected:
			for alg in algs.lcll:
				algs_to_show.remove(alg)
		if l_selected:
			for alg in algs.lcll:
				algs_to_show.append(alg)

	if checkbox_tcll.draw():
		t_selected = not t_selected
		if not t_selected:
			for alg in algs.tcll:
				algs_to_show.remove(alg)
		if t_selected:
			for alg in algs.tcll:
				algs_to_show.append(alg)

	if checkbox_hcll.draw():
		h_selected = not h_selected
		if not h_selected:
			for alg in algs.hcll:
				algs_to_show.remove(alg)
		if h_selected:
			for alg in algs.hcll:
				algs_to_show.append(alg)

	# blitting checkmark into checkbox if our checkbox is selected
	if s_selected:
		screen.blit(checkmark_img, checkmark_s_rect)
	if as_selected:
		screen.blit(checkmark_img, checkmark_as_rect)
	if p_selected:
		screen.blit(checkmark_img, checkmark_p_rect)
	if u_selected:
		screen.blit(checkmark_img, checkmark_u_rect)
	if l_selected:
		screen.blit(checkmark_img, checkmark_l_rect)
	if t_selected:
		screen.blit(checkmark_img, checkmark_t_rect)
	if h_selected:
		screen.blit(checkmark_img, checkmark_h_rect)

	# blitting labels over buttons, checkboxes etc.	
	screen.blit(scramble_surf, scramble_rect)
	screen.blit(reset_surf, reset_rect)
	screen.blit(cll_surf, cll_rect)
	screen.blit(cll_selector_surf, cll_selector_rect)
	screen.blit(cll_labels_surf, cll_labels_rect)

	pygame.display.update()
	# set fps cap... this is capped to 60 fps anyway because vsync is activated.
	clock.tick(60)
	#print(clock.get_fps())
