import json
import time

from catalog.models import RequestLog


class RequestLogMiddleware:
	def __init__(self, get_response):

		self.get_response = get_response

	def __call__(self, request):
		# Add execution time
		start_time = time.monotonic()
		# Request passes to controller
		response = self.get_response(request)
		exec_time = int((time.monotonic() - start_time) * 1000)

		if "admin" not in request.path:
			log = RequestLog(path=request.path,
			                 method=request.method,
			                 full_response=self.get_response(request),
			                 exec_time=exec_time,
			                 status_code=response.status_code,
			                 body_post=request.POST,
			                 body_get=request.GET,
			                 ip_address=request.META.get("REMOTE_ADDR"))
			log.save()
		else:
			pass
		return response
