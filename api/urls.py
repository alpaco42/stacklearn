from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.urls import path
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
			model = User
			fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	# overwrite the get_object method so that `@me` returns the currently
	# logged in user.
	def get_object(self):
		pk = self.kwargs.get('pk')

		if pk == "@me":
			return self.request.user

		return super(UserViewSet, self).get_object()

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
	path('', include(router.urls))
]
