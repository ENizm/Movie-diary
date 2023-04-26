from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about-us', views.about, name='about'),
    path('addfilm', views.addfilm, name='addfilm'),
    path('<int:pk>', views.FilmsDetailView.as_view(), name='films-detail'),
    path('<int:pk>/update', views.FilmsUpdateView.as_view(), name='films-update'),
    path('<int:pk>/delete', views.FilmsDeleteView.as_view(), name='films-delete')
]