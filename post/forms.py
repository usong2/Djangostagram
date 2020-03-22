from django import forms

class PostForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력하세요'
        },
        max_length=128, label="제목"
    )
    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력하세요'
        },
        widget=forms.Textarea, label="내용"
    )
    image_url = forms.CharField(
        error_messages={
            'required': '이미지 주소를 입력하세요'
        },
        max_length=256, label="이미지 주소"
    )