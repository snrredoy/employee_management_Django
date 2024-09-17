from django.urls import path, include

from .views import (
    HomeView,
    EmployeeDetail,
    CreateEmployee,
    EmployeeUpdateView,
    EmployeeDeleteView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("detail/<int:pk> /", EmployeeDetail.as_view(), name="detail"),
    path("create/", CreateEmployee.as_view(), name="create"),
    path("update/<int:pk>/", EmployeeUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", EmployeeDeleteView.as_view(), name="delete"),
]
