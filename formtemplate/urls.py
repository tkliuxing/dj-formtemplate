from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api


router = DefaultRouter()

router.register(r'formdatadefine', api.FormDataDefineViewSet)
router.register(r'formfields', api.FormFieldsViewSet)
router.register(r'formtemplate', api.FormTemplateViewSet)
router.register(r'formdata', api.FormDataViewSet)
router.register(r'formdatareportconf', api.FormDataReportConfViewSet)

urlpatterns = (
    path('api/v1/', include(router.urls)),
)
