from django.urls import path
from .views import HomePage, AboutPage, MySkills, AboutDetailsPage, PortFolio_View
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('details/<int:pk>/', AboutDetailsPage.as_view(), name='details'),
    path('about/', AboutPage.as_view(), name='about'),
    path('skills/', MySkills.as_view(), name='skills'),
    path('portfolio/', PortFolio_View.as_view(), name='portfolio'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)