"""
Bot de Instagram baseado no InstaPy

Objetivo: seguir novas contas com base em hashtags

"""

#imports
from instapy import InstaPy
from instapy import smart_run
import getpass

#credenciais
insta_username = input("Usuário:")
insta_password = getpass.getpass("Senha:")

#início de sessão
session = InstaPy(username=insta_username,password=insta_password,headless_browser=True)

with smart_run(session):

    #definir parâmetros de iteratividade:
    #
    #contas com no máximo 15000 seguidores
    #contas com no mínimo 10 seguidores
    #contas seguindo no mínimo 10 pessoas
    #
    session.set_relationship_bounds(
        enabled=True,
        delimit_by_numbers=True,
        max_followers=15000,
        min_followers=10,
        min_following=10
    )

    #configurar para interagir com 2 publicações do usuário que será seguido
    session.set_user_interact(amount=2, randomize=True, percentage=100, media='Photo')

    #seguir 100 novas contas com base nas tags abaixo
    #session.follow_by_tags(['#vivaolinux', "#linuxbrasil"], amount=100)
    session.follow_by_tags(['#vivaolinux'], amount=5)
