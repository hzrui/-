from django import forms
from django.core import validators

from sup_uesr.helper import set_password
from sup_uesr.models import Users


class RegisterForm(forms.ModelForm):
    # 确认密码
    repassword = forms.CharField(max_length=16,
                                 min_length=6,
                                 error_messages={
                                     'required': "请填写确认密码",
                                 },
                                 widget=forms.PasswordInput(attrs={
                                     "class": "login-password",
                                     "placeholder": "请输入确认密码"
                                 }
                                 ),
                                 )

    class Meta:
        model = Users
        fields = ['phone', 'password']

        widgets = {
            "phone": forms.TextInput(attrs={"class": "login-name", "placeholder": "请输入手机号码"}),
            "password": forms.PasswordInput(attrs={"class": "login-password", "placeholder": "请输入密码"}),
        }

    error_messages = {
        "phone": {
            "required": "请填写手机号!"
        },
        "password": {
            "required": "请填写密码!",
            "min_length": "密码必须大于6个字符!",
            "max_length": "密码必须小于16个字符!",
        }
    }

    def __init__(self, *args, **kwargs):
        # 调用父类方法
        super().__init__(*args, **kwargs)
        # 自定义验证密码长度6-16位
        self.fields['password'].validators.append(validators.MinLengthValidator(6))
        self.fields['password'].validators.append(validators.MaxLengthValidator(16))

    # 自定义方法 验证单个验证
    def clean_phone(self):
        # 验证手机号码是否被注册
        phone = self.cleaned_data.get('phone')  # 把手机号传入

        # 数据库查询
        rs = Users.objects.filter(phone=phone).exists()
        # 如果查到
        if rs:
            # 抛出异常
            raise forms.ValidationError('该手机号码已被注册')

        # 返回清洗后的值
        return phone

    # 综合验证信息
    def clean(self):
        # 所有清洗后的数据
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('password')
        pwd2 = cleaned_data.get('repassword')
        # 比较两次密码是否一致
        if pwd1 and pwd2 and pwd1 != pwd2:
            raise forms.ValidationError({'repassword': '两次密码不一致!'})
        else:
            if pwd1:
                # 加密密码
                cleaned_data['password'] = set_password(pwd1)
        # 返回清洗后的所有数据
        return cleaned_data


class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['phone', 'password']

        widgets = {
            "phone": forms.TextInput(attrs={"class": "login-name", "placeholder": "请输入手机号码"}),
            "password": forms.PasswordInput(attrs={"class": "login-password", "placeholder": "请输入密码"})
        }

        error_messages = {
            "phone": {
                "required": "请填写手机号"
            },
            "password": {
                "required": "请填写密码",
            }
        }

    def clean(self):
        cleaned_data = super().clean()
        # 验证手机号和密码是否正确
        phone = cleaned_data.get('phone')
        password = cleaned_data.get('password', '')
        # 通过手机号码查询数据(如果有就验证密码,如果没有就报错)
        user = Users.objects.filter(phone=phone).first()
        if user is None:
            raise forms.ValidationError({'phone': '手机号没有被注册'})
        else:
            # 存在 验证密码
            password_in_db = user.password
            password = set_password(password)
            if password_in_db != password:
                raise forms.ValidationError({'password': '密码错误'})
            else:
                # 保存用户的信息对象 到 cleaned_data
                cleaned_data['user'] = user
                return cleaned_data
