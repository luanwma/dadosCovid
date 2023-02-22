import pandas as pd
import plotly.express as px
import streamlit as st

versao = px.__doc__
print(versao)



# lendo dataset
dataset = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Melhorando visualização das colunas
dataset = dataset.rename(columns = {'newDeaths':'Novos óbitos' , 'newCases':'Novos casos', 'deaths_per_100k_inhabitants':'Óbitos por 100k habitantes',
                                    'totalCases_per_100k_inhabitants':'Casos por 100k habitantes'})

# Seleçao do estado
estados = list(dataset['state'].unique()) 
#para menu lateral st.sidebar caso contrario vai abrir o menu em outra janela
estado = st.sidebar.selectbox('Dados de qual estado?',
        estados)

# selecionando colunas

colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100k habitantes','Casos por 100k habitantes']
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)
# seleção das linhas que pertecem ao estado selecionado
dataset = dataset[dataset['state'] == estado]

figura = px.line(dataset, x="date" , y=column, title=column + ' - ' + estado)
figura.update_layout(xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})


#print('DADOS COVID - BRASIL')
st.title('DADOS COVID - BRASIL')
#print('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar no gráfico. ' +
 #     'Utilize o menu lateral para alterar ')
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar no gráfico. ' +
      'Utilize o menu lateral para alterar ')
# figura.show() PARA PLOTAR NO STREAMLIT É DIFERENTE
st.plotly_chart(figura, use_container_width=True) 



st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br', 
    unsafe_allow_html=False)

