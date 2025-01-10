from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import CategoryForm
from .models import Category
from .forms import TransactionForm
from .models import Transaction
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from .models import SavingsGoal
from .forms import SavingsGoalForm



def home(request):
    return render(request,'finance/index.html')

def login_user(request):
    if request.method=='POST':
        forms=AuthenticationForm(data=request.POST)
        if forms.is_valid():
            username=forms.cleaned_data['username']
            password=forms.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/dashboard/')
        return HttpResponseRedirect('/login/')
        
    forms=AuthenticationForm()
    return render(request,'finance/login.html',{'forms':forms})

def signup(request):
    if request.method=='POST':
        forms=UserCreationForm(request.POST)
        if forms.is_valid:
            forms.save()
            return HttpResponseRedirect('/login/')
    forms=UserCreationForm()
    return render(request,'finance/signup.html',{'forms':forms})

@login_required
def dashboard(request):
    category=Category.objects.filter(user=request.user)
    transaction=Transaction.objects.filter(user=request.user).order_by('-date')
    savings_goals = SavingsGoal.objects.filter(user=request.user)


    return render(request,'finance/dashboard.html',{'category':category,'transactions':transaction,'savings_goals':savings_goals})


@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return HttpResponseRedirect('/dashboard/')  
    else:
        form = CategoryForm()

    return render(request, 'finance/forms.html', {'form': form,'heading':'CATEGORY'})



@login_required
def manage_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'finance/forms.html', {'form': form,'heading':'PROFILE'})



@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return HttpResponseRedirect('/dashboard/') 
    else:
        form = TransactionForm()

    return render(request, 'finance/forms.html', {'form': form,'heading':'TRANSACTION'})




@login_required
def update_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'finance/forms.html', {'form': form,'heading':'TRANSACTION'})

@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('/dashboard/')

    return render(request, 'finance/dashboard.html', {'transaction': transaction})

@login_required
def create_savings_goal(request):
    if request.method == "POST":
        form = SavingsGoalForm(request.POST)
        if form.is_valid():
            savings_goal = form.save(commit=False)
            savings_goal.user = request.user
            savings_goal.save()
            return redirect("/dashboard/")
    else:
        form = SavingsGoalForm()
    return render(request, "finance/forms.html", {"form": form,'heading':'SAVING GOAL'})

@login_required
def update_savings_goal(request, id):
    savings_goal = get_object_or_404(SavingsGoal, id=id, user=request.user)
    if request.method == "POST":
        form = SavingsGoalForm(request.POST, instance=savings_goal)
        if form.is_valid():
            form.save()
            return redirect("/dashboard/")
    else:
        form = SavingsGoalForm(instance=savings_goal)
    return render(request, "finance/forms.html", {"form": form})

@login_required
def delete_savings_goal(request, id):
    savings_goal = get_object_or_404(SavingsGoal, id=id, user=request.user)
    if request.method == "POST":
        savings_goal.delete()
        return redirect("/dashboard/")
    return render(request, "finance/dashboard.html", {"savings_goal":savings_goal})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')