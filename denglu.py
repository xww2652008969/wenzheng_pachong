import os
import sys
from bs4 import BeautifulSoup
import requests
os.chdir("src")
note=li()
sql=[]
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
login_url="http://my.sdwz.cn/login"
login_ur2="http://my.sdwz.cn/"
url_img="http://my.sdwz.cn/s/verification" 
url1="http://my.sdwz.cn/uc/schedule/notice/index"
def getcookie():       #模拟登录获取对话
    denglu=requests.session()
    a=denglu.get(login_url)
    so=BeautifulSoup(a.text, "html5lib")
    a=denglu.get(url_img)
    f=open("1.jpg","wb")
    f.write(a.content)
    f.close()  
    data={}
    data['username']=1817404059
    data['password']='zW2652008969'
    data['_csrf']=so.input.attrs['value']
    data['code']=input("请输入验证码")
    a=denglu.post(login_url,data=data)
    print(a.url)
    print(data)
    if (a.url)!="http://my.sdwz.cn/index":
        print("你的验证码或者学号或者密码错误")
        getcookie()
    denglu.__doc__=data['_csrf']
    return denglu
def li():
    c=[]
    if(os.path.exists('note')):    
        fo=open("note",'r')
        for a in fo.readlines():
            a=a.strip()
            c.append(a)
    return c
def guize(a):
      pass
      a=re.sub('&quot;','"',a)
      a=re.sub('&gt;','>',a)
      a=re.sub('&lt;','<',a)
      a=re.sub('" name="content"/>','',a)
      a=re.sub(' /','',a)
      a=re.sub('<input type="hidden" value="','',a)
      a=re.sub('&amp;nbsp;','',a)
      return a
#因为原网页是部分代码是需要js修改  我就写正则了
def got(a,b):
    data=[]   
    so=BeautifulSoup(a,"html5lib")
    for a in so.find_all(class_="layui-custom-li new-li",content=re.compile("\w")):
        f=open("note","a")
        if a.attrs['content'] not in b:
               pass
               f.write(a.attrs['content']+'\n')
               data.append(a.attrs['content'])
        '''
        m=1
        for c in a.children :
             if c!='\n':
               # if(m%3==1):
                #   oo.write("通知标题:  "+c.string)
                #if(m%3==2):
                 #  oo.write("通知来源:  "+c.string)
                if(m%3==0):
                   oo.write("\n")
                m=m+1
         '''       
    f.close()
    return data
#为了记录所爬行的数据记录
def dow(url):
    url=guize(url)   
    so=BeautifulSoup(url,"html5lib")
    for a in so.find_all(class_='layui-h1'):
       print (a.string)
       xuyao=open(str(a.string),"w")
    for a in so.find_all(class_='layui-h2'):
       for c in a:
           try:
              xuyao.write(c.string)
           except :
              pass
    xuyao.write("\n")
    b=so.find_all(class_="layui-nr")
    for c in b:
        xuyao.write(c.get_text())
    xuyao.close()
#下载
a=getcookie()
cishu=1
data={'title':'',
       'rows':'11',
       'totalPages':'3153',
       }
data['current']=cishu
data['_csrf']=a.__doc__
while cishu<=200000:
    print(data)
    b=a.post(url1,data=data)
    sql=got(b.text,note)
    i=1
    while i>0:
        try:
            b=a.get("http://my.sdwz.cn/uc/schedule/notice/"+sql[i]+"/index")
            dow(b.text)
            i=i+1
        except:
            break
    cishu=cishu+1
    data['current']=cishu
