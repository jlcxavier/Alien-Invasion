class GameStats():
	"""Armazena dados estatísticos da Invasão Alienígena."""

	def __init__(self, c_settings):
		"""Inicializa os dados estatíssticos."""
		self.c_settings = c_settings
		self.reset_stats()

		# Inicia o jogo em um estado inativo
		self.game_active = False

	def reset_stats(self):
		""" Inicializa os dados estatísticos que podem mudar durante o jogo."""
		self.ships_left = self.c_settings.ship_limit
