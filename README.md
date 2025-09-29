main 상위 폴더의 urls.py 파일에서 main.urls도 include했고, setting 파일에서 main 앱 또한 추가했습니다.
해당 설정 파일들은 내용이 방대하여 따로 건든 부분만 README에 혹시 몰라 추가했습니다.
감사합니다.

#urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls'))
]
#settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]
