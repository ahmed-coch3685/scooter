from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings
User=settings.AUTH_USER_MODEL
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from .forms import *

from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth import login,authenticate,logout




#regst
def register(request):
    if request.method == "POST" and "regist" in request.POST:
        em = request.POST.get("em")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not em or not username or not password:
            error = "جميع الحقول مطلوبة"
            return render(request, "registrations/lo_re.html", {"error": error})

        if User.objects.filter(username=username).exists():
            error = "اسم المستخدم موجود بالفعل"
            return render(request, "registrations/lo_re.html", {"error": error})

        # إنشاء المستخدم
        user = User.objects.create_user(
            username=username,
            password=password,
            email=em
        )
        user.is_active = False
        user.save()

        # إرسال إيميل التفعيل
        current_site = get_current_site(request)
        subject = "تفعيل الحساب"
        message = render_to_string("registrations/emails/resetPass_em.html", {
            "user": user,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": default_token_generator.make_token(user),
        })

        email = EmailMessage(subject, message, to=[em])
        email.send()

        return render(request, "registrations/emails/check_email.html")
    
    return render(request, "registrations/lo_re.html")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("acc:login")
    else:
        error = "رابط التفعيل غير صالح أو منتهي"
        return render(request, "registrations/emails/activation_failed.html", {"error": error})


def logout_bl(request):
    logout(request)
    return redirect("acc:login")

def login_bl(request):
    if request.method == "POST" and "login" in request.POST:
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("pro:home")
        else:
            erro="name or pass false"
            return render(request,"registrations/lo_re.html",{"erro":erro})
    else:
        return render(request,"registrations/lo_re.html")



class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    def form_valid(self, form):
        response = super().form_valid(form)
        # تسجيل الدخول تلقائياً
        user = form.user
        login(self.request, user)
        return response



def profile(request):

    return render(request, 'registrations/profile.html')




def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=user
        )
        if form.is_valid():
            form.save()
            return redirect('acc:profile')
    else:
        form = ProfileUpdateForm(instance=user)

    return render(request, 'registrations/edit_profile.html', {
        'form': form
    })



def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)      # تسجيل خروج
        user.delete()        # حذف الحساب
        return redirect('acc:login')

    return render(request, 'registrations/delete_account.html')