import pytest
from src.service.netflix_service import NetflixApp

def test_video_resume_exact_minute():
    """
    Testa se o vídeo retoma exatamente do ponto onde foi pausado.
    """
    app = NetflixApp()
    app.login("user@example.com", "senha123")
    app.pause_video(15)
    app.reopen()
    app.play_video()
    assert app.get_current_play_time() == 15

def test_video_resume_after_multiple_pauses():
    """
    Testa a retomada do vídeo considerando que o usuário pausou em diferentes pontos,
    garantindo que sempre retoma do último ponto pausado.
    """
    app = NetflixApp()
    app.login("user@example.com", "senha123")
    # Primeira pausa no minuto 10
    app.pause_video(10)
    app.reopen()
    app.play_video()
    assert app.get_current_play_time() == 10
    # O usuário pausa novamente no minuto 25
    app.pause_video(25)
    app.reopen()
    app.play_video()
    assert app.get_current_play_time() == 25

def test_resume_without_login_fails():
    """
    Verifica que, se o usuário não estiver logado, a retomada não deve ocorrer
    (nesse exemplo, o comportamento pode ser definido de acordo com a lógica da aplicação).
    """
    app = NetflixApp()
    # Não realiza login
    app.pause_video(15)
    app.reopen()
    app.play_video()
    # Se a lógica exigir login, o current_play_time deve continuar em 0
    assert app.get_current_play_time() == 0
