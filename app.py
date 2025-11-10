import requests
import sys

# URL de l'API publique Chuck Norris Jokes
API_URL = "https://api.chucknorris.io/jokes/random"

def get_joke():
    """Récupère une blague aléatoire et l'affiche."""
    print("🧠 Tentative de récupération d'une blague de Chuck Norris...")
    try:
        # Effectuer la requête GET avec un timeout de 10 secondes
        response = requests.get(API_URL, timeout=10)
        
        # Lève une exception si le statut de la réponse n'est pas 2xx
        response.raise_for_status()
        
        # Convertir la réponse JSON
        data = response.json()
        
        # Extraire la blague (clé 'value')
        joke = data.get("value")
        
        if joke:
            print("\n💥 Blague de Chuck Norris :")
            print("---------------------------------")
            print(joke)
            print("---------------------------------")
        else:
            print("❌ Erreur : Blague non trouvée dans la réponse de l'API.", file=sys.stderr)

    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de requête (connexion ou HTTP) : {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Une erreur inattendue s'est produite : {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    get_joke()
