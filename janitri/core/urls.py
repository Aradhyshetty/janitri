from django.urls import path
from .views import *
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("add_patient/", add_patient, name="add_patient"),
    path("record_heart_rate/<int:patient_id>/", record_heart_rate, name="record_heart_rate"),
    path("get_heart_rates/<int:patient_id>/", get_heart_rates, name="get_heart_rates"),
]