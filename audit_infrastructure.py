import socket
import ssl

def verifier_securite_web(host, port_audit):
    """
    Effectue un diagnostic de l'infrastructure cible :
    1. Vérification de l'ouverture de ports nons tandard.
    2. Analyse de la validité du certificat SSL.
    """
    print(f"--- Rapport d'audit pour : {host} ---")
    
    # --- TEST DE VULNÉRABILITÉ PORTUAIRE ---
    # On vérifie si le port spécifié (ex: 888) accepte les connexions
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(3) # Timeout pour éviter les attentes infinies
    
    connexion_result = client_socket.connect_ex((host, port_audit))
    if connexion_result == 0:
        print(f"[ALERTE] Port {port_audit} : OUVERT. Risque d'exposition détecté.")
    else:
        print(f"[INFO] Port {port_audit} : Fermé ou filtré.")
    client_socket.close()

    # --- ANALYSE DU CERTIFICAT SSL ---
    # On tente d'établir une connexion sécurisée pour extraire les métadonnées du certificat
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                certificat = ssock.getpeercert()
                # Extraction de la date d'expiration
                date_expiration = certificat['notAfter']
                print(f"[INFO] Certificat SSL valide. Expiration : {date_expiration}")
    except Exception:
        print("[ALERTE CRITIQUE] Erreur SSL : Certificat expiré, invalide ou absent.")

if __name__ == "__main__":
    # Diagnostic appliquée au domaine de l'agence GDI
    verifier_securite_web("numlab.ardi-gdi.fr", 888)