from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired, EqualTo, Length
from flask_wtf.file import FileRequired, FileAllowed


# 管理员表单验证
class UserForm(FlaskForm):

    login_name = StringField("管理员账号",
                           validators=[DataRequired(message="请输入管理员账号！"),
                                       Length(5, 12, message="账号长度要求5~12字符！")],
                           render_kw={"class": "form-control",
                                      "placeholder": "请输入管理员账号"})

    login_pwd = PasswordField("管理员密码",
                             validators=[DataRequired(message="请输入管理员密码！"),
                                         Length(6, 8, message="密码长度要求6~8字符！")],
                             render_kw={"class": "form-control",
                                        "placeholder": "请输入管理员密码"})

    repassword = PasswordField("确认密码",
                               validators=[DataRequired(message="请再次输入密码！"),
                                           EqualTo("login_pwd", message="两次密码不一致!")],
                               render_kw={"class": "form-control",
                                          "placeholder": "请再次输入密码！"})

    status = BooleanField("是否启用")

    submit = SubmitField("提交", render_kw={"class": "btn btn-primary"})


class ArticleForm(FlaskForm):
    title = StringField("新闻标题",
                        validators=[DataRequired(message="请输入新闻标题!"),
                                    Length(1, 50, message="标题长度要求1~50个字符!")],
                        render_kw={"class": "form-control",
                                   "placeholder": "请输入新闻标题!"})
    content = TextAreaField("新闻详情",
                            validators=[DataRequired(message="请输入新闻详情内容!")],
                            render_kw={"class": "form-control",
                                       "style": "resize:none",
                                       "id": "content"})
    types = SelectField("新闻类型",
                        choices=[('国内', '国内'), ('娱乐', '娱乐'), ('军事', '军事'), ('体育', '体育')],
                        render_kw={"class": "form-control"})
    # img_url = StringField("新闻封面图片",
    #                       validators=[DataRequired(message="请输入新闻图片路径!")],
    #                       render_kw={"class": "form-control"})
    img_url = FileField("上传新闻封面图片",
                       validators=[FileRequired(),
                                   FileAllowed(['png', 'jpg', 'gif'],
                                               message="只接收.png、.jpg和.gif格式的图片")])
    author = StringField("新闻来源",
                         validators=[DataRequired(message="请输入新闻来源!")],
                         render_kw={"class": "form-control"})
    is_recommend = BooleanField("是否推荐")
    is_valid = BooleanField("是否启用")
    submit = SubmitField("提交", render_kw={"class": "btn btn-primary"})


class ModifyForm(FlaskForm):

    username = StringField("管理员账号",
                           validators=[DataRequired(message="请输入管理员账号！"),
                                       Length(5, 12, message="账号长度要求5~12字符！")],
                           render_kw={"class": "form-control",
                                      "placeholder": "请输入管理员账号"})

    password = PasswordField("旧管理员密码",
                             validators=[DataRequired(message="请输入旧管理员密码！"),
                                         Length(6, 8, message="密码长度要求6~8字符！")],
                             render_kw={"class": "form-control",
                                        "placeholder": "请输入旧管理员密码"})

    newpassword = PasswordField("新管理员密码",
                                validators=[DataRequired(message="请输入新管理员密码！"),
                                            Length(6, 8, message="密码长度要求6~8字符！")],
                                render_kw={"class": "form-control",
                                           "placeholder": "请输入新管理员密码"})

    renewpassword = PasswordField("确认新密码",
                                  validators=[DataRequired(message="请再次输入新密码！"),
                                              EqualTo("newpassword", message="两次密码不一致!")],
                                  render_kw={"class": "form-control",
                                             "placeholder": "请再次输入新密码！"})

    submit = SubmitField("提交", render_kw={"class": "btn btn-primary"})


class UploadForm(FlaskForm):
    upload = FileField("上传新闻封面图片",
                       validators=[FileRequired(),
                                   FileAllowed(['png', 'jpg', 'gif'], "直接收.png、.jpg和.gif格式的图片")])
    submit = SubmitField("上传", render_kw={"class": "btn btn-primary pull-left"})
