from django.shortcuts import render
from django.views import View
from dumcrown.forms import RegisterForm


class SingUpView(View):

    def get(self, request):
        print('get')
        return render(request, 'singup.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            created_account = True
            context = {'created_account': created_account, }

            return render(
                request,
                'singup.html',
                context,
            )
        else:
            return render(request, 'singup.html', {'form': form})
