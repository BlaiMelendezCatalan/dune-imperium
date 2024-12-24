from fastapi import APIRouter


def make_routes() -> APIRouter:

    router = APIRouter(prefix="/locations", tags=["locations"])

    @router.post("/pay")
    def pay_location_cost(): ...

    return router
