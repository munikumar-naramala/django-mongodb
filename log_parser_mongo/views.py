from rest_framework import routers, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import LogParserMongo
from .serializer import LogSerializer


class LogmongoViewSet(viewsets.ModelViewSet):
    queryset = LogParserMongo.objects.all()
    serializer_class = LogSerializer

    @action(detail=True, methods=['post'])
    def logparser_read(self, request, pk=None):
        logmongo = self.get_object()
        logmongo.is_read = True
        logmongo.save()
        return Response({'status': 'success'})

    @action(detail=False, methods=['post'])
    def logparser_unread(self, request):
        queryset = self.get_queryset().filter(is_read=True)
        queryset.update(is_read=False)
        return Response({'status': 'success'})

    def get_queryset(self):
        # Filter the queryset based on query params
        queryset = super().get_queryset()
        is_read = self.request.query_params.get('is_read', None)
        if is_read is not None:
            queryset = queryset.filter(is_read=is_read)
        return queryset
