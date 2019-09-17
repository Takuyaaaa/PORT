from django import forms
from .models import Security,Description

#index.htmlの検索フォーム
class SearchForm(forms.Form):
    keyword = forms.CharField(label='Search by Asset Class ',max_length=100)


#index.html >> Addの新規銘柄追加フォーム
class SecurityForm(forms.ModelForm):
    class Meta:
        model = Security
        fields = ('des','asset','price','position')


#detail.htmlにおけるDescriptionモデル自動生成フォーム
class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Description
        fields = ('name',)


#edit.html >> Rebalanceの銘柄編集フォーム
class RebalanceForm(forms.ModelForm):
    class Meta:
        model = Security
        fields = ('price','position')


#detail.html >> Edit Description Infoの情報編集フォーム
class Des_updateForm(forms.ModelForm):
    class Meta:
        model = Description
        fields = ('sector','country','business')
