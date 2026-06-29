from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BooksModel
from .serializers import BookSerializer


# list get
class ListApiView(APIView):
    def get(self, request):
        book = BooksModel.objects.all()
        serializer = BookSerializer(book, many=True).data
        data = {
            "status": f"Returned {len(book)} books",
            "book": serializer
        }
        return Response(data)


# list detail
class ListDetailView(APIView):
    def get(self, request, pk):
        try:
            obj = BooksModel.objects.get(id=pk)
            serializer = BookSerializer(obj).data
            data = {"status": "successfull",
                    "book": serializer}
            return Response(data, status.HTTP_200_OK)
        except Exception:
            return Response({
                "status": "Doesn't exist",

            }, status=status.HTTP_204_NO_CONTENT)


# create
class ListCreateView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            books = serializer.save()
            data = {"status": f"books are saved to database ",
                    "books": data}
            return Response(data)


# update
class ListUpdateView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(BooksModel, id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_save = serializer.save()
        return Response({
            "status": True,
            "massage": f"book {book_save}, updated successfull"
        })


# delete
class ListDeleteView(APIView):
    def delete(self, request, pk):
        try:
            book = get_object_or_404(BooksModel, id=pk)
            book.delete()
            return Response({
                "status": True,
                "massage": "SuccessFull deleted"
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response({
                "status": False,
                "massage": "books is not fount",
            }, status.HTTP_400_BAD_REQUEST)


class BookViewSet(viewsets.ModelViewSet):
    queryset = BooksModel
    serializer_class = BookSerializer
