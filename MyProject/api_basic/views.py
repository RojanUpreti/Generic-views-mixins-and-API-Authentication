from cgitb import lookup
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# @api_view(['GET','POST'])
# def article_list(request):
#     if request.method=='GET':
#         articles=Article.objects.all()
#         serializer=ArticleSerializer(articles,many=True)
#         return Response(serializer.data)

#     elif request.method=='POST':
#         # data=JSONParser().parse(request)
#         serializer=ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors,status.HTTP_400_BAD_REQUEST)

# class ArticleAPIView(APIView):
#     def get(self,request):
#         articles=Article.objects.all()
#         serializer=ArticleSerializer(articles,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer=ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin):
    serializer_class=ArticleSerializer
    queryset=Article.objects.all()
    lookup_field='id'

    # authentication_classes=[TokenAuthentication]
    # authentication_classes=[SessionAuthentication,BasicAuthentication]
    # permission_classses=[IsAuthenticated]

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id):
        return self.destroy(request,id)



# class ArticleDetails(APIView):
#     def get_object(self,id):
#         try:
#             return Article.objects.get(id=id)
#         except Article.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self,request,id):
#         article=self.get_object(id)
#         serializer=ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self,request,id):
#         article=self.get_object(id)
#         serializer=ArticleSerializer(article,data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,id):
#         article=self.get_object(id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# @api_view(['GET','PUT','DELETE'])
# def article_detail(request,pk):
#     try:
#         article=Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method=='GET':
#         serializer=ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method=='PUT':
#         serializer=ArticleSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     elif request.method=='DELETE':
#         article.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

