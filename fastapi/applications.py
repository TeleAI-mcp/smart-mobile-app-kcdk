from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

from fastapi import params
from fastapi.encoders import DictIntStrAny, SetIntStr
from fastapi.responses import JSONResponse, Response
from fastapi.routing import APIRoute


class FastAPI:
    """
    The main FastAPI class.
    """

    def __init__(
        self,
        *,
        debug: bool = False,
        routes: Optional[List[APIRoute]] = None,
        title: str = "FastAPI",
        description: str = "",
        version: str = "0.1.0",
        openapi_url: Optional[str] = "/openapi.json",
        openapi_tags: Optional[List[Dict[str, Any]]] = None,
        servers: Optional[List[Dict[str, Union[str, Any]]]] = None,
        default_response_class: Type[Response] = JSONResponse,
        docs_url: Optional[str] = "/docs",
        redoc_url: Optional[str] = "/redoc",
        swagger_ui_oauth2_redirect_url: Optional[str] = None,
        **extra: Any,
    ) -> None:
        self.debug: bool = debug
        self.routes: List[APIRoute] = routes or []
        self.title: str = title
        self.description: str = description
        self.version: str = version
        self.openapi_url: Optional[str] = openapi_url
        self.openapi_tags: Optional[List[Dict[str, Any]]] = openapi_tags
        self.servers: Optional[List[Dict[str, Union[str, Any]]]] = servers
        self.default_response_class: Type[Response] = default_response_class
        self.docs_url: Optional[str] = docs_url
        self.redoc_url: Optional[str] = redoc_url
        self.swagger_ui_oauth2_redirect_url: Optional[str] = swagger_ui_oauth2_redirect_url
        self.extra: Dict[str, Any] = extra

    def add_route(
        self,
        path: str,
        route: APIRoute,
    ) -> None:
        self.routes.append(route)

    def include_router(
        self,
        router: "APIRouter",
        *,
        prefix: str = "",
        tags: Optional[List[str]] = None,
        dependencies: Optional[Sequence[params.Depends]] = None,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
    ) -> None:
        for route in router.routes:
            self.routes.append(route)
