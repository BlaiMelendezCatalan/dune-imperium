from fastapi import FastAPI

from dune_imperium.server.routers import actions, game


def create_app():

    app = FastAPI()

    app.include_router(game.make_routes())
    app.include_router(actions.make_routes())

    return app
