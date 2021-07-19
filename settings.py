class Settings():
	"""
	Uma classe para armazenar todas as configurações da invasão alienígena.
	"""

	def __init__(self):
		""" Inicializa as configurações do jogo."""
		# Configurações da tela
		self.screen_width = 1280		
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Configurações da espaçonave
		self.ship_limit = 3

		# Configurações dos projéteis
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3

		# Configurações dos alienígenasS
		self.fleet_drop_speed = 10

		# A taxa com que a velocidade do jogo aumenta
		self.speedup_scale = 1.1

		self.initializa_dynamic_settings()

	def initializa_dynamic_settings(self):
		"""Inicializa as configurações que mudam no deocrrer do jogo."""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		# fleet direction igual a 1 representa a direita; -1 representa a esquerda
		self.fleet_direction = 1

		# Pontuação
		self.alien_points = 50

	def increase_speed(self):
		"""Aumenta as configurações de velocidade."""
		self.ship_speed_factor *= self.speedup_scale 
		self.bullet_speed_factor *= self.speedup_scale 
		self.alien_speed_factor *= self.speedup_scale 