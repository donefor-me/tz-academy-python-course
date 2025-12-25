# cores/exceptions/exception_handlers.py
from fastapi import Request
from fastapi.responses import JSONResponse

from business_exception import BusinessException
from schemas.responses.error_response import ErrorResponse


async def business_exception_handler(
    request: Request,
    exc: BusinessException,
):
    trace_id = getattr(request.state, "trace_id", None)

    response = ErrorResponse(
        error_code=exc.error_code,
        message=exc.message,
        trace_id=trace_id,
        extra=exc.extra,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=response.model_dump(),
    )
