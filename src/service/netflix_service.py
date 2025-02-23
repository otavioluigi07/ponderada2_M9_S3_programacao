class NetflixApp:
    def __init__(self):
        self.logged_in = False
        self.last_played_time = 0
        self.current_play_time = 0
        self.episode_finished = False

    def login(self, email, senha):
        # Simulação simples de login
        if email and senha:
            self.logged_in = True

    def is_logged_in(self):
        return self.logged_in

    def pause_video(self, time):
        self.last_played_time = time

    def get_last_played_time(self):
        return self.last_played_time

    def reopen(self) -> None:
        # Somente reabre o vídeo se o usuário estiver logado
        if self.logged_in:
            self.current_play_time = self.last_played_time

    def play_video(self) -> None:
        # Só reproduz se estiver logado; caso contrário, mantém em 0
        if self.logged_in:
            self.current_play_time = self.last_played_time
        else:
            self.current_play_time = 0

    def get_current_play_time(self):
        return self.current_play_time

    def watch_episode(self):
        # Simula a visualização completa de um episódio
        self.episode_finished = True

    def is_playing_next_episode(self):
        # Se o episódio foi finalizado, simula o autoplay do próximo episódio
        if self.episode_finished:
            return True
        return False
