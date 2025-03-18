cd funding_app
python manage.py runserver
#执行测试
python manage.py test

用户登录后，访问自己的申请
访问 http://127.0.0.1:8000/accounts/login/ 进行登录
访问 http://127.0.0.1:8000/funding/apply/ 提交资金申请
访问 http://127.0.0.1:8000/funding/view_applications/查看自己的申请状态
访问 http://127.0.0.1:8000/funding/dashboard/ 查看统计数据管理员审核流程

username:zhangzhixing
pwd:zhangzhixing

管理员登录 http://127.0.0.1:8000/admin/ 访问后台

html路径：funding_app\funding\templates\funding\apply_funding.html