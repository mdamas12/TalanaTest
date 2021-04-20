from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from  .serializer import UserSerializer
from rest_framework import status
import random
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template import loader


# Create your views here.


class UserView(APIView):

    def get(self, request, format=None):
    
        """listar usuarios"""

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):

        """Registrar Usuario"""

        data = request.data
       
        try:
            User.objects.get(email=data["email"])
        except User.DoesNotExist:
            password = "123456789"
            user = User.objects.create_user(username=data["email"], email=data["email"], password=password, first_name=data["first_name"], is_superuser=data["is_superuser"]).save()
            serializer = UserSerializer(user, many=False)

            html_message = loader.render_to_string(
            '../templates/verify-email.html',
                    {
                        'user': data["first_name"]+' '+data["last_name"]+' haz click en el siguiente enlace para validar tu cuenta',
                        'subject':  'http://localhost:8080/#/verify/'+data["email"]         
                    }
            )

            send_mail(
                    'Subject here',
                    'Here is the message.',
                    'marcosdamas12@gmail.com',
                    [data["email"]],
                    fail_silently=False,
                    html_message=html_message
                )
            return Response("usuario creado, el link de validacion sera enviado a su email", status=status.HTTP_200_OK)

        return Response("Email o username  ya esta registrado", status=status.HTTP_400_BAD_REQUEST)
    
class UserChangePassword(APIView): #Actualizar Contrasenia

    
    def put(self, request, email, format=None):
        data = request.data
  
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response("El Usuario no existe",  status=status.HTTP_400_BAD_REQUEST)
        user.set_password(data["password"])
        user.save() 
        serializer = UserSerializer(user, many=False)
        return Response("Cuenta Verificada Satisfactoriamente", status=status.HTTP_200_OK)

class winnerView(APIView):
      
    def get(self, request, format=None):
        """Obtener Ganador del concurso"""

        n_user = User.objects.count()
        rand = random.randint(1,n_user)
        print(rand)
        user = User.objects.get(id=rand)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)



