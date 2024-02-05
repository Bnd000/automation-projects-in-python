import pandas as pd
from twilio.rest import Client

account_sid = 'AC7420e2c3d4919d78fb179eb55188959c'
auth_token = '208ec5847825fd017acb269aad4a9d37'
from_number = '+1 315 371 3066'
to_number = '+5521994890321'

client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabelas_vendas = pd.read_excel(f'{mes}.xlsx')

    if (tabelas_vendas['Vendas'] > 55000).any():
        vendendor = tabelas_vendas.loc[tabelas_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabelas_vendas.loc[tabelas_vendas['Vendas'] > 55000, 'Vendas'].values[0]

        print(f'Seu funcionário: {vendendor} conseguiu vender: {vendas} no mês de {mes}')

        # Crie o cliente Twilio
        client = Client(account_sid, auth_token)

        # Mensagem a ser enviada
        mensagem = f'Seu funcionário: {vendendor} conseguiu vender: {vendas} no mês de {mes}'

        # Correção: Adicionei um parêntese no final do método client.messages.create() e removi o espaço após a vírgula
        message = client.messages.create(
            body=f'Seu funcionário: {vendendor} conseguiu vender: {vendas} no mês de {mes}',
            from_="+13153713066",
            to='+5521994890321'
        )

        print(message.sid)

