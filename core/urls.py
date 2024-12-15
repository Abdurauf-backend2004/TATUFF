
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('bino/',bino_view,name='bino'),
    path('fakultet/',fakultet_view,name='fakultet'),
    path('yonalish/',yonalishlar_view,name='yonalish'),
    path('yonalish/<int:yonalish_id>/',yonalish_index_view),
    path('kafedra/',kafedra_view,name='kafedra'),
    path('kafedra-mudiri/', kafedra_mudiri_view,name='kafedra_mudiri'),
    path('ustozlar/', ustoz_view,name='ustozlar'),
    path('talabalar/', talaba_view,name='talabalar'),
    path('titurlar/',titur_view,name='titurlar'),
    path('guruhlar/',guruh_view,name='guruhlar'),
    path('talabalar/<int:talaba_id>/',talaba_index_view),
    path('bino/<int:bino_id>/',bino_index_view),
    path('fakultet/<int:fakultet_id>/',fakultet_index_view),
    path('kafedra/<int:kafedra_id>/',kafedra_index_view),
    path('kafedra-mudiri/<int:kafedra_mudiri_id>/', kafedra_mudiri_index_view),
    path('ustozlar/<int:ustoz_id>/', ustoz_index_view),
    path('titurlar/<int:titur_id>/', titur_index_view),
    path('guruhlar/<int:guruh_id>/', guruh_index_view),
    path('talabalar/<int:talaba_id>/delete/', talaba_delete_view),
    path('bino/<int:bino_id>/delete/', bino_delete_view),
    path('fakultet/<int:fakultet_id>/delete/', fakultet_delete_view),
    path('yonalish/<int:yonalish_id>/delete/', yonalish_delete_view),
    path('kafedra/<int:kafedra_id>/delete/',kafedra_delete_view),
    path('kafedra-mudiri/<int:kafedra_mudiri_id>/delete/',kafedra_mudiri_delete_view),
    path('ustozlar/<int:ustoz_id>/delete/',ustoz_delete_view),
    path('titurlar/<int:titur_id>/delete/',titur_delete_view),
    path('guruhlar/<int:guruh_id>/delete/',guruh_delete_view),
]
