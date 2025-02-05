from django.urls import path
from .views import (
    base, home, aboutCottonMove, aboutPlatform, news, 
    disposeHere, circularEconomy, traceability, contact, faq
)

urlpatterns = [
    path("", home, name="home"),
    path("about/cotton-move/", aboutCottonMove, name="about_cotton_move"),
    path("about/platform/", aboutPlatform, name="about_platform"),
    path("news/", news, name="news"),
    path("dispose-here/", disposeHere, name="dispose_here"),
    path("circular-economy/", circularEconomy, name="circular_economy"),
    path("traceability/", traceability, name="traceability"),
    path("contact/", contact, name="contact"),
    path("faq/", faq, name="faq"),
]

