from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
class HomePage(TemplateView):
    template_name="index.html"


class ThanksPage(TemplateView):
    template_name="thanks.html"

class AboutPage(TemplateView):
    template_name="about.html"

#class MyLoginView(auth_views.LoginView):
#        template_name='Exp_trac_app/login.html'
#        redirect_authenticated_user=True
#        def get(self, request, *args, **kwargs):
#            if self.request.user.is_authenticated:
#                return redirect('{}'.format(self.request.GET.get('next', 'index')))

#            return super(MyLoginView, self).get(request, *args, **kwargs)
