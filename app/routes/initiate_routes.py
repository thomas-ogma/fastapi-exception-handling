from app.routes import test_route


class InitiateRouters:
    def __init__(self, app):
        app.include_router(test_route.router)

