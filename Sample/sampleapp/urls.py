from django.urls import path
from sampleapp import views

urlpatterns = [
    path('',views.home_fun),
    path('add',views.add_fun),
    path('show',views.show_fun,name='show'),
    path('update<int:sampleid>',views.update_fun,name='update'),
    path('delete<int:sampleid>',views.delete_fun,name='delete')
]