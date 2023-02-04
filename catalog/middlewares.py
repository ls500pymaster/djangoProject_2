class SimpleMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		print(self.get_response)
		print(request)
		response = self.get_response(request)
		print(request)
		return response
