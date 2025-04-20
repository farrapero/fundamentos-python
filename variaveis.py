# MÓDULO 01 — VARIÁVEIS EM PYTHON (v11.1)
# Projeto: Cartão de Visita Digital + Contexto Real e Didática Aprimorada

import random

def linha():
    print("-" * 60)

# 0) Introdução com analogia e uso real
print("📘 MÓDULO 01 — VARIÁVEIS EM PYTHON (v11.1)")
print("💡 Analogias, exemplos reais e contextos")
linha()
print("""
Imagine que variáveis são como **Caixinhas Rotuladas**:

  ┌───────────────┐
  │    nome       │ → guarda um texto, ex: "Lucas"
  └───────────────┘

  ┌───────────────┐
  │    idade      │ → guarda um número, ex: 30
  └───────────────┘

Você coloca **dentro** das caixinhas valores que serão usados 
depois. E o Python te dá o poder de criar, ler e atualizar 
essas caixinhas com código!

🔍 **Em projetos reais**:
- **Apps de finanças** usam variáveis para saldo e histórico.
- **Jogos** guardam pontuação, vidas e níveis.
- **Web** armazena nome, email e preferências do usuário.
- **Automação** salva caminhos de arquivos e configurações.

Neste módulo você vai aprender:
1) O que é uma variável (caixinha)  
2) Como criar e nomear caixinhas no Python  
3) Como guardar textos, inteiros e decimais  
4) Como ler, usar e atualizar valores  
5) Como evitar erros comuns  
6) Como aplicar tudo num mini‑projeto real  
""")
input("Pressione ENTER para começar…")

# 1.5) Tipos de Dados, input() e Conversão
linha()
print("""
📚 O QUE É input() & TIPOS DE DADOS

1️⃣ **O comando input():**
   - Exibe uma **mensagem** na tela, espera você digitar algo e então
     retorna **tudo** que você digitou como texto (string).
   - Exemplo:
       nome = input("Digite seu nome: ")
     Aqui, se você digitar Lucas e pressionar ENTER,
     a variável nome receberá o texto "Lucas".

2️⃣ Por que isso importa?
   Mesmo que você digite um número, ele sempre vem como texto:
       idade_texto = input("Idade: ")
       # Se digitar 25, idade_texto == "25" (string)

3️⃣ Se você tentar misturar texto e número:
       texto = "25"
       resultado = texto + 10
     → TypeError: não dá para somar string com int.

4️⃣ Para usar como número, converta com int():
       idade = int(idade_texto)   # transforma "25" em 25 (int)

Resumo:
- **input()** → sempre string  
- Para operações numéricas → use **int()**

⚠️ Erro comum:
   TypeError: can only concatenate str (not "int") to str
""")
input("ENTER para criar variáveis básicas…")


# 2) Coleta de dados
linha()
print("✍️  Crie suas variáveis básicas (digite só o valor):")

# Nome (string)
while True:
    nome = input("1️⃣  Nome (texto): ").strip().title()
    if nome:
        break
    print("❌ O nome não pode ficar em branco. Ex: Lucas")

# Idade (int)
while True:
    txt = input("2️⃣  Idade (número inteiro): ").strip()
    if txt.isdigit():
        idade = int(txt)
        break
    print("❌ Digite apenas dígitos. Ex: 30 (sem aspas)")

input("Variáveis básicas criadas! ENTER para prática de sintaxe…")

# 3) Prática dirigida de sintaxe
linha()
print("""
🖊️ PRÁTICA DE SINTAXE

a) Crie hobby_str como string:
   hobby_str = "seu hobby"

b) Crie nota como inteiro:
   nota = 8
""")
# hobby_str
while True:
    cmd = input("> Digite hobby_str = \"...\": ").strip()
    try:
        exec(cmd, globals())
        if 'hobby_str' in globals() and isinstance(hobby_str, str):
            print(f"✅ hobby_str criada: {hobby_str}")
            break
        else:
            print("❌ Variável hobby_str incorreta. Precisa ser string.")
    except SyntaxError:
        print("❌ Erro de sintaxe — lembre-se das aspas.")
    except Exception as e:
        print(f"❌ Outro erro: {e}")

# nota
while True:
    cmd = input("> Digite nota = 8 : ").strip()
    try:
        exec(cmd, globals())
        if 'nota' in globals() and isinstance(nota, int):
            print(f"✅ nota criada: {nota}")
            break
        else:
            print("❌ Variável nota incorreta. Precisa ser inteiro, sem aspas.")
    except SyntaxError:
        print("❌ Erro de sintaxe.")
    except Exception as e:
        print(f"❌ Outro erro: {e}")

input("ENTER para ver seu cartão de visita…")

