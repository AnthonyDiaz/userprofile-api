from rest_framework import viewsets, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response


from user_profile.models import User
from user_profile.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow users to be viewed, create, and edited.
    """
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name']

    def get_queryset(self):
        """
        Allow to GET a param, 'q', to be used against the search field
        """
        queryset = super(viewsets.ModelViewSet, self).get_queryset().order_by('first_name')

        if self.request.GET.get('q', None):
            return queryset.filter(username__icontains=self.request.GET['q'])
        return queryset

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


    # def partial_update(self, request, pk=None):
    #     pass
