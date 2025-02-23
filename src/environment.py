from service.netflix_service import NetflixApp

def before_scenario(context, scenario):
    context.netflix = NetflixApp()
    context.netflix.login("user@example.com", "senha123")