# Função para exibir cartão
def exibir_cartao(n, i, h, nt):
    linha()
    print("🧾  SEU CARTÃO DE VISITA DIGITAL")
    linha()
    print(f"👤 Nome : {n} ({type(n).__name__})")
    print(f"🎂 Idade: {i} ({type(i).__name__})")
    print(f"🎯 Hobby: {h} ({type(h).__name__})")
    print(f"🏆 Nota : {nt} ({type(nt).__name__})")
    linha()

# 4) Exibir cartão inicial
exibir_cartao(nome, idade, hobby_str, nota)

# 5) Atualização de variáveis com explicação
linha()
print("""
🔁 O que é atualizar uma variável?

Quando você faz:
    saldo = 100         # cria
    saldo = saldo + 50  # lê, soma e substitui

Ou seja, a 'caixinha' saldo ganha um novo valor.

Agora você pode atualizar:
- hobby_str = "novo hobby"   (string)
- nota = 10                  (inteiro)

Digite no formato **campo = valor**.
Pressione ENTER sem nada para encerrar.
""")
while True:
    upd = input("> ").strip()
    if not upd:
        print("🔒 Fim das atualizações.")
        break
    if "=" not in upd:
        print("❌ Formato inválido. Use campo=valor.")
        continue
    var, val = [p.strip() for p in upd.split("=", 1)]
    if var not in ("nome", "idade", "hobby_str", "nota"):
        print("❌ Variável não reconhecida. Use nome, idade, hobby_str ou nota.")
        continue
    try:
        exec(f"{var} = {val}", globals())
        print(f"✅ {var} atualizado para {eval(var)}")
        exibir_cartao(nome, idade, hobby_str, nota)
    except Exception as e:
        print(f"❌ Erro na atualização: {e}")

# 6) Aplicação simples: ano de nascimento
linha()
print("📅 Aplicação: calcular ano de nascimento")
ano_atual = 2025
ano_nasc = ano_atual - idade
print(f"Você nasceu por volta de {ano_nasc}.")
linha()
input("ENTER para ver um erro de tipo…")

# 7) Erro de TypeError explicado
print("""
❌ ERRO DE TYPE:

Imagine:
    anos = "25"
    idade2 = anos + 10

O Python avisa:
    TypeError: can only concatenate str (not 'int') to str

Porque tentou juntar texto ("25") com número (10).

✅ Correto:
    idade2 = int(anos) + 10
""")

# 8) Prática extra: segundo cartão completo
linha()
print("🧑‍💻 PRÁTICA EXTRA: Crie um segundo cartão completo")
while True:
    nome2 = input("• Nome 2 (texto): ").strip().title()
    if nome2: break
    print("❌ Não pode ficar vazio.")
while True:
    txt2 = input("• Idade 2 (número): ").strip()
    if txt2.isdigit():
        idade2 = int(txt2)
        break
    print("❌ Apenas dígitos.")
while True:
    hobby2 = input("• Hobby 2 (texto): ").strip()
    if hobby2: break
    print("❌ Não pode ficar vazio.")
while True:
    nt2 = input("• Nota 2 (0-10): ").strip()
    if nt2.isdigit():
        nota2 = int(nt2)
        break
    print("❌ Digite um número válido.")
input("ENTER para exibir o segundo cartão…")
exibir_cartao(nome2, idade2, hobby2, nota2)

# 9) Exercício livre: adicionar email
linha()
print("""
🎨 EXERCÍCIO LIVRE:
Adicione uma variável email:
email = "seu@exemplo.com"
Pressione ENTER em branco para pular.
""")
while True:
    code = input("> ").strip()
    if not code:
        print("⚠️ Pulando email.")
        break
    if not code.startswith("email"):
        print("❌ Comece com 'email ='.")
        continue
    try:
        exec(code, globals())
        print(f"✅ email criado: {email}")
        break
    except Exception as e:
        print(f"❌ Erro: {e}")

# 10) Síntese e curiosidade
linha()
print("🧠 O QUE VOCÊ APRENDEU:")
for tópico in [
    "✔️ Variáveis como caixinhas rotuladas",
    "✔️ Criação de textos e inteiros",
    "✔️ Conversão de input() para int()",
    "✔️ Sintaxe de atribuição com exec()",
    "✔️ Atualização (reatribuição) de valores",
    "✔️ Tratamento de erros (TypeError, SyntaxError)",
    "✔️ Autonomia para criar variáveis novas"
]:
    print(tópico)
linha()
cur = random.choice([
    "📱 Apps guardam variáveis para lembrar suas preferências.",
    "🎮 Jogos usam variáveis para pontuação e vidas.",
    "📊 Em finanças, variáveis representam saldos e transações."
])
print("🎲 Curiosidade:", cur)
linha()
print("🎉 Parabéns! Você concluiu o Módulo 01 — Variáveis (v11.1) com sucesso.")
