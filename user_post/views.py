from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from django.views import generic
from .forms import SignUpForm, PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.


class PostList(generic.ListView):
    '''
    this is view class for postlist which is inhereting from generic listview
    '''

    # get all objects from model post
    queryset = Post.objects.order_by('-created_at')

    # html template to render all post model objects
    template_name = 'postlist.html'
    context_object_name = 'list'


class DetailPost(generic.DetailView):
    '''
    this is view class for post detail which is inhereting from generic detailview
    '''
    model = Post
    template_name = 'detailpost.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


def SignUp(request):
    '''
    this view function is for making sign up backend logic with all the validations and fields
    '''

    # checking request is for post or not
    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():
            # if form is valid then saving in user model
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. Click login button to login")
            return redirect('register')
        else:

            messages.error(request, "Registration unsuccesful.")
    form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def Login(request):
    '''
    this view function is for login user
    '''
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        # use authenticate method to check post parameters are matching or not
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("PostList")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return render(request, 'login.html')

    return render(request, 'login.html')

# require login to create new post
@login_required(login_url='/login/')
def CreatePost(request):
    '''
    view function to create a post view without login it is not working
    '''
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Your post successfully posted')
            return redirect('PostList')
        else:

            messages.error(request, 'Please fill all the fields')
    form = PostForm()
    return render(request, 'create.html', {'form': form})


def Logout(request):
    '''
    simple logout function
    '''
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')

