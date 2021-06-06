from rest_framework.views import APIView
frpm rest_framework.response import Response


class HelloAPIView(APIView):

    def get(self,request, format=None):
        
        an_apiview = [
            
            'User HTTp methods as function (get, post, patch, put, delete)',
            'Is mapped manually to URLs',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            
            
        ]
        
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
        