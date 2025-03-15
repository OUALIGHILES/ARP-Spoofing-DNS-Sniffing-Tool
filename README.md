# ARP Spoofing & DNS Sniffing Tool

Ce projet est un outil de sécurité réseau qui permet de réaliser des attaques ARP Spoofing et de capturer les requêtes DNS. Il est développé en Python en utilisant la bibliothèque Scapy pour manipuler les paquets réseau.

##  Fonctionnalités

- **ARP Spoofing** : Permet de rediriger le trafic réseau entre une cible et la passerelle (gateway) en envoyant des paquets ARP falsifiés.
- **DNS Sniffing** : Capture et affiche les requêtes DNS envoyées par les appareils sur le réseau.

## Utilisation

1. **ARP Spoofing** : Le script envoie des paquets ARP falsifiés à la cible et à la passerelle pour rediriger le trafic.
2. **DNS Sniffing** : Le script écoute sur le port UDP 53 pour capturer les requêtes DNS et affiche l'adresse IP source ainsi que la requête DNS.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git

## Installation les biblioteques

2. Installez les dépendances :

   ```bash
   pip install scapy

3. Exécutez le script :
   ```bash
   python votre_script.py

4. Exemple de sortie :
   ```bash
        [+] ARP spoofing started :
    --------------------------------------------------
    IP Address        DNS Query
    --------------------------------------------------
    192.168.0.10      example.com
    192.168.0.15      another-example.com

## Avertissement
Ce projet est à des fins éducatives uniquement. L'utilisation de cet outil pour des activités malveillantes est strictement interdite. L'auteur n'est pas responsable de toute utilisation abusive de ce logiciel.
## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
