from django.shortcuts import render, redirect
from pages.models import Market
from django.contrib import messages

def market_login(request):
    if request.method == 'POST':
        # الحصول على البيانات مباشرة من request.POST
        market_name = request.POST.get('market_name', '').strip()
        place = request.POST.get('place', '').strip()
        
        print(f"📝 البيانات المستلمة: {market_name} - {place}")
        
        # التحقق من صحة البيانات يدوياً
        if not market_name:
            messages.error(request, '⚠️ اسم الفرع مطلوب')
            
        if not place:
            messages.error(request, '⚠️ المكان مطلوب')
        
        # إذا كان هناك أخطاء، أعد عرض الصفحة
        if messages.get_messages(request):
            return render(request, 'market_login/market_login.html', {
                'market_name': market_name,
                'place': place
            })
        
        # محاولة حفظ البيانات في قاعدة البيانات
        try:
            market = Market.objects.create(
                name=market_name,
                place=place
            )
            print(f"✅ تم إنشاء الفرع: {market_name} في {place}")
            messages.success(request, f'تم إنشاء الفرع "{market_name}" بنجاح!')
            return redirect('index')  # غير هذا إلى اسم URL الخاص بك
            
        except Exception as e:
            print(f"❌ خطأ في الحفظ: {e}")
            messages.error(request, f'حدث خطأ: {str(e)}')
            return render(request, 'market_login/market_login.html', {
                'market_name': market_name,
                'place': place
            })
    
    else:
        # إذا كان طلب GET، عرض الصفحة فارغة
        print("📄 عرض صفحة تسجيل الفرع")
        return render(request, 'market_login/market_login.html')