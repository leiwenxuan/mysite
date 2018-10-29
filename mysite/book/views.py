from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse, render, redirect
from book.models import Press, book, Person

def login(request):
    #定义一个error 消息替换变量
    error_msg = ''
    # 如果是POST提交
    if request.method == "POST":
        # request.POST提交的字典的形式
        email = request.POST['email']
        # 字典操作get 没有找到返回None
        pwd = request.POST.get('pwd',None)

        ret = Person.objects.filter(email=email, password=pwd)
        # if email == '892028617@qq.com' and pwd == '123':
        if ret:
            return redirect('/girl/')
        else:
            error_msg = '用户名和密码错误'
    # 如果用户验证正确那么error_msg 是空字符串 为空render不出来
    return render(request, 'login.html', {'error_msg':error_msg})
from django.shortcuts import HttpResponse, render, redirect
def girl(request):
    return render(request, '00起飞.html')


def index(request):

    data = Press.objects.all()
    # print(data[0].pname)

    return render(request,'index.html', {"press_list": data})


def add_press(request):
    print(1111)
    if request.method == "POST":
        ret = request.POST.get("press_name")
        Press.objects.create(pname=ret)
        print(333)
        return redirect("/index.html/")
    return  render(request, 'add_press.html',)

def del_press(request):
    #获取ID
    del_id = request.GET.get("id")
    print(del_id)
    Press.objects.filter(id=del_id).delete()

    return redirect("/index.html/")

def edit_press(request):
    print("*"*120)
    #先查询表单ｎａｍｅ
    if request.method == "POST":
        id = request.POST.get("press_id")
        name = request.POST.get("press_name")
        ret = Press.objects.get(id=id)
        ret1 =  Press.objects.filter(id=id)
        ret.pname = name
        ret.save()
        return redirect("/index.html/")
    id_edit = request.GET.get('id')
    print(id_edit)
    print("*" * 120)
    obj = Press.objects.get(id=id_edit)
    print("*" * 120)
    return render(request, "edit_press.html", {"obj":obj})

def book_list(request):
    ret = book.objects.all()
    press_ret = Press.objects.all()
    print(press_ret)
    return render(request, 'book_list.html', {"book_list": ret, "press_list": press_ret})
#添加数据
def add_book(request):
    add_name = request.POST.get('book_name')
    add_press = request.POST.get('press')
    print(add_press, add_name)
    book.objects.create(title=add_name, press_id=add_press)
    ret_press = Press.objects.all()
    return redirect("/book_list.html/")

#删除图书

def del_book(requesst):

    book_id = requesst.GET.get("id")
    print('你要删除我吗', book_id)
    book.objects.filter(id=book_id).delete()
    return redirect('/book_list.html/')

def edit_book(request):
    book_id = request.GET.get('id')
    print(book_id)
    ret_press = Press.objects.all()
    edit_book = book.objects.get(id=book_id)
    if request.method == "POST":
        print(12333333)
        press_input =  request.POST.get('press_name')
        book_input = request.POST.get('title')
        print(press_input, book_input)
        edit_book.title=book_input
        edit_book.press_id = press_input
        edit_book.save()
        return redirect('/book_list/')
    return render( request, 'edit_book.html', {"press_list": ret_press, 'book': edit_book})




