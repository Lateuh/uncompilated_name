# uncompilated_name
Bot de gestion de connaissances, interface sous forme de page web, le tout réalisé en python (framework Django)

Tous les modules requis au fonctionnement du programme sont dans requirements.txt

Ensuite, vous devrez créer une base de données SQL nommée "un".
Vous devrez également modifier le fichier uncompilated_name/uncompilated_name/settings.py en fonction du SGBD choisi.
En console, positionnez vous dans uncompilated_name/ et entrez :
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

La page du bot se trouve à l'adresse "localhost:8000/" depuis votre navigateur favoris.
Vous pouvez interagir directement sans avoir rempli la base de données mais le bot devra importer au fur et à mesure les termes entrés.
Nous conseillons, si vous avez le temps de lancer l'extraction ci-dessous.
La page d'extraction des 1200 termes les plus utilisés en français et de ses relations, se fait depuis l'adresse :
"localhost:8000/chatbot/extraction" (environ 1h30 d'exécution)
