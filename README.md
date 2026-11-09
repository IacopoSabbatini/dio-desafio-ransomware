# Simulação Educacional de Criptografia de Arquivos com Python

Projeto desenvolvido como atividade prática do desafio de Cibersegurança da DIO. O objetivo é compreender, em ambiente controlado, os conceitos de criptografia simétrica e recuperação de arquivos.

> **Aviso de segurança:** este repositório contém uma demonstração didática, não um ransomware operacional. Os scripts atuam exclusivamente sobre arquivos `.txt` diretamente na pasta `test_files/`, não percorrem subpastas, não acessam diretórios externos e não apagam nem sobrescrevem os originais.

## Objetivos

- Aplicar criptografia simétrica usando Python.
- Entender o papel de uma chave criptográfica.
- Descriptografar dados previamente protegidos.
- Praticar organização, documentação e versionamento com Git/GitHub.

## Tecnologias

- Python 3.10 ou superior
- [Cryptography](https://cryptography.io/)
- Git e GitHub

## Estrutura

```text
dio-desafio-ransomware/
├── encrypter.py
├── decrypter.py
├── requirements.txt
├── README.md
├── .gitignore
├── fernet.key          # gerada localmente; ignorada pelo Git
└── test_files/
    └── arquivo_teste.txt
```

## Como executar

### 1. Preparar o ambiente

Clone o repositório e entre na pasta:

```bash
git clone URL_DO_SEU_REPOSITORIO
cd dio-desafio-ransomware
```

Crie e ative um ambiente virtual (opcional, recomendado):

```bash
python -m venv .venv
```

Windows (Git Bash):

```bash
source .venv/Scripts/activate
```

Instale a dependência:

```bash
pip install -r requirements.txt
```

### 2. Executar a demonstração

Crie ou coloque um arquivo `.txt` de teste dentro de `test_files/`. Em seguida:

```bash
python encrypter.py
```

O programa gera uma chave Fernet local (`fernet.key`) e cria uma cópia criptografada com a extensão `.txt.encrypted`. O arquivo original permanece intacto.

Para recuperar o conteúdo:

```bash
python decrypter.py
```

O resultado é salvo com a extensão `.decrypted`. Compare o conteúdo recuperado com o arquivo original.

## Como funciona

1. O script de criptografia gera uma chave com `Fernet.generate_key()` na primeira execução.
2. A chave é salva localmente em `fernet.key`.
3. O conteúdo do arquivo de teste é criptografado com Fernet, uma implementação de criptografia simétrica autenticada.
4. O script de descriptografia usa a mesma chave para validar e recuperar o conteúdo.
5. Os arquivos originais e criptografados são mantidos para permitir a comparação.

## Cuidados importantes

- **Não compartilhe `fernet.key`.** Quem tiver acesso à chave poderá descriptografar os arquivos produzidos por esta demonstração.
- O arquivo de chave está listado no `.gitignore` e não deve ser enviado ao GitHub.
- Se a chave for perdida, os arquivos criptografados não poderão ser recuperados por este exemplo.
- Use somente arquivos fictícios e próprios dentro de `test_files/`.
- Este projeto não possui persistência, propagação, execução automática, evasão ou acesso a arquivos fora da pasta de testes.

## Aprendizados

- Uso de bibliotecas criptográficas em Python.
- Diferença entre criptografar e descriptografar.
- Importância do gerenciamento seguro de chaves.
- Organização de um projeto e documentação técnica com Markdown.
- Versionamento de código com Git e GitHub.

## Possíveis melhorias futuras

- Criar testes automatizados para validar a integridade do conteúdo recuperado.
- Adicionar tratamento para arquivos vazios e erros de leitura/escrita.
- Registrar resultados de execução sem armazenar dados sensíveis.

## Créditos

Desafio proposto no percurso de Cibersegurança da [DIO](https://www.dio.me/), com repositório de referência disponibilizado pelo instrutor:
https://github.com/cassiano-dio/cibersecurity-desafio-ransomware

Este projeto é uma implementação educacional independente, com escopo restrito e proteções para evitar alterações destrutivas.
