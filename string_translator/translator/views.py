from django.shortcuts import render
from deep_translator import GoogleTranslator

def home(request):
    translated_text = None
    if request.method == "POST":
        text = request.POST.get('text')
        target = request.POST.get('target')
        print("Text:", text)
        print("Target:", target)
        
        try:
            translated_text = GoogleTranslator(source='auto', target=target).translate(text)
        except Exception as e:
            translated_text = f"sorry there is an Error: {e}"
    return render(request, 'home.html',{'translated': translated_text})
