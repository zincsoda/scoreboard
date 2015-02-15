import traceback
import logging

logger = logging.getLogger('exceptions')

class ExceptionMiddleware(object):

    def process_exception(self, request, exception):
        exc_str = "Logging Exception: %s" % traceback.format_exc()
        logger.info(exc_str)
        return process_http_exception(request, exception)

