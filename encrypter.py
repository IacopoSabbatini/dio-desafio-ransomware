"""
Demonstração educacional de criptografia de arquivos.
Opera SOMENTE nos arquivos .txt diretamente dentro de ./test_files.
Os originais são preservados; a saída recebe a extensão .encrypted.
"""
from pathlib import Path
from cryptography.fernet import Fernet

BASE_DIR = Path(__file__).resolve().parent
TEST_DIR = BASE_DIR / "test_files"
KEY_FILE = BASE_DIR / "fernet.key"


def main():
    TEST_DIR.mkdir(exist_ok=True)

    if KEY_FILE.exists():
        print("A chave fernet.key já existe. Ela será reutilizada.")
        key = KEY_FILE.read_bytes()
    else:
        key = Fernet.generate_key()
        KEY_FILE.write_bytes(key)
        print(f"Chave criada em: {KEY_FILE.name}")
        print("Guarde essa chave em local seguro; sem ela não será possível descriptografar.")

    cipher = Fernet(key)
    files = [p for p in TEST_DIR.glob("*.txt") if p.is_file()]

    if not files:
        print("Nenhum arquivo .txt encontrado diretamente em test_files/.")
        return

    for source in files:
        encrypted_path = source.with_suffix(source.suffix + ".encrypted")
        encrypted_path.write_bytes(cipher.encrypt(source.read_bytes()))
        print(f"Criptografado: {source.name} -> {encrypted_path.name}")

    print("Concluído. Os arquivos originais foram mantidos intactos.")


if __name__ == "__main__":
    main()
