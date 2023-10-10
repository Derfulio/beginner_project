from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class PythonPageView(TemplateView):
    template_name = "python.html"


class FsharpPageView(TemplateView):
    template_name = "fsharp.html"


class CsharpPageView(TemplateView):
    template_name = "csharp.html"


class CPageView(TemplateView):
    template_name = "c.html"


class CppPageView(TemplateView):
    template_name = "cpp.html"


class JavaPageView(TemplateView):
    template_name = "java.html"


class RacketPageView(TemplateView):
    template_name = "racket.html"
