from django.contrib import admin
from django.urls import path
from auapp.views import user_login, user_signup, user_logout, user_np, about_me
from quizapp.views import home, takequiz, deletequiz, submitquiz, newquiz, newquestion, results, report, aboutme
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Login App
    path('admin/', admin.site.urls),
    path("user_login/", user_login, name="user_login"),
    path("user_signup/", user_signup, name="user_signup"),
    path("user_logout/", user_logout, name="user_logout"),
    path("user_np/", user_np, name="user_np"),
    path("about_me/", about_me, name="about_me"),

    # Main Project
    path("", home, name="home"),
    path("deletequiz/<quiz_id>", deletequiz, name="deletequiz"),
    path("takequiz/<quiz_id>", takequiz, name="takequiz"),
    path("takequiz/<quiz_id>/submit", submitquiz, name="submitquiz"),
    path("newquiz/", newquiz, name="newquiz"),
    path("newquiz/<quiz_id>/newquestion", newquestion, name="newquestion"),
    path("results/", results, name="results"),
    path("results/<quiz_id>/report", report, name="report"),
    path("aboutme/", aboutme, name="aboutme"),
]

urlpatterns += staticfiles_urlpatterns()
