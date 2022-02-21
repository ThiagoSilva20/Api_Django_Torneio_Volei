from rest_framework import viewsets
from django.db import connection
from rest_framework import status
from rest_framework.response import Response


class Teams(viewsets.ModelViewSet):
    queryset =  """
                SELECT * FROM Teams
                """
    try:
        statement = 0
        with connection.cursor() as cursor:
            cursor.execute(queryset.format(id))
            statement = cursor.fetchall()[0][0]
        return statement
    except Exception:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Athletes(viewsets.ModelViewSet):
     queryset = 'SELECT * FROM Athletes'

class Coach(viewsets.ModelViewSet):
     queryset = 'SELECT * FROM Coach'