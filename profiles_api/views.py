from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """
    Test API View
    """
    def get(self, request, format=None):
        """
        returns a list of APIView features
        :param request: a djangoframework request containing the details of the request
        :param format:
        :return:
        """
        an_apiview = [
            'Uses HTTP methods as function(get, post, patcg, put)',
            'Is similar to a traditional Django view',
            'Gives you the most control over you application logic',
            'Is mapped manuaaly to URLs'
        ]
        return Response({'message': 'Hello',
                         'an_apiview': an_apiview})

