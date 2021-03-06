# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: form.py
@time: 2017/7/13 16:42
"""
from flask_wtf import  Form
from wtforms import  StringField,SubmitField,DateTimeField,validators,IntegerField,FileField,PasswordField
class LoginFrom(Form):
    username=StringField(u'用户名',[validators.Length(min=4, max=16,message=u'用户名长度在4-16位'),validators.DataRequired(message=u'用户名不能为空')],render_kw={'placeholder':u'请输入用户名'})
    password=PasswordField(u'密码',[validators.length(min=8,max=16,message=u'密码长度8-16位'),validators.DataRequired(message=u'密码不能为空')],render_kw={'placeholder':u'请输入密码'})
class RegFrom(Form):
    username = StringField(u'注册用户名', [validators.Length(min=4, max=16, message=u'用户名长度在4-16位'), validators.DataRequired(message=u'用户名不能为空')],render_kw={'placeholder': u'请输入用户名'})
    password = PasswordField(u'注册密码', [validators.length(min=8, max=16, message=u'密码长度8-16位'), validators.DataRequired(message=u'密码不能为空')],render_kw={'placeholder': u'请输入密码'})
    se_password = PasswordField(u'再次输入密码', [validators.length(min=8, max=16, message=u'密码长度8-16位'), validators.DataRequired(message=u'密码不能为空')],
                             render_kw={'placeholder': u'请输入密码'})
    email=StringField(u'输入注册邮箱', [ validators.DataRequired(message=u'注册邮箱不能为空')],
                           render_kw={'placeholder': u'请输入邮箱'})
class XugaiFrom(Form):
    password = PasswordField(u'密码', [validators.length(min=8, max=16, message=u'密码长度8-16位'), validators.DataRequired(message=u'原密码不能为空')],
                             render_kw={'placeholder': u'请输入原密码'})
    xiu_password = PasswordField(u'密码',
                                [validators.length(min=8, max=16, message=u'密码长度8-16位'), validators.DataRequired(message=u'密码不能为空')],
                                render_kw={'placeholder': u'请输入新密码'})
    xiu_password_se = PasswordField(u'密码',
                                 [validators.length(min=8, max=16, message=u'密码长度8-16位'), validators.DataRequired(message=u'密码不能为空')],
                                 render_kw={'placeholder': u'请再次输入密码'})
class InterForm(Form):
    project_name=StringField(u'项目名字', [validators.DataRequired(message=u'项目名不能为空')],render_kw={'placeholder': u'请输入接口所属项目名称'})
    model_name=StringField(u'模块名字', [validators.DataRequired(message=u'模块名不能为空')],render_kw={'placeholder': u'请输入接口所属模块名称'})
    interface_name=StringField(u'接口名字', [validators.DataRequired(message=u'接口名不能为空')],render_kw={'placeholder': u'请输入接口名称'})
    interface_url=StringField(u'接口url', [validators.DataRequired(message=u'接口url不能为空')],render_kw={'placeholder': u'请输入接口url'})
    interface_meth=StringField(u'请求方式', [validators.DataRequired(message=u'请求方式不能为空')],render_kw={'placeholder': u'请输入接口请求方式'})
    interface_par = StringField(u'请求示例', [validators.DataRequired(message=u'请求示例不能为空')], render_kw={'placeholder': u'请输入接口参数示例'})
    interface_bas= StringField(u'请求返回示例', [validators.DataRequired(message=u'返回示例不能为空')], render_kw={'placeholder': u'请输入接口返回示例'})
class Interface_yong_Form(Form):
    yongli_name=StringField(u'项目', [validators.DataRequired(message=u'项目名不能为空')],render_kw={'placeholder': u'请输入接口项目名称'})
    model_name=StringField(u'模块', [validators.DataRequired(message=u'模块名不能为空')],render_kw={'placeholder': u'请输入接口模块名称'})
    interface_name = StringField(u'接口名字', [validators.DataRequired(message=u'接口名不能为空')], render_kw={'placeholder': u'请输入接口名称'})
    interface_url = StringField(u'接口url', [validators.DataRequired(message=u'接口地址不能为空')], render_kw={'placeholder': u'请输入接口url'})
    interface_meth = StringField(u'请求方式', [validators.DataRequired(message=u'请求方式不能为空')], render_kw={'placeholder': u'请输入接口请求方式'})
    interface_can=StringField(u'请求参数', [validators.DataRequired(message=u'请求参数不能为空')], render_kw={'placeholder': u'请输入接口请求参数'})
    interface_rest = StringField(u'请求预期', [validators.DataRequired(message=u'接口预期不能为空')], render_kw={'placeholder': u'请输入接口预期'})
