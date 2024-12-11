import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu


lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'
   },
   'root': {
       'name': 'root',
       'password': 'rootMDP',
       'email': 'admin@gmail.com',
       'failed_login_attemps': 0, # Sera géré automatiquement
       'logged_in': False, # Sera géré automatiquement
       'role': 'administrateur'
       }
       }}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil():
    
    with st.sidebar:
        name = lesDonneesDesComptes['usernames']['root']['name']
        st.write(f"Bienvenue {name}")
        authenticator.logout("Déconnexion")
        selection = option_menu(
            menu_title="Menu",
            options = ["Accueil", "Photos des chats"]
        )

    if selection == "Accueil":
        st.title("Bienvenue sur la page d'accueil !")

        st.image("https://gifdb.com/images/high/standing-ovation-crowd-applause-oscar-awards-ai72icmh1ac7apdz.gif")

    elif selection == "Photos des chats":
        st.title("Bienvenue sur l'album photo")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://t4.ftcdn.net/jpg/03/03/62/45/240_F_303624505_u0bFT1Rnoj8CMUSs8wMCwoKlnWlh5Jiq.jpg")
        
        with col2:
            st.image("https://t4.ftcdn.net/jpg/02/66/72/41/360_F_266724172_Iy8gdKgMa7XmrhYYxLCxyhx6J7070Pr8.jpg")
            
        with col3:
            st.image("data:image/jpeg;base64,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")      


if st.session_state["authentication_status"]:
    accueil()
    

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
