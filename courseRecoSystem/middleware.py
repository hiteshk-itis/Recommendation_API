# from django.contrib.auth import 
from rest_framework.authtoken.models import Token

class TokenAppendMiddleware:
    def __init__(self, get_response): 
        self.get_response = get_response

    def __call__(self, request): 

        if request.user.is_authenticated: 
            # request.META['Authorization'] = 
            tokenVal = Token.objects.get(user_id=request.user.id).key
            request.META['Authorization'] = "Token "+ str(tokenVal)
            

            
        response = self.get_response(request)

        return response 
