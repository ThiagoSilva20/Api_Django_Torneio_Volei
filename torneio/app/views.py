from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view




@api_view(['GET'])
def index(request):
    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

##############################################################################

@api_view(['GET'])
def fun_teams_g(request):
    queryset =  """
                SELECT * FROM app_teams
                """
    try:
        times = []
        with connection.cursor() as cursor:
            cursor.execute(queryset.format(id))
            times_retorno = cursor.fetchall()

        for time in times_retorno:
            conteudo = {
               'id':time[0],
               'name_team':time[1], 
               'coaches_id':time[2]
            }
            times.append(conteudo)
        
        return Response(times, status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#################################
#################################
#################################

@api_view(['GET'])
def fun_athletes_g(request):
    queryset =  """
                SELECT * FROM app_athletes
                """
    try:
        athletes = []
        with connection.cursor() as cursor:
            cursor.execute(queryset.format(id))
            athletes_retorno = cursor.fetchall()

        for atleta in athletes_retorno:
            conteudo = {
                'id':atleta[0],
                'full_name':atleta[1],
                'email':atleta[2],
                'federado':atleta[3],
                'cpf':atleta[4],
                'rg':atleta[5],
                'team_id':atleta[6]
            }
            athletes.append(conteudo)
        return Response(athletes, status=status.HTTP_202_ACCEPTED)
    except Exception:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#################################
#################################
#################################

@api_view(['GET'])
def fun_coach_g(request):
    queryset =  """
                SELECT * FROM app_coach
                """
    try:
        coach_ar = []
        
        with connection.cursor() as cursor:
            cursor.execute(queryset.format(id))
            coach_retorno = cursor.fetchall()
        for coach in coach_retorno:
            conteudo = {
                'id':coach[0],
                'full_name':coach[1],
                'email':coach[2],
                'cpf':coach[3],
                'rg':coach[4]
            }
            coach_ar.append(conteudo)

        return Response(coach_ar, status=status.HTTP_202_ACCEPTED )
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################################################################################################################################################
###################################################################################################################################################################
###################################################################################################################################################################

@api_view(['POST'])
def fun_team_p(request):
    try:

        if not request.data.__contains__('name_team'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar o nome da equipe."})
        
        if not request.data.__contains__('coaches'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar o nome do treinador."})
        
        queryinsert =   """
                        INSERT INTO public.app_teams
                        (name_team, coaches_id)
                        VALUES('{}', {});
                        """.format(request.data['name_team'], request.data['coaches'])
        with connection.cursor() as cursor:
            cursor.execute(queryinsert)

        querybus =  """
            SELECT * FROM app_teams WHERE id = (SELECT MAX (id) FROM app_teams) 
        """
        with connection.cursor() as cursor:
            cursor.execute(querybus)
            times = cursor.fetchall()
            print(times)
        return Response(data={'id':times[0][0], 'team_name':times[0][1], 'coach_id':times[0][2]},status=status.HTTP_201_CREATED)
         
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#################################
#################################
#################################
         
@api_view(['POST'])
def fun_athletes_p(request):
    try:

        if not request.data.__contains__('full_name'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar seu nome completo."})
        
        if not request.data.__contains__('email'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar o email."})
        
        if not request.data.__contains__('cpf'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar o seu cpf."})

        if not request.data.__contains__('rg'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar o seu rg."})

        if not request.data.__contains__('team_id'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar o numero destinado a sua equipe."})
        queryinsert =  """
            INSERT INTO app_athletes
            (full_name, email, federado, cpf, rg, team_id )
            VALUES('{}', '{}', {}, '{}', '{}', {});
        """.format(request.data['full_name'], request.data['email'], request.data['federado'], request.data['cpf'], request.data['rg'], request.data['team_id'])
        with connection.cursor() as cursor:
            cursor.execute(queryinsert)

        querybus = """
            SELECT * FROM app_athletes WHERE id = (SELECT MAX (id) FROM app_athletes)
        """
        with connection.cursor() as cursor:
            cursor.execute(querybus)
            atletas = cursor.fetchall()
            print(atletas)

        return Response(data={'id':atletas[0][0], 'full_name':atletas[0][1], 'email':atletas[0][2], 'federado':atletas[0][3], 'cpf':atletas[0][4], 'rg':atletas[0][5], 'team_id':atletas[0][6] }, status=status.HTTP_201_CREATED)
    except Exception:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#################################
#################################
#################################

@api_view(['POST'])
def fun_coach_p(request):
    try:

        if not request.data.__contains__('full_name'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar seu nome completo."})
        
        if not request.data.__contains__('email'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar seu email."})
        
        if not request.data.__contains__('cpf'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar seu cpf."})
        
        if not request.data.__contains__('rg'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar seu rg."})
        
        queryinsert =  """
            INSERT INTO  app_coach(full_name, email, cpf, rg)
            VALUES('{}', '{}', '{}', '{}')
            """.format(request.data['full_name'], request.data['email'], request.data['cpf'], request.data['rg'])
        with connection.cursor() as cursor:
            cursor.execute(queryinsert)

        querybus = """
            SELECT * FROM app_coach WHERE id = (SELECT MAX (id) FROM app_coach)
        """
        with connection.cursor() as cursor:
            cursor.execute(querybus)
            coach = cursor.fetchall()
            print(coach)

        return Response(data={'id':coach[0][0], 'full_name':coach[0][1], 'email':coach[0][2], 'cpf':coach[0][3], 'rg':coach[0][4]}, status=status.HTTP_201_CREATED)
         
    except Exception:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################################################################################################################################################
###################################################################################################################################################################
###################################################################################################################################################################

@api_view(['DELETE'])
def fun_team_d(request, id):
    try: 
        querydel = """
            DELETE FROM app_teams
            WHERE id = {}
            """.format(id)
        
        with connection.cursor() as cursor:
            cursor.execute(querydel)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#################################
#################################
#################################

@api_view(['DELETE'])
def fun_athletes_d(request, id):
    try:
        querydel = """
            DELETE FROM app_athletes
            WHERE id = {} 
            """.format(id)
        
        with connection.cursor() as cursor:
            cursor.execute(querydel)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#################################
#################################
#################################

@api_view(['DELETE'])
def fun_coach_d(request, id):
    try:
        queryup = """
            UPDATE app_teams
            SET coaches_id = 0
            WHERE coach_id = {}
            """.format(id)
            
        querydel = """
            DELETE FROM app_coach
            WHERE id = {}
            """.format(id)

        with connection.cursor() as cursor:
            cursor.execute(querydel)


        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################################################################################################################################################
###################################################################################################################################################################
###################################################################################################################################################################

@api_view(['PUT'])
def fun_teams_put(request, id):
    try:
        if not request.data.__contains__('name_team'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar o nome da equipe."})
        
        if not request.data.__contains__('coaches_id'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar o identificador do treinador."})

        queryup = """
            UPDATE app_teams
            SET name_team = '{}' , coaches_id = {}
            WHERE id = {}

        """.format(request.data['name_team'], request.data['coaches_id'], id)
        with connection.cursor() as cursor:
            cursor.execute(queryup)

        return Response(status=status.HTTP_200_OK)
    except Exception:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#################################
#################################
#################################

@api_view(['PUT'])
def fun_athletes_put(request, id):
    try:
        if not request.data.__contains__('full_name'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar seu nome completo."})
        
        if not request.data.__contains__('email'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar o email."})
        
        if not request.data.__contains__('cpf'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar o seu cpf."})

        if not request.data.__contains__('rg'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar o seu rg."})

        if not request.data.__contains__('team_id'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar o numero destinado a sua equipe."})

        queryup = """
            UPDATE app_athletes
            SET full_name = '{}' , email = '{}', cpf = '{}', rg = '{}', team__id = {} 
            WHERE id = {}

        """.format(request.data['full_name'], request.data['email'], request.data['cpf'], request.data['rg'], request.data['team_id'], id)
        with connection.cursor() as cursor:
            cursor.execute(queryup)

        return Response(status=status.HTTP_200_OK)
    except Exception:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#################################
#################################
#################################

@api_view(['PUT'])
def fun_coach_put(request, id):
    try:
        if not request.data.__contains__('full_name'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar seu nome completo."})
        
        if not request.data.__contains__('email'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar seu email."})
        
        if not request.data.__contains__('cpf'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar seu cpf."})
        
        if not request.data.__contains__('rg'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar seu rg."})
        

        queryup = """
            UPDATE app_coach
            SET full_name = '{}' , email = '{}', cpf = '{}', rg = '{}'
            WHERE id = {}

        """.format(request.data['full_name'], request.data['email'], request.data['cpf'], request.data['rg'], id)
        with connection.cursor() as cursor:
            cursor.execute(queryup)

        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
