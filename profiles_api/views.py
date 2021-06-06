from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import Status

from profiles_api import serializers


class HelloAPIView(APIView):

    def get(self,request, format=None):
        
        serializer_class = serializers.HelloSerializer
        
        def get(self,request,format=None):
        
            an_apiview = [
                
                'User HTTp methods as function (get, post, patch, put, delete)',
                'Is mapped manually to URLs',
                'Is similar to a traditional Django View',
                'Gives you the most control over you application logic',
                
            
        ]
        
            return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
        def post(self,request):
            
            serializers = self.serializer_class(data=request.data)
            
            
            if serializer.is_valid():
                
                name = serializer.validate.get('name')
                
                message = f'hello {name}'
                return Response({'message': message})
            else:
                return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)
            
            