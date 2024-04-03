import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
data = pd.DataFrame([[1,3.5,5.3],[2,3.6,4.7],[3,4.6,5.8]], columns = ['Время, с', '1', '2'])

#заставка
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.title('📊 HTO ЦСС') 
#понелька
st.sidebar.header('Настройки')
ms  = st.sidebar.multiselect('Выберите ID', ['72:28:23:45:32','22:22:43:45:56'])
rec = st.sidebar.button('получить данные')



#выборы понельки

  #график амплитудного спектра

for id in ms:
  st.markdown(f'### MAC-адрес {id}')
  c1, c2, c3, c4, c5 = st.columns(5)
  c1.metric('Ср. арифм.', '10', '1.2 F')
  c2.metric('Медиан. знач.', '10')
  c3.metric('Мин. знач.', '10')
  c4.metric('Макс. знач.', '10')
  c5.metric('Ср. квадр. откл.', '10')

  st.line_chart(data, x='Время, с', y = '1')




#selectbox

























    
#st.markdown('_среднее арифметическое значение сигнала_') 
#st.markdown('_медианное значение сигнала_')
#st.markdown('_минимальное значение сигнала_')
#st.markdown('_максимальное значение сигнала_')

#grS = st.sidebar.checkbox('График для сенсоров')
#grO = st.sidebar.checkbox('График для операторов')

#st.selectbox('Значение сигнала', ['среднее арифметическое', 'медианное', 'минимальное и макисмальное'])
#st.subheader('My sub')

#st.button('график ')
#st.checkbox('Check me out')
#st.radio('Pick one:', ['nose','ear'])
#st.selectbox('Select', [1,2,3])
#st.multiselect('Multiselect', [1,2,3])




#st.subheader('My sub')

#st.button('график ')
#st.checkbox('Check me out')
#st.radio('Pick one:', ['nose','ear'])
#st.selectbox('Select', [1,2,3])
#st.multiselect('Multiselect', [1,2,3])






#графики
#data = pd.DataFrame([[1,2,3],[2,3,4],[3,4,5]], columns = ['a', 'b', 'c'])
#st.line_chart(data, x='a', y = 'b')
#with st.expander('About this app'):
#   st.markdown('**What can this app do?**')
#   st.info('This app shows the use of Pandas for data wrangling, Altair for chart creation and editable dataframe for data interaction.')
#   st.markdown('**How to use the app?**')
#   st.warning('To engage with the app, 1. Select genres of your interest in the drop-down selection box and then 2. Select the year duration from the slider widget. As a result, this should generate an updated editable DataFrame and line plot.')
  
 #st.subheader('Which Movie Genre performs ($) best at the box office?')

# # Load data
# df = pd.read_csv('data/movies_genres_summary.csv')
# df.year = df.year.astype('int')

# # Input widgets
# ## Genres selection
# genres_list = df.genre.unique()
# genres_selection = st.multiselect('Select genres', genres_list, ['Action', 'Adventure', 'Biography', 'Comedy', 'Drama', 'Horror'])

#Year selection
#year_list = df.year.unique()
#year_selection = st.slider('Select year duration', 1986, 2006, (2000, 2016))
#year_selection_list = list(np.arange(year_selection[0], year_selection[1]+1))

# df_selection = df[df.genre.isin(genres_selection) & df['year'].isin(year_selection_list)]
# reshaped_df = df_selection.pivot_table(index='year', columns='genre', values='gross', aggfunc='sum', fill_value=0)
# reshaped_df = reshaped_df.sort_values(by='year', ascending=False)


# # Display DataFrame

# df_editor = st.data_editor(reshaped_df, height=212, use_container_width=True,
#                             column_config={"year": st.column_config.TextColumn("Year")},
#                             num_rows="dynamic")
# df_chart = pd.melt(df_editor.reset_index(), id_vars='year', var_name='genre', value_name='gross')

# # Display chart
# chart = alt.Chart(df_chart).mark_line().encode(
#             x=alt.X('year:N', title='Year'),
#             y=alt.Y('gross:Q', title='Gross earnings ($)'),
#             color='genre:N'
#             ).properties(height=320)
# st.altair_chart(chart, use_container_width=True)
