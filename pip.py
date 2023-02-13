import streamlit as st


st.set_page_config(page_title="my Portfolio",page_icon=':tada:',layout='wide')

with st.container():
 st.subheader('hi,Im ayoub:wave:')
 st.title('A front-end developper,from maroco')

with st.container ( ):
     st.write('---')
     left_column,right_column=st.columns(2)
     with left_column:
          st.header('what i do')
          st.write('##')
          st.write(
               '''
               As a highly motivated and skilled web developer, I bring a passion for creating innovative and effective web solutions to every project I undertake. With several years of experience in the industry, I have honed my abilities in a range of technologies including HTML, CSS, JavaScript, and PHP. I have a talent for taking complex problems and breaking them down into manageable tasks, allowing me to deliver clean and efficient code. I have worked on various projects, from simple static websites to complex web applications, and have consistently received positive feedback from clients for my attention to detail and ability to meet tight deadlines. My goal is to use my expertise to create
                user-friendly and visually appealing websites that engage and inform users, and I am confident that I can bring value to any project I work on.'''
          )


with st.container():
     st.write('---')
     st.header('my portfolio')
     st.write('##')
     image_column,text_column=st.columns((1,2))
     with image_column:
          st.image.open('image/ayoub.jpeg')
     with text_column:
          st.subheader('ayoub ahnouch')
          st.write(
               '''
               déveloper informatique
               tel:0697052798
               E-mail:ayoubeahnouch@gmail.com
               Adress:lagwira lkhyam,agadir
               Epitech:lafac 
               lycee baptiste poquelin:Bac physique(2020),Ecol EWA (2022)
               competences:le HTML,le css
               lunguage:arab'''
               
          )
