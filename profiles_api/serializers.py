from rest_framework import  serializeers

class HelloSerializer(serializeers.Serializer):
    
    name = serializeers.CharField(max_length=10)

