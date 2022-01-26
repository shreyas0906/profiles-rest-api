from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """
    Test APIView
    """

    def get(self, request, format=None):
        """
        return a list of APIViews features
        """
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over you application logic',
            'Is mapped manuaaly to URLs'
        ]
        return Response({'message': 'Hello',
                         'an_apiview': an_apiview})
