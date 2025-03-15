ARP Spoofing & DNS Sniffing Tool
Ce projet est un outil de sécurité réseau qui permet de réaliser des attaques ARP Spoofing et de capturer les requêtes DNS. Il est développé en Python en utilisant la bibliothèque Scapy pour manipuler les paquets réseau.

Fonctionnalités
ARP Spoofing : Permet de rediriger le trafic réseau entre une cible et la passerelle (gateway) en envoyant des paquets ARP falsifiés.

DNS Sniffing : Capture et affiche les requêtes DNS envoyées par les appareils sur le réseau.

Utilisation
ARP Spoofing : Le script envoie des paquets ARP falsifiés à la cible et à la passerelle pour rediriger le trafic.

DNS Sniffing : Le script écoute sur le port UDP 53 pour capturer les requêtes DNS et affiche l'adresse IP source ainsi que la requête DNS.

Installation
Clonez le dépôt :

bash
Copy
git clone https://github.com/votre-utilisateur/votre-repo.git
Installez les dépendances :

bash
Copy
pip install scapy
Exécutez le script :

bash
Copy
python votre_script.py
Exemple de sortie
Copy
[+] ARP spoofing started :
--------------------------------------------------
IP Address        DNS Query
--------------------------------------------------
192.168.0.10      example.com
192.168.0.15      another-example.com
Avertissement
Ce projet est à des fins éducatives uniquement. L'utilisation de cet outil pour des activités malveillantes est strictement interdite. L'auteur n'est pas responsable de toute utilisation abusive de ce logiciel.

Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

N'oubliez pas de remplacer les placeholders comme votre-utilisateur, votre-repo, et votre_script.py par les informations appropriées pour votre projet.
