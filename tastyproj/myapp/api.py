from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.api import Api

from tastypie.authentication import Authentication
from tastypie.authorization import Authorization

from .models import MyModel, MyExtraModel


class MyModelResource(ModelResource):
    myextramodel = fields.ToOneField('tastyproj.myapp.api.MyExtraModelResource',
                              'myextramodel', related_name='mymodel',
                              full=True, null=True, blank=True)

    class Meta:
        queryset = MyModel.objects.all()
        resource_name = 'mymodel'
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True


class MyExtraModelResource(ModelResource):
    mymodel = fields.ToOneField(MyModelResource,
                                'mymodel', related_name='myextramodel')

    class Meta:
        queryset = MyExtraModel.objects.all()
        resource_name = 'myextramodel'
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True


v1_api = Api(api_name='v1')
v1_api.register(MyModelResource())
v1_api.register(MyExtraModelResource())
