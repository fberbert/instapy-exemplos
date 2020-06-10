"""
Bot de Instagram baseado no InstaPy

Objetivo: curtir posts do seu feed 1x por hora

"""

#imports
from instapy import InstaPy
from instapy import smart_run
import getpass
import schedule
import time

#credenciais
insta_username = input("Usuário: ")
insta_password = getpass.getpass("Senha: ")

#início de sessão
session = InstaPy(username=insta_username,password=insta_password,headless_browser=True)

def curtirFeed():

        with smart_run(session):

            #definir parâmetros de iteratividade:
            #
            #contas com no máximo 15000 seguidores
            #contas com no mínimo 10 seguidores
            #contas seguindo no mínimo 10 pessoas
            #
            session.set_relationship_bounds(
                enabled=False,
                delimit_by_numbers=True,
                max_followers=15000,
                min_followers=10,
                min_following=10
            )
            
            session.like_by_feed(amount=20, randomize=False, interact=True)

#definir schedule para cada hora
schedule.every().hour.do(curtirFeed)

#loop infinito
while True:
    schedule.run_pending()
    time.sleep(60)
