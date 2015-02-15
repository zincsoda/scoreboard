import traceback
import logging
from django.http import HttpResponseServerError

logger = logging.getLogger('exceptions')

class ExceptionMiddleware(object):

    def process_exception(self, request, exception):
        exc_str = "Logging Exception: %s" % traceback.format_exc()
        logger.info(exc_str)
        response = "Server Error: %s" % exception
        return HttpResponseServerError(response) 
