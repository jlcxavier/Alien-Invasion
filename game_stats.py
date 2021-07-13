class GameStats():
	"""Armazena dados estatísticos da Invasão Alienígena."""

	def __init__(self, c_settings):
		"""Inicializa os dados estatíssticos."""
		self.c_settings = c_settings
		self.reset_stats()

		# Inicia a Invasão alienígena em um estado ativo
		self.game_active = True

	def reset_stats(self):
		""" Inicializa os dados estatísticos que podem mudar durante o jogo."""
		self.ships_left = self.c_settings.ship_limit
