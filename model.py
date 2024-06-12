import subprocess



def model_load():
    # Exécuter la commande curl pour télécharger le script
    curl_command = ["curl", "-fsSL", "https://ollama.com/install.sh"]

    # Lancer le processus curl
    curl_process = subprocess.Popen(curl_command, stdout=subprocess.PIPE)

    # Exécuter le script téléchargé avec sh en utilisant la sortie de curl comme entrée
    sh_command = ["sh"]
    sh_process = subprocess.Popen(sh_command, stdin=curl_process.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Fermer la sortie de curl pour permettre à curl de recevoir un signal EOF
    curl_process.stdout.close()

    # Capturer la sortie et l'erreur du processus sh
    stdout, stderr = sh_process.communicate()

    # Afficher la sortie standard et la sortie d'erreur
    print('Standard output of install command:')
    print(stdout.decode())
    print('Standard error of install command:')
    print(stderr.decode())
    print('Return code of install command:', sh_process.returncode)

    # Définir la commande et ses arguments sous forme de liste
    commands = [["ollama", "pull", "mixtral:8x22b"], ["ollama", "serve"], ["ollama", "run", "mixtral:latest"], ["POST",  "/api/generate"]]

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
