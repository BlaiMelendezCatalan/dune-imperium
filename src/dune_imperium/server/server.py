from fastapi import FastAPI

from dune_imperium.server.routers import locations


def create_app():

    app = FastAPI()

    # TODO feed all routes
    app.include_router(locations.make_routes())

    return app
