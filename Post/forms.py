from  django.forms import ModelForm, TextInput, EmailInput
from  .models import Post


class PostForm(ModelForm):
    class Meta:
        model=Post
        fields =["title","host","category", "description"]
        #widgets={
        #    'title':TextInput(attrs={'class':'form-control'}),
            #'host':TextInput(attrs={'class':'form-control'}),
         #   'category':TextInput(attrs={'class':'form-control'}),
           # 'description':TextInput(attrs={'class':'form-control'})
# }