from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
import models


class TodoResource(ModelResource):
    class Meta:
        authorization = Authorization()
        queryset = models.Todo.objects.all()
        resource_name = 'todos'
