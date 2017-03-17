from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from LanguageExchange.forms import UserCreationForm,UserChangeForm
from registration.backends.simple.views import RegistrationView


def about(request):
    
    return render(request, 'LanguageExchange/about.html')

def contact(request):
   
    return render(request, 'LanguageExchange/contact.html')    

@login_required    
def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'LanguageExchange/index.html', context=context_dict)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserCreationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and
            # put it in the UserProfile model.
            user.save()
            if 'picture' in request.FILES:
                user.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            user.save()
            registered = True
        
        else:
            print(user_form.errors)

    else:
        user_form = UserCreationForm()
        
    return render(request,
                'LanguageExchange/register.html',
                {'user_form': UserCreationForm,
                'registered': registered})

                
                
@login_required                 
def edit_information(request):
    edited = False

    if request.method == 'POST':
       
        change_form = UserChangeForm(data=request.POST)
        if change_form.is_valid():
           
            #user = change_form.save()
            user = request.user
            user.set_password(change_form.cleaned_data['password1'])
            user.Mother_language = change_form.cleaned_data['Mother_language']
            user.Wish_language = change_form.cleaned_data['Wish_language']
           
            user.save()
            return render(request, 'LanguageExchange/index.html')
           
            #user.set_password(user.password)
            user.save()

        #if change_form.is_valid():    
        #    change = change_form.save()
        #    change.set_password(user.password)
        #    change.user = user
            edited = True
        
        else:
          
            print(change_form.errors)

    else:
       
       
        change_form = UserChangeForm()

    return render(request,
                'LanguageExchange/edit.html',
                {'change_form': UserChangeForm,
                'edited': edited})
                
             
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
              
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
           
            else:
               
                return HttpResponseRedirect(reverse('register'))	
        else:
            
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponseRedirect(reverse('register'))	
   
    else:
     
        return render(request, 'LanguageExchange/login.html', {})

@login_required
def user_logout(request):
    # since we know user is already logged in
    logout(request)
    # take user back to homepage
    return HttpResponseRedirect(reverse('register'))	

class MyRegistrationView(RegistrationView):
    def get_success_url(self,user):
        return '/LanguageExchange/'

        


def search(request):
    serch_form =Searchform(data=request.POST)
    result=None
    if request.method == 'POST':
        if serch_form.is_valid():
            results = Searchform.objects.all()
        

        search = request.POST.get('q', None)
        if search:
            results = results.filter(Q(Mother_language=search))
            result.save()
        
            
        Mother_language = request.POST.get('Mother_language', None)
        if Mother_language:
            results = results.filter(Mother_language__icontain=search)    
            
       

        return render_to_response('index.html', {'form': Searchform(request.POST), 'results': results})

    return render('index.html', {'form': Searchform, 'results': results})