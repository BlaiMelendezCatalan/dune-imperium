from fastapi import FastAPI

from dune_imperium.server.routers import game


def create_app():

    app = FastAPI()

    # TODO feed all routes
    app.include_router(game.make_routes())
    # app.include_router(big_cards.make_routes())
    # app.include_router(locations.make_routes())

    return app
