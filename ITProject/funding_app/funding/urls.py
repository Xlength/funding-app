from django.urls import path
from .views import index, register, login_view, logout_view, apply_funding, funding_success, view_applications, review_funding, approve_or_reject, dashboard, user_settings

urlpatterns = [
    path('', index, name='index'), 
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('apply/', apply_funding, name='apply_funding'),  # 资金申请页面
    path('success/', funding_success, name='funding_success'),
    path('view_applications/', view_applications, name='view_applications'), 
    path('admin/review/', review_funding, name='review_funding'),
    path('admin/review/<int:application_id>/', approve_or_reject, name='approve_or_reject'),
    path('dashboard/', dashboard, name='dashboard'),
    path('settings/', user_settings, name='user_settings'),
]
