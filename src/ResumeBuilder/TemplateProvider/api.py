from tastypie.resources import ModelResource
from TemplateProvider.models import Templates

class TemplatesResource(ModelResource):
	class Meta:
		queryset = Templates.objects.all()
		resource_name = 'entry'