from django.shortcuts import render, redirect
""" django.shortcuts :-this package collects some functions and classes,
render:-Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
render() is the same as a call to render_to_response()

Example:

 return render(request,
                      'home.html',
                      {'auth_form': auth_form, 'user_form': user_form, })

"""

from django.contrib.auth import login, authenticate, logout
""" django.contrib.auth:-contains inbuilt functions and classes and all the authentication framework, and its default models.
It handles user accounts(username(with given size),password, Email validation etc.), groups, permissions and cookie-based user sessions

I have used Login ,logout and also checked authentication  by importing login, authenticate, logout form  django.contrib.auth"""

from django.contrib.auth.decorators import login_required
"""django.contrib.auth.decorators:-i have import login_required() :If the user isnot logged in, redirect to
settings.LOGIN_URL, passing the current absolute path in the query string.
Example: If the user is logged in, execute the view normally. The view code is free to assume the user is logged in.
"""

from django.db.models import Count
"""django.db.models:-A model is the single, definitive source of information about your data.
For Example Here:
in models.py file of k_twitter_app it contents k_twitter models and UserProfiles models for which it create table
automatically in database.

here I have import 'count' so that I can count number of followers and following and number of tweets in k_twitter_app
"""
from k_twitter_app.forms import AuthForm, UserForm, K_twitterForm
""" A Django Form is responsible for taking some user input, validating it, and turning it into Python objects.
in forms.py  I have created UserForm() Class to take user input for signUp  is_valid() function check validity and AuthForm
() class to authenticate form which i have imported"""

from django.contrib.auth.models import User
""" django.contrib.auth:-contains the core of the authentication framework, and its default models.
It handles user accounts, groups, permissions and cookie-based user sessions
"""
from django.http import Http404
"""Django provides an Http404 exception. If you raise Http404 at any point in a view function, Django will catch
it and return the standard error page for your application, along with an HTTP error code 404. """

from k_twitter_app.models import K_twitter
"""models.py:k_twitter() class have content (max character 100 ),user , creation_data create table
automatically in database  and this User() class has imported.
"""
from django.core.exceptions import ObjectDoesNotExist
"""Django core exception classes are defined in django.core.exceptions.
1.ObjectDoesNotExist
2. DoesNotExist
"""


# Create your views here.
def index(request, auth_form=None, user_form=None):
    # User is logged in
    if request.user.is_authenticated():
        k_twitter_form = K_twitterForm()
        user = request.user
        k_twitters_self = K_twitter.objects.filter(user=user.id)
        k_twitters_buddies = K_twitter.objects.filter(user__userprofile__in=user.profile.follows.all)
        k_twitters = k_twitters_self | k_twitters_buddies

        return render(request,
                      'friends.html',
                      {'k_twitter_form': k_twitter_form, 'user': user,
                       'k_twitters': k_twitters,
                       'next_url': '/', })
    else:
        # User is not logged in
        auth_form = auth_form or AuthForm()
        user_form = user_form or UserForm()

        return render(request,
                      'home.html',
                      {'auth_form': auth_form, 'user_form': user_form, })

""" auth_form and user_form is variable of forms.py file where code for signup is
written and value stored in databases.frist value of usenane and password is authenti
-cated which code is written in forms.py

if authentication is successful go to friends.html otherwise it still lie on home.html
"""

def login_view(request):
    if request.method == 'POST':
        form = AuthForm(data=request.POST)#authenticate logn data
        if form.is_valid():
            login(request, form.get_user())
            # Success
            return redirect('/')
        else:
            # Failure
            return index(request, auth_form=form)
    return redirect('/')

""" In function login_view() take input from 'POST' method and call AuthForm() function
and return result in 'form' if  form is valir i.e if usrname and password lie in database
it return True and call function login(request, form.get_user()) if False then call
fuction index(request, auth_form=form)"""


def logout_view(request):
    logout(request)
    return redirect('/')
"""this function called when logout button is clicked ,fuction call logout(request)
"""

def signup(request):
    user_form = UserForm(data=request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return index(request, user_form=user_form)
    return redirect('/')

""" In function signup(request)  , in variable user_form ,take all data entered in
function UserForm(data=request.POST) , is_valid() function check data is valid or not
i.e email is valid or not password1 and password2 matched or not etc. if user_form.is_valid() return
true, in username and password take username and password entered in signup form ,also
save data in database, call function authenticate(username=username, password=password) to check
validity of username and password and call function login(request, user) otherwise
stay on base.html i.e call index(request, user_form=user_form)
"""

def public(request, k_twitter_form=None):
    k_twitter_form = k_twitter_form or K_twitterForm()
    k_twitters = K_twitter.objects.reverse()[:10]
    return render(request,
                  'public_tweets.html',
                  {'k_twitter_form': k_twitter_form, 'next_url': '/k_twitters',
                   'k_twitters': k_twitters, 'username': request.user.username})


"""this funtion display all tweets posted my public whom user follow. """

def submit(request):
    if request.method == "POST":
        k_twitter_form = K_twitterForm(data=request.POST)
        next_url = request.POST.get("next_url", "/")
        if k_twitter_form.is_valid():
            k_twitter = k_twitter_form.save(commit=False)
            k_twitter.user = request.user
            k_twitter.save()
            return redirect(next_url)
        else:
            return public(request, k_twitter_form)
    return redirect('/')


def get_latest(user):
    try:
        return user.k_twitter_set.order_by('id').reverse()[0]
    except IndexError:
        return ""



def users(request, username="", k_twitter_form=None):
    if username:
        # Show a profile
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
        k_twitters = K_twitter.objects.filter(user=user.id)
        if username == request.user.username or request.user.profile.follows.filter(user__username=username):
            # Self Profile
            return render(request, 'user_profile.html', {'user': user, 'k_twitters': k_twitters, })
        return render(request, 'user_profile.html', {'user': user, 'k_twitters': k_twitters, 'follow': True, })
    users = User.objects.all().annotate(k_twitter_count=Count('k_twitter'))
    k_twitters = map(get_latest, users)
    obj = zip(users, k_twitters)
    k_twitter_form = k_twitter_form or K_twitterForm()
    return render(request,
                  'All_profiles_.html',
                  {'obj': obj, 'next_url': '/users/',
                   'k_twitter_form': k_twitter_form,
                   'username': request.user.username, })



def follow(request):
    if request.method == "POST":
        follow_id = request.POST.get('follow', False)
        if follow_id:
            try:
                user = User.objects.get(id=follow_id)
                request.user.profile.follows.add(user.profile)
            except ObjectDoesNotExist:
                return redirect('/users/')
    return redirect('/users/')
