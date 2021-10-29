from django.urls import path
from usuarios import views as v

app_name = "aplication"
urlpatterns = [
    path('', v.inicio, name = "inicio"),
    path ( "detalle_<int:id>/", v.detalle, name = "detalle"),
    path ('create/', v.create_user, name = "create"),
    path ('editar_<int:id>/', v.update_user, name = "update"),
    path ('delete_<int:id>/', v.delete, name = "delete")
]
