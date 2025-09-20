from django.shortcuts import render, redirect
from .forms import Market_login
from pages.models import Market  # استيراد النموذج إذا كنت تريد الحفظ

def market_login(request):
    if request.method == 'POST':
        form = Market_login(request.POST)
        if form.is_valid():
            # استخراج البيانات النظيفة
            market_name = form.cleaned_data['market_name']
            place = form.cleaned_data['place']
            
            try:
                # حفظ البيانات في قاعدة البيانات
                market = Market.objects.create(
                    name=market_name,
                    place=place
                )
                print(f"✅ تم إنشاء فرع جديد: {market_name} - {place}")
                
                # توجيه إلى صفحة النجاح أو العرض
                return redirect('market_success')  # تحتاج إلى تعريف هذا المسار
                
            except Exception as e:
                print(f"❌ خطأ في الحفظ: {e}")
                # يمكنك إضافة رسالة خطأ هنا
                
    else:
        form = Market_login()
    
    return render(request, 'market_login/market_login.html', {'form': form})