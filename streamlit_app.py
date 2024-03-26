import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
data = pd.DataFrame([[1,3.5,5.3],[2,3.6,4.7],[3,4.6,5.8]], columns = ['time', 'ID1', 'ID2'])

#заставка
st.set_page_config(page_title='Interactive Data Explorer', page_icon= '📊')
st.title('📊 HTO ЦАП') 

#понелька
st.sidebar.header('Настройки')
grS = st.sidebar.checkbox('График для сенсоров')
grO = st.sidebar.checkbox('График для операторов')


#выборы понельки
if grS == True:
  v1 = st.multiselect('выберете ID сенсоров', ['ID1','ID2'])
  if v1:
    st.line_chart(data, x='time', y = v1)
if grO == True:
  v2 = st.multiselect('выберете ID операторов', ['ID1','ID2'])
  if v2:
    st.line_chart(data, x='time', y = v2)











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
