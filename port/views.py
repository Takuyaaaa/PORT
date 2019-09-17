from django.shortcuts import render, get_object_or_404
from .models import Security,Description
from .forms import SearchForm,RebalanceForm,SecurityForm,DescriptionForm,Des_updateForm



#index.htmlのページに対応
def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        securities = Security.objects.filter(asset__contains=keyword)
    else:
        searchForm = SearchForm()
        securities = Security.objects.all()
    context = {
        'securities':securities,
        'searchform':searchForm,
    }
    return render(request, 'port/index.html',context)


#detail.htmlのページに対応
def detail(request,id):
    security = get_object_or_404(Security, pk=id)
    #Securityモデルに対応するDescriptionモデルのデータベースを自動生成
    try:
        description = Description.objects.get(name_id=id)
    except Description.DoesNotExist:
        descriptionForm = DescriptionForm({'name':id})
        description = descriptionForm.save()
    context = {
        'security':security,
        'description':description,
    }
    return render(request, 'port/detail.html',context)


#index.html >> Addボタン >> new.htmlに対応
def new(request):
    securityForm = SecurityForm()
    context = {
        'message':'Add a New Security',
        'securityForm':securityForm,
    }
    return render(request, 'port/new.html',context)

#new.htmlのフォームから入力を受け、実際にSecurityモデルにデータを追加
def create(request):
    if request.method == 'POST':
        securityForm = SecurityForm(request.POST)
        if securityForm.is_valid():
            security=securityForm.save()
    context = {
        'security': security,
    }
    #create URLでも、index.htmlを表示できるようindexファンクションの構成を付記。
    #Create後のurlを直接indexビューにするのがベストだが、、、、
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        securities = Security.objects.filter(asset__contains=keyword)
    else:
        searchForm = SearchForm()
        securities = Security.objects.all()
    context = {
        'securities':securities,
        'searchform':searchForm,
    }
    return render(request, 'port/index.html', context)


#detail.html >> Rebalanceボタン >> edit.htmlに対応
def edit(request,id):
    security = get_object_or_404(Security, pk=id)
    rebalanceForm = RebalanceForm(instance=security)
    context = {
        'message':'Rebalance a Position',
        'security':security,
        'rebalanceForm':rebalanceForm,
    }
    return render(request, 'port/edit.html',context)

#edit.htmlのフォームから入力を受け、実際にSecurityモデルのデータを編集
def update(request,id):
    if request.method == 'POST':
        security = get_object_or_404(Security, pk=id)
        rebalanceForm = RebalanceForm(request.POST, instance=security)
        if rebalanceForm.is_valid():
            rebalanceForm.save()
    try:
        description = Description.objects.get(name_id=id)
    except Description.DoesNotExist:
        description = None
    context = {
        'security':security,
        'description':description,
    }
    return render(request, 'port/detail.html',context)


#detail.html >> Removeボタン >> confirm_delete.htmlに対応
def confirm_delete(request,id):
    security = get_object_or_404(Security, pk=id)
    context ={
        'security':security,
    }
    return render(request, 'port/confirm_delete.html',context)

#confirm_delete.htmlの入力を受けて実際にecurityモデルからデータを消去
def delete(request,id):
    security = get_object_or_404(Security, pk=id)
    security.delete()
    securities = Security.objects.all()
    context = {
        'message':'Delete Security ' + str(id),
        'securities':securities,
    }
    return render(request, 'port/index.html',context)


#detail.html >> Edit Description Infoリンク >> des_edit.htmlに対応
def des_edit(request,id):
    security = get_object_or_404(Description,name_id=id)
    des_updateForm = Des_updateForm(instance=security)
    if des_updateForm.is_valid():
        des_updateForm.save()
    context = {
        'message':'Edit Description info',
        'security':security,
        'des_updateForm':des_updateForm,
    }
    return render(request, 'port/des_edit.html',context)

#des_edit.htmlの入力を受け、実際にDescriptionモデルのデータを編集
def des_update(request,id):
    if request.method == 'POST':
        security = get_object_or_404(Security, pk=id)
        description = get_object_or_404(Description,name_id=id)
        des_updateForm = Des_updateForm(request.POST,instance=description)
        if des_updateForm.is_valid():
            des_updateForm.save()
    context = {
        'description':description,
        'security':security,
        'des_updateForm':des_updateForm,
    }
    return render(request,'port/detail.html',context)
