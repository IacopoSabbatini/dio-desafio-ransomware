"""
Demonstração educacional de descriptografia.
Opera SOMENTE nos arquivos *.txt.encrypted diretamente dentro de ./test_files.
Cria arquivos recuperados com a extensão .decrypted e preserva os criptografados.
"""
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

BASE_DIR = Path(__file__).resolve().parent
TEST_DIR = BASE_DIR / "test_files"
KEY_FILE = BASE_DIR / "fernet.key"


def main():
    if not KEY_FILE.exists():
        print("Chave não encontrada. Execute encrypter.py primeiro.")
        return

    cipher = Fernet(KEY_FILE.read_bytes())
    files = [p for p in TEST_DIR.glob("*.txt.encrypted") if p.is_file()]

    if not files:
        print("Nenhum arquivo .txt.encrypted encontrado em test_files/.")
        return

    for encrypted_path in files:
        output_path = encrypted_path.with_suffix(".decrypted")
        try:
            plaintext = cipher.decrypt(encrypted_path.read_bytes())
            output_path.write_bytes(plaintext)
            print(f"Recuperado: {encrypted_path.name} -> {output_path.name}")
        except InvalidToken:
            print(f"Falha em {encrypted_path.name}: chave incorreta ou arquivo alterado.")

    print("Concluído. Os arquivos criptografados foram preservados.")


if __name__ == "__main__":
    main()
