from django import forms

from article.models import ArticleType
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=8,
        label=' 文章标题',
        widget=forms.TextInput(attrs={'class':'input-text'}),
        error_messages={
            'max_length': '长度不能超过8位',
            'required': "标题名称不能为空"
        }
    )
    content = SummernoteTextFormField(
        max_length=10240,
        label="文章内容"

    )
    type = forms.IntegerField(
        label="文章类别",
        widget=forms.Select(
            choices=ArticleType.objects.all().values_list('id', 'title'),
            attrs={'class': 'select'}
        )
    )