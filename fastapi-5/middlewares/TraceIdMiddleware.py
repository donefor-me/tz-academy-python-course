import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from cores.trace import trace_id_ctx

TRACE_HEADER = "X-Trace-Id"


class TraceIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        trace_id = str(uuid.uuid4())
        request.state.trace_id = trace_id
        token = trace_id_ctx.set(trace_id)
        try:
            response = await call_next(request)
        finally:
            trace_id_ctx.reset(token)
        response.headers[TRACE_HEADER] = trace_id
        return response
