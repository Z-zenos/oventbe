from fastapi import APIRouter, FastAPI
from fastapi.routing import APIRoute

# from app.api.admin.routes import admin_routers
from app.api.audience.routes import audience_routers

# from app.api.organizer.routes import organizer_routers
# from app.api.shared.routes import shared_routers

api_router = APIRouter()

api_router.include_router(audience_routers)
# api_router.include_router(organizer_routers, prefix="/org")
# api_router.include_router(admin_routers, prefix="/admin")
# api_router.include_router(shared_routers)


# path operation関数 の名前をoperationIdとして使用する
# https://fastapi.tiangolo.com/ja/advanced/path-operation-advanced-configuration/#path-operation-operationid
def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, 'read_items'


use_route_names_as_operation_ids(api_router)
