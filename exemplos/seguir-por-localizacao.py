"""
Bot de Instagram baseado no InstaPy

Objetivo: seguir novas contas com base em localização

"""

#imports
from instapy import InstaPy
from instapy import smart_run
import getpass

#credenciais
insta_username = input("Usuário: ")
insta_password = getpass.getpass("Senha: ")

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
        enabled=False,
        delimit_by_numbers=True,
        max_followers=15000,
        min_followers=10,
        min_following=10
    )
    
    #acessar o link abaixo e navegar até a localização desejada:
    #
    # https://www.instagram.com/explore/locations/
    #
    #copiar tudo o que vier após /location/ na URL final, exemplo:
    #
    # /112047398814697/sao-paulo-brazil/
    #

    #configurar para interagir com 2 publicações do usuário que será seguido
    #session.set_user_interact(amount=2, randomize=True, percentage=100, media='Photo')

    #seguir 30 novas contas com base nas localizações abaixo
    #é possível adicionar mais que uma localização
    session.follow_by_locations(['112047398814697/sao-paulo-brazil/'], amount=30, skip_top_posts=False)


