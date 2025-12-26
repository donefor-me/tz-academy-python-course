from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from exceptions.base_exception import BusinessException
from exceptions.handlers import business_exception_handler
from routers.router import api_router
from middlewares.DbSessionMiddleware import DBSessionMiddleware
from middlewares.TraceIdMiddleware import TraceIdMiddleware

app = FastAPI()
app.include_router(api_router)

# Middlewares
__APP_MIDDLEWARES__ = [
    (DBSessionMiddleware, {}),
    (TraceIdMiddleware, {}),
    (CORSMiddleware, {
        "allow_origins": ["*"],
        "allow_methods": ["*"],
        "allow_headers": ["*"],
    }),
]
for middleware, options in __APP_MIDDLEWARES__:
    app.add_middleware(middleware, **options)

# Exceptions
__APP_EXCEPTIONS__ = [
    (BusinessException, business_exception_handler),
]
for exc_class, handler in __APP_EXCEPTIONS__:
    app.add_exception_handler(exc_class, handler)
