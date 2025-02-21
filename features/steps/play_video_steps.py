from behave import given, when, then
from src.service.netflix_service import NetflixApp

@given("o usuário está logado na Netflix")
def step_user_logged_in(context):
    context.netflix = NetflixApp()
    context.netflix.login("user@example.com", "senha123")
    assert context.netflix.is_logged_in()

@given("o usuário pausou um vídeo no minuto {time:d}")
def step_user_paused_video(context, time):
    context.netflix.pause_video(time)
    assert context.netflix.get_last_played_time() == time

@when("o usuário acessa a Netflix novamente e inicia a reprodução do vídeo")
def step_user_reopens_and_plays(context):
    context.netflix.reopen()
    context.netflix.play_video()

@then("o vídeo deve começar a partir do minuto {time:d}")
def step_video_resumes_correctly(context, time):
    assert context.netflix.get_current_play_time() == time

@given("o usuário assistiu um episódio inteiro de uma série")
def step_watched_episode(context):
    context.netflix.watch_episode()

@when("o episódio termina")
def step_episode_finishes(context):
    context.netflix.episode_finished = True

@then("o próximo episódio deve começar automaticamente")
def step_next_episode_autoplays(context):
    assert context.netflix.is_playing_next_episode()
