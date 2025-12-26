import logging
from colorlog import ColoredFormatter
from cores.trace import trace_id_ctx


class TraceIdFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.trace_id = trace_id_ctx.get() or "n/a"
        return True


# Called once when the application starts to
# create a formatter with %(trace_id)s
# and attach the TraceIdFilter to the root logger
def setup_logging(sql_echo: bool = False) -> None:
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    trace_filter = TraceIdFilter()

    # If the root logger already has handlers
    # (usually configured by Uvicorn), attach the filter to them
    if root.handlers:
        for h in root.handlers:
            h.addFilter(trace_filter)
    else:
        # If no handlers exist, create a console handler
        # with a custom formatter
        handler = logging.StreamHandler()
        formatter = ColoredFormatter(
            fmt="%(log_color)s %(asctime)s %(levelname)s [trace_id=%(trace_id)s] %(name)s: %(message)s",
            log_colors={
                "DEBUG": "white",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            }
        )
        handler.setFormatter(formatter)
        handler.addFilter(trace_filter)
        root.addHandler(handler)

    # DEV ONLY: enable SQLAlchemy engine logging
    # through the current logging system
    sa_logger = logging.getLogger("sqlalchemy.engine")
    sa_logger.setLevel(logging.INFO if sql_echo else logging.WARNING)
    sa_logger.propagate = True

# Review this in the database configuration file
# engine = create_engine(
#     settings.database_url,
#     echo=False,  # disable echo to avoid duplicate DB logs
#     pool_pre_ping=True,
#     pool_size=settings.pool_size,
#     max_overflow=settings.max_overflow,
# )
