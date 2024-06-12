import subprocess



def model_load():
    # Définir la commande et ses arguments sous forme de liste
    commands = [["curl", "-fsSL", "https://ollama.com/install.sh",  "|",  "sh"], ["ollama", "pull", "mixtral:8x22b"], ["ollama", "serve"], ["ollama", "run", "mixtral:latest"], ["POST",  "/api/generate"]]

    # Exécuter la commande
    for i in commands:
        result = subprocess.run(i, capture_output=True, text=True)
        msg = ""

        for a in i:
            msg = msg + " " + a

        # Afficher la sortie standard et la sortie d'erreur
        print(f'{msg} Standard output:')
        print(result.stdout)
        print(f'{msg} Standard error:')
        print(result.stderr)
