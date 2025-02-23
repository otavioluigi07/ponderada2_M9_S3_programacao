import pytest
from src.service.netflix_service import NetflixApp

def test_autoplay_next_episode_after_full_watch():
    """
    Testa se o próximo episódio é iniciado automaticamente após o episódio atual ser finalizado.
    """
    app = NetflixApp()
    app.login("user@example.com", "senha123")
    app.watch_episode()
    assert app.is_playing_next_episode() is True

def test_no_autoplay_if_episode_not_finished():
    """
    Verifica que se o episódio não for concluído, o autoplay não é acionado.
    """
    app = NetflixApp()
    app.login("user@example.com", "senha123")
    # Simulando que o episódio não foi finalizado (episode_finished permanece False)
    assert app.is_playing_next_episode() is False

def test_autoplay_with_multiple_episodes():
    """
    Simula um cenário onde o usuário assiste a vários episódios seguidos.
    Após cada episódio completo, o autoplay deve ser ativado.
    """
    app = NetflixApp()
    app.login("user@example.com", "senha123")
    # Episódio 1
    app.watch_episode()
    assert app.is_playing_next_episode() is True

    # Reseta para simular que o usuário iniciou o próximo episódio
    app.episode_finished = False
    # Episódio 2 não finalizado
    assert app.is_playing_next_episode() is False

    # Finaliza episódio 2
    app.watch_episode()
    assert app.is_playing_next_episode() is True
