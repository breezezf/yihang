# -- coding:utf-8 --
'''科技工作室'''
import streamlit as st
import datetime
from PIL import Image
from PIL import ImageFilter,ImageDraw,ImageFont
page = st.sidebar.title('科技工作室')
page = st.sidebar.radio('',['科技普及','图片处理','智能词典','留言区(评价与建议)'])
today = st.date_input("",datetime.datetime.now())
def page1():
    '''科技普及'''
    st.subheader("科技普及(2024年1月17日期)")
    st.write("____________________________")
    st.title("物理-核物理")
    st.header("聚变、裂变-氢弹、原子弹")
    st.write("____________________________")
    st.subheader("自动朗读")
    with open('马一航_原子弹、氢弹.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.write("____________________________")
    st.subheader("文本")
    st.write("氢弹和原子弹是目前人类所拥有的威力最大的武器，但他们的原理截然不同，简单来说一个是两个原子分裂，在带动其他原子分裂产生裂变，另一个则相反，是让两个原子聚拢。再带动其他原子聚拢产生聚变，咱们先说裂变，这个反应在正常环境中就能进行。它用到的元素是铀，想要把天然铀提纯到核武器可以用的程度可不容易，得要经过一系列化学程序，再在分离机里甩几年，才能把铀中不要的铀238都弄掉的，只剩下有用的铀235，铀的重量只要达到一个数值就能引发裂变，人们利用这个原理制作了两种不同结构的原子弹。枪式和内爆式，枪式就是把达到临界质量的铀分成两份，要引爆时把一块铀推到另一块铀上，就能引发裂变了，虽然简单，但这种结构的原子弹铀利用率非常低，为了解决这个问题，人们设计了另一种结构的原子弹也就是内爆式，它是制作了一块接近临界质量的球形铀，在在球形油的表面上均匀布置炸弹，再要引爆时把球形铀上的炸弹同时引爆，这样就能向内挤压铀。让它达到临界质量从而引发裂变，这样做虽然难度高，但铀利用率也很高，这时大家可能发现一个问题就是其实不管是枪式还是内爆式，它单颗原子弹爆炸能力都是有限的，就这样，氢弹孕育而生了，在开始讲氢弹前，我们先说一个原理，只要有合适的温度与压力一切比铁轻的物质都能聚变，但这个温度和压力很难实现，在发明原子弹后，人们就意识到哎，这个氢的聚变条件原子弹可以满足，于是人们造出了氢弹，就是一个装氘氚(氢的同位素)的容器，旁边放一颗原子弹，这样在起爆的一瞬间就会引发氘氚的聚变，这就是两种核武器。")
    st.write("最后我想说一句话:核武是一把双刃剑，就看人类怎么用它了")
    st.write("____________________________")
    st.subheader("图片")
    st.write("原子弹实物")
    st.image("马一航_原子弹实物.jpg")
    st.write("原子弹枪式结构")
    st.image("马一航_原子弹枪式结构.jpg")
    st.write("原子弹内爆式结构")
    st.image("马一航_原子弹内爆式结构.png")
    st.write("氢弹实物")
    st.image("马一航_氢弹实物.png")
    st.write("氢弹结构")
    st.image("马一航_氢弹结构.jpg")
    st.write("____________________________")
    st.subheader("视频")
    st.video("马一航_氢弹、原子弹.mp4")
    st.write("____________________________")
    st.write("原子弹枪式与内爆式铀利用率对比(0代表枪式,1内爆式(单位:百分之(%)))")
    st.bar_chart(data=[22,28.5],width=10, height=500, use_container_width=True)
    st.write("____________________________")
    st.subheader("网页")
    st.link_button('原子弹','https://baike.baidu.com/item/%E5%8E%9F%E5%AD%90%E5%BC%B9/136858')
    st.link_button('氢弹','https://baike.baidu.com/item/%E6%B0%A2%E5%BC%B9/110129')
    st.write("____________________________")
    st.subheader("本期完")
    st.write("____________________________")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("____________________________")
    st.subheader("科技普及(2024年1月15日期)")
    st.write("____________________________")
    st.title("航空航天-深空探测")
    st.header("离子推进器-星际之门的钥匙")
    st.write("____________________________")
    st.subheader("自动朗读")
    with open('马一航_离子推进器.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.write("____________________________")
    st.subheader("文本")
    st.write("离子推进器,是一种工质推进器,也就是靠向后抛出物质,来获得一个反推力,从而推动飞船,不过和普通的化学火箭不同,它的工质不是液氢液氧,而是氙,氙是一种气体,离子推进器,是先电离粒子,再靠线圈加速粒子,以非常快的速度喷出,从而推动飞船,但因为推力很小,它不能直接从大气层内起飞,但它虽然推力很小,但比冲很大,虽然开始速度很慢,但它能一直加速到200分之一光速,而且还很节省燃料。")
    st.write("离子推进器是一把钥匙,是一把帮人类打开星际之门的钥匙！")
    st.write("____________________________")
    st.subheader("图片")
    st.write("离子推进器实物")
    st.image('马一航_离子推进器.jpg')
    st.write("离子推进器结构")
    st.image('马一航_离子推进器结构.jpg')
    st.write("____________________________")
    st.subheader("视频")
    st.video('马一航_离子推进器.mp4')
    st.write("____________________________")
    st.subheader("图表")
    st.write("化学与离子推进器推力对比(0代表化学推进器,1代表离子推进器(单位:牛顿(N)))")
    st.bar_chart(data=[450,5.4],width=10, height=500, use_container_width=True)
    st.write("化学与离子推进器冲比对比(0代表化学推进器,1代表离子推进器(单位:秒(m/s)))")
    st.bar_chart(data=[440,5100],width=10, height=500, use_container_width=True)
    st.write("____________________________")
    st.subheader("网页")
    st.link_button('离子推进器','https://baike.baidu.com/item/%E7%A6%BB%E5%AD%90%E6%8E%A8%E8%BF%9B%E5%99%A8/4751870')
    st.write("____________________________")
    st.subheader("本期完")
    st.write("____________________________")
    st.subheader("我也是有底线的呦！")
    pass
if page == '科技普及':
    page1()
def f(img):
    img_temp = img.filter(ImageFilter.BLUR)
    return img_temp
def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height=img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (b,g,r)
    return img
def xvanzhuan(img,D):
    rotated_img = img.rotate(D)
    return rotated_img
def fanzhuan(img):
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return flipped_img
def page2():
    '''图片处理'''
    st.write("____________________________")
    st.title("图片处理工具")
    st.header("图片换色")
    A=int(st.slider('红',0,2))
    B=int(st.slider('绿',0,2))
    C=int(st.slider('蓝',0,2))
    st.subheader("上传图片")
    uploaded_file = st.file_uploader("",type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img,A,B,C))
    st.write("____________________________")
    st.header("图片模糊")
    st.subheader("上传图片")
    uploaded_fileA = st.file_uploader(" ",type=['png','jpeg','jpg'])
    if uploaded_fileA:
        file_nameA = uploaded_fileA.name
        file_typeA = uploaded_fileA.type
        file_sizeA = uploaded_fileA.size
        imgA = Image.open(uploaded_fileA)
        st.image(imgA)
        st.image(f(imgA))
    st.write("____________________________")
    st.header("图片旋转")
    D=st.slider('度数',0,360)
    st.subheader("上传图片")
    uploaded_fileB = st.file_uploader("  ",type=['png','jpeg','jpg'])
    if uploaded_fileB:
        file_nameB = uploaded_fileB.name
        file_typeB = uploaded_fileB.type
        file_sizeB = uploaded_fileB.size
        imgB = Image.open(uploaded_fileB)
        st.image(imgB)
        st.image(xvanzhuan(imgB,D))
    st.write("____________________________")
    st.header("图片翻转")
    st.subheader("上传图片")
    uploaded_fileC = st.file_uploader("   ",type=['png','jpeg','jpg'])
    if uploaded_fileC:
        file_nameC = uploaded_fileC.name
        file_typeC = uploaded_fileC.type
        file_sizeC = uploaded_fileC.size
        imgC = Image.open(uploaded_fileC)
        st.image(imgC)
        st.image(fanzhuan(imgC))
    st.write("____________________________")
    st.subheader("我也是有底线的呦！")
    pass
if page == '图片处理':
    page2()
def page3():
    '''智能词典'''
    st.write("____________________________")
    st.title("智慧词典")
    st.write("____________________________")
    with open('马一航_words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
    times_dict = {}
    for i in times_dict:
        times_dict[int(i[0])] = int(i[1])
    st.header("请输入要查询的单词:")
    word = st.text_input('')
    if word in words_dict:
        st.write(words_dict[word][1])
    st.write("____________________________")
    st.subheader("我也是有底线的呦！")
if page == '智能词典':
    page3()
def page4():
    '''留言区(评价与建议)'''
    st.write("____________________________")
    st.subheader("在这里留下你的痕迹吧，但请友善留言，恶语伤人心！")
    st.write("____________________________")
    st.title("留言区域")
    st.write("____________________________")
    with open ('马一航_leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
        for i in range(len(messages_list)):
            messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        st.write(i[0],':',i[1],':',i[2])
    st.write("____________________________")
    st.subheader('我是……')
    x= st.text_input('自定义名称')
    if x == "官方":
        st.title("你确定你是官方？")
    else:
        name = st.selectbox('',['游客','科技大牛','编程大牛',x])
        if name == '游客':
            st.write("____________________________")
            st.subheader('想要做的评价、提的建议、说的话……')
            new_message = st.text_input('')
            if st.button('留言'):
                messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
                with open('马一航_leave_messages.txt','w',encoding='utf-8') as f:
                    messages = ''
                    for i in messages_list:
                        messages += i[0] + '#' + i[1] + '#' + i[2] + '\n'
                    messages = messages[:-1]
                    f.write(messages)
        if name == '科技大牛':
            st.subheader('请选择一个类型:')
            kx = st.radio(
                    '',
                    ['天文', '物理', '化学']
                    )
            if kx == '天文':
                st.subheader('请问星等指的是恒星的什么？')
                st.write('A 恒星的大小')
                st.write('B 恒星的年龄')
                st.write('C 恒星的亮度')
                st.write('D 我们离恒星的距离')
                xx1= st.text_input(' ')
                if xx1 == 'C':
                    st.write("____________________________")
                    st.subheader('想要做的评价、提的建议、说的话……')
                    new_message = st.text_input('')
                    if st.button('留言'):
                        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
                        with open('马一航_leave_messages.txt','w',encoding='utf-8') as f:
                            messages = ''
                            for i in messages_list:
                                messages += i[0] + '#' + i[1] +'#' + i[2] + '\n'
                            messages = messages[:-1]
                            f.write(messages)
            if kx == '物理':
                st.subheader('两种物质被称为同位素，是因为它们？')
                st.write('A 原子核内质子数相等')
                st.write('B 原子核内中子数相等')
                st.write('C 原子核内质子加中子数相等')
                xx2= st.text_input('  ')
                if xx2 == 'A':
                    st.write("____________________________")
                    st.subheader('想要做的评价、提的建议、说的话……')
                    new_message = st.text_input('')
                    if st.button('留言'):
                        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
                        with open('马一航_leave_messages.txt','w',encoding='utf-8') as f:
                            messages = ''
                            for i in messages_list:
                                messages += i[0] + '#' + i[1] + '#' + i[2] + '\n'
                            messages = messages[:-1]
                            f.write(messages)
            if kx == '化学':
                st.subheader('大气层中臭氧的主要作用是？')
                st.write('A 吸收CO2')
                st.write('B 补充O2')
                st.write('C 吸收红外线')
                st.write('D 吸收紫外线')
                xx3= st.text_input('  ')
                if xx3 == 'D':
                    st.write("____________________________")
                    st.subheader('想要做的评价、提的建议、说的话……')
                    new_message = st.text_input('')
                    if st.button('留言'):
                        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
                        with open('马一航_leave_messages.txt','w',encoding='utf-8') as f:
                            messages = ''
                            for i in messages_list:
                                messages += i[0] + '#' + i[1] + '#' + i[2] + '\n'
                            messages = messages[:-1]
                            f.write(messages)
        if name == '编程大牛':
            st.subheader('请问这段文本使用的Python代码是什么？')
            st.write('A st.text()')
            st.write('B st.title()')
            st.write('C st.write()')
            st.write('D st.subheader()')
            xx4= st.text_input(' ')
            if xx4 == 'D':
                st.write("____________________________")
                st.subheader('想要做的评价、提的建议、说的话……')
                new_message = st.text_input('')
                if st.button('留言'):
                    messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
                    with open('马一航_leave_messages.txt','w',encoding='utf-8') as f:
                        messages = ''
                        for i in messages_list:
                            messages += i[0] + '#' + i[1] +'#' + i[2] + '\n'
                        messages = messages[:-1]
                        f.write(messages)
    st.write("____________________________")
    st.subheader("我也是有底线的呦！")
    pass
if page == '留言区(评价与建议)':
    page4()
