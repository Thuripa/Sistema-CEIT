import pyrebase


# Credenciais do Banco
config = {
    "apiKey": "AIzaSyA-4KDbTkVKWISJDElVmdNjwHCleTeGZl8",
    "authDomain": "sitema-ceit.firebaseapp.com",
    "databaseURL": "https://sitema-ceit-default-rtdb.firebaseio.com",
    "projectId": "sitema-ceit",
    "storageBucket": "sitema-ceit.appspot.com",
    "messagingSenderId": "847435602498",
    "appId": "1:847435602498:web:0ea74f36d9790265222bdb",
    "measurementId": "G-7PC3DC90MX"
};

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

db = firebase.database()


# Cria Usuário
email = "tutainha@tutanota.com"
pwd = "tutainha123"

# Registra usuário e senha no Google Authentication
#auth.create_user_with_email_and_password(email, pwd)

# Registra o token de autenticação
auth_token = auth.sign_in_with_email_and_password(email, pwd)

# Registra o ID Token, expira a cada 1 hora
token_id = auth_token['idToken']

# Pega o token atualizado (erro sla pq)
#token_id = auth.refresh(auth_token['refreshToken'])

# Envia um email de confirmação
#auth.send_email_verification(token_id)

# Pega Informações da Conta
auth.get_account_info(token_id)

# Pega especificamente a informação de email verificado da conta (retorna Boolean)
auth.get_account_info(token_id)['users'][0]['emailVerified']

# Pega especificamente a informação de ultima atualização do token da conta (retorna um daytime)
auth.get_account_info(token_id)['users'][0]['lastRefreshAt']

# Envia um email de redefinição de senha
#auth.send_password_reset_email(email)

# Novo usuário
novo_usuario = {

    'nome' : 'jao da silva',
    'nascimento' : '01/02/2000',
    'turma' : '600',
    'email' : 'setiver@tomara.com'

};


# Adiciona novo usuario no banco na "tabela" usuarios
db.child('usuarios').child('jao da silva').set(novo_usuario, token_id)
