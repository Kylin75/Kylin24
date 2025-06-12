import streamlit as st
#修改网页名字和图标
st.set_page_config(page_title='动物图鉴', page_icon='🦝')
#设置标题
st.title("📽Streamlit视频播放器")
#导入文本写内容
st.text("点击下方视频封面选择要播放的视频")
# 创建一个子章节
st.subheader("视频播放")

# 在内存中初始化一个ind,当内存中没有'ind'的时候，才初始化
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 视频数组-装多个视频和相关信息

vedio_obj = [{
        'url':' https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
        '时长': '0:10',
        '分类':'动画',
        '描述':'优美' ,
         'title':'剧情优美'
    }, {
        'url': 'https://www.w3schools.com/html/movie.mp4',
        '时长': '0:12',
        '分类' :'自然',
        '描述':'美丽的自然景观，山川湖海',
        'title':'自然风光'
        
    }, {
        'url': 'https://media.w3.org/2010/05/sintel/trailer.mp4',
        '时长': '0:52',
        '分类' :'冒险',
        '描述':'惊险刺激',
        'title':'精彩有趣'
    }]


st.video(vedio_obj[st.session_state['ind']]['url'])
# 显示按钮

def nextImg():
    # 点击下一张按钮要做的事
    st.session_state['ind'] = 0

def nextImg1():
    # 点击下一张按钮要做的事
    st.session_state['ind'] = 1
def nextImg2():
    # 点击下一张按钮要做的事
    st.session_state['ind'] = 2



# 创建一个子章节
st.subheader(vedio_obj[st.session_state['ind']]['title'])

#将一行分为两列将对应列写入内容
c1, c2,= st.columns([1,10])
with c1:
   st.markdown('描述：')

with c2:
   st.markdown(vedio_obj[st.session_state['ind']]['描述'])

#将一行分为两列将对应列写入内容
c1, c2,= st.columns([1,10])
with c1:
   st.markdown('时长: ')

with c2:
   st.markdown(vedio_obj[st.session_state['ind']]['时长'])
   
#将一行分为两列将对应列写入内容
c1, c2,= st.columns([1,10])
with c1:
   st.markdown('分类:')

with c2:
  st.markdown(vedio_obj[st.session_state['ind']]['分类'])




# 自定义format_func函数
def my_format_func(option):
    return f'{option}'

st.header('下拉按钮示例')

category= st.selectbox('选择你喜欢的类型：', ['全部','动画', '自然', '冒险'], format_func=my_format_func, index=2)
# 根据返回值不同，选择不同的特色回答
# 同时应注意返回值不受自定义my_format_func
if category == '全部':
    st.button(' ', on_click=nextImg)
    st.image("https://img.likebizhi.com/1821652950/123pan/123panlikebizhi/240105101004.jpg")

    st.button('   ', on_click=nextImg1)
    st.image("https://img.shetu66.com/2023/04/26/1682497576231754.png")

    st.button('     ', on_click=nextImg2)
    st.image("https://n.sinaimg.cn/sinacn06/265/w640h425/20180710/f540-hezpzwu4459148.jpg")
    
elif category == '动画':
    st.button(' ', on_click=nextImg)
    st.image("https://img.likebizhi.com/1821652950/123pan/123panlikebizhi/240105101004.jpg")
elif category == '自然':
    st.button('   ', on_click=nextImg1)
    st.image("https://img.shetu66.com/2023/04/26/1682497576231754.png")
    
else: 
    st.button('     ', on_click=nextImg2)
    st.image("https://n.sinaimg.cn/sinacn06/265/w640h425/20180710/f540-hezpzwu4459148.jpg")


