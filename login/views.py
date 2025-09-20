from django.shortcuts import render, redirect
from django.http import HttpResponse
from pages.models import Clint
from django.contrib import messages

def login(request):
    # إذا كان طلب GET، فقط اعرض الصفحة
    if request.method != 'POST':
        return render(request, 'login/login.html', {'name': 'adel101'})
    
    # معالجة طلب POST
    user_name = request.POST.get('user_name', '').strip()
    password = request.POST.get('password', '').strip()
    phone = request.POST.get('phone', '').strip()
    image = request.FILES.get('image')
    
    # التحقق من البيانات المطلوبة
    if not user_name:
        messages.error(request, 'اسم المستخدم مطلوب')
        return render(request, 'login/login.html')
    
    if not password:
        messages.error(request, 'كلمة المرور مطلوبة')
        return render(request, 'login/login.html')
    
    try:
        # إنشاء وحفظ المستخدم
        clint = Clint.objects.create(
            name=user_name,
            password=password,
            phone=phone,
            image=image
        )
        
        messages.success(request, f'تم إنشاء الحساب بنجاح لـ {user_name}')
        return redirect('home')  # توجيه إلى الصفحة الرئيسية
        
    except Exception as e:
        messages.error(request, f'حدث خطأ: {str(e)}')
        return render(request, 'login/login.html')