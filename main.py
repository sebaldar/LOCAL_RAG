import os
import sys

def mostra_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"Sto usando il Python in: {sys.executable}")
    print("="*30)
    print("   MATHEMATIC - RAG SYSTEM   ")
    print("="*30)
    print("1.  INDICIZZA DOCUMENTI (Aggiorna DB)")
    print("2.  AVVIA CHAT (OpenAI)")
    print("3.  RESET DATABASE (Cancella tutto)")
    print("4. ❌ ESCI")
    print("="*30)

def main():
    while True:
        mostra_menu()
        scelta = input("Scegli un'opzione (1-4): ")

        if scelta == '1':
            print("\n--- Avvio Indicizzazione ---")
            # Esegue lo script di indicizzazione
            os.system(f"{sys.executable} indicizza.py")
            input("\nPremere Invio per tornare al menu...")

        elif scelta == '2':
            print("\n--- Avvio Sessione Chat ---")
            # Esegue lo script della chat
            os.system(f"{sys.executable} chat_rag.py")
            # Non mettiamo input() qui perché la chat ha già il suo ciclo

        elif scelta == '3':
            conferma = input("\nSei sicuro di voler cancellare il DB? (s/n): ")
            if conferma.lower() == 's':
                path_db = "./my_knowledge_base"
                import shutil
                if os.path.exists(path_db):
                    shutil.rmtree(path_db)
                    print("[!] Database eliminato.")
                else:
                    print("[?] Database non trovato.")
            input("\nPremere Invio per tornare al menu...")

        elif scelta == '4':
            print("Chiusura sistema. Alla prossima!")
            break
        else:
            print("Scelta non valida.")
            import time
            time.sleep(1)

if __name__ == "__main__":
    main()
