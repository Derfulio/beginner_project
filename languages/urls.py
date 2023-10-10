from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    JavaPageView,
    CppPageView,
    CPageView,
    CsharpPageView,
    FsharpPageView,
    PythonPageView,
    RacketPageView,
)

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("fsharp/", FsharpPageView.as_view(), name="fsharp"),
    path("csharp/", CsharpPageView.as_view(), name="csharp"),
    path("cpp/", CppPageView.as_view(), name="cpp"),
    path("c/", CPageView.as_view(), name="c"),
    path("java/", JavaPageView.as_view(), name="java"),
    path("python/", PythonPageView.as_view(), name="python"),
    path("racket/", RacketPageView.as_view(), name="racket"),
    path("", HomePageView.as_view(), name="home"),
]
