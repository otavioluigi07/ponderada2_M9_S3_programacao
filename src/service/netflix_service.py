class NetflixApp():
  def __init__(self):
    self.logged_in = False

  def login(self, email: str, senha: str) -> None:
    #Simulação de login
    if email and senha:
      self.logged_in = True
