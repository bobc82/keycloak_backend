# keycloak_backend
base example auth backend

- Installare keycloak, es. keycloak-24.0.1.zip
- Dentro PostgreeSQL creare un database chiamato keycloak, con utente keycloak e password mysecret (ricordarsi di aggiungere i permessi all'utente keycloak dentro lo schema public)
- Scaricare il file jdbc che collega keycloak a postgreesql (assicurarsi di avere installato OpenJDK, anche l'ultima versione va bene), poi copiare il file dentro PATH_KEYCLOAK/providers/
- Per settare le variabili d'ambiente per java, aggiungere o modificare le seguenti:
```
JAVA_HOME=C:\Program Files\OpenJDK\jdk-24.0.2
PATH=%JAVA_HOME%\bin
```
- Configura il file PATH_KEYCLOAK/conf/keycloak.conf come segue:
```
db=postgres
db-url=jdbc:postgresql://localhost:5432/keycloak
db-username=keycloak
db-password=mypassword
hostname=localhost
```
- Da prompt settare le seguenti variabili d'ambiente:
```
set KEYCLOAK_ADMIN=admin
set KEYCLOAK_ADMIN_PASSWORD=admin
```
- Con il prompt andare all'interno della cartella bin ed eseguire: `kc.bat start-dev`

- Tramite browser accedere al seguente indirizzo: `http://localhost:8080`
- Si procede alla configurazione di keycloak andando prima in realm settings, creare un nuovo realm, dentro Realm name inserire "master" e dentro frontend URL inserire "http://localhost:8080"
- Sempre dentro keycloak andare su Clients, creare un nuovo client chiamandolo "react-frontend", all'interno di Valid Redirect URIs inserire "http://localhost:3000/*" e dentro Web origins inserire "http://localhost:3000"
- Creare un ulteriore client, in Client ID inserire "django-backend", in Root URL inserire "http://localhost:8000/" e dentro Valid Redirect URIs inserire "http://localhost:8000/*", andare su Client Authentication e settare flag a ON. Si attiverà la tab Credentials dalla quale si copierà il client secret da mettere dentro il file authentication.py a backend

# Test finale
- Avvia Keycloak (http://localhost:8080)
- Avvia Django (python manage.py runserver)
- Avvia React (npm start)
- L'utente verrà autenticato da Keycloak
- Cliccando “Chiama API protetta” invii il token a Django
- Django verifica con Keycloak via introspection
- Se valido, ricevi: Hai accesso autorizzato!
