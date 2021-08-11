from django import forms
from django.contrib.auth.models import User

#フォームクラス作成
class UserForm(forms.ModelForm):
    #パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        #ユーザー認証
        model = User
        #フィールド指定
        fields = ('username','password',)
        #フィールド名指定
        labels = {'username':"ユーザーID",}
