from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>hello</h1>')

def item(request,id):
    print(id)
    return HttpResponse(f'id is {id}')

def user(request,name):
    return HttpResponse(f"name is {name}")

def read(request,book):
    return HttpResponse(f'uuid:{book}')

def way(request,route):
    return HttpResponse(f'path:{route}')

def index(request):
    html=('''
    <div><a href="/item/65.html">item</a></div>
    <div><a href="/user/tom">user</a></div>
    <div><a href="/read/12345678-1234-1234-1234-123456789012">read</a></div>
    <div><a href="/way/bn/34/1234">way</a></div>
    ''')
    return HttpResponse(html)