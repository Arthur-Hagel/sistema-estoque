estoque = {}
# Cria um dicionário vazio que vai guardar todos os produtos.
# Cada produto será uma "chave" (nome) apontando para outro dicionário (quantidade e preço).

while True:
    # Loop infinito: o menu vai se repetir pra sempre, até algo com "break" interromper.
    
    print("\n--- MENU ---")
    # \n imprime uma linha em branco antes do título, pra separar visualmente do print anterior.
    print("1. Adicionar produto")
    print("2. Listar produto")
    print("3. Atualizar quantidade")
    print("4. Remover produto")
    print("5. Sair")
    # Esses 5 prints só exibem as opções na tela, não fazem nenhuma lógica.

    opcao = input("Escolha uma opção: ")
    # Pausa o programa esperando o usuário digitar algo e apertar Enter.
    # O valor digitado (sempre como texto/string) fica guardado na variável "opcao".

    if opcao == "5":
        # Compara o texto digitado com a string "5".
        print("Saindo do sistema...")
        break
        # "break" interrompe o "while True", encerrando o loop (e o programa, já que não há mais código depois).

    elif opcao == "1":
        # "elif" = "senão, se". Só é checado se o "if" acima foi falso.
        nome = input("Nome do produto: ")
        # Pede e guarda o nome do produto que o usuário quer cadastrar.

        if nome in estoque:
            # Verifica se essa chave (nome) já existe dentro do dicionário "estoque".
            print(f"Produto '{nome}' já existe! Use a opção 3 para atualizar a quantidade.")
            # f-string: permite inserir o valor da variável "nome" direto dentro do texto usando {}.
        else:
            # Só executa se o produto NÃO existir ainda.
            quantidade = int(input("Quantidade: "))
            # input() sempre devolve texto; int() converte esse texto pra número inteiro.
            preco = float(input("Preço: "))
            # float() converte o texto pra número decimal (com casas depois da vírgula).

            estoque[nome] = {"quantidade": quantidade, "preco": preco}
            # Cria uma nova entrada no dicionário "estoque":
            # a chave é o "nome", e o valor é outro dicionário com quantidade e preço.
            print(f"Produto '{nome}' adicionado com sucesso!")
            # Confirma a ação pro usuário.

    elif opcao == "2":
        if not estoque:
            # "not estoque" é True quando o dicionário está vazio.
            print("Estoque vazio.")
        else:
            for nome, dados in estoque.items():
                # .items() percorre o dicionário devolvendo pares (chave, valor).
                # "nome" recebe a chave (ex: "arroz"), "dados" recebe o dicionário interno (quantidade/preco).
                print(f"{nome} | Quantidade: {dados['quantidade']} | Preço: R$ {dados['preco']:.2f}")
                # Acessa os valores de dentro de "dados" usando as chaves 'quantidade' e 'preco'.
                # ":.2f" formata o número decimal com exatamente 2 casas depois da vírgula.

    elif opcao == "3":
        nome = input("Nome do produto a atualizar: ")

        if nome in estoque:
            nova_quantidade = int(input("Nova quantidade: "))
            estoque[nome]["quantidade"] = nova_quantidade
            # Acessa o produto pelo nome, entra no dicionário interno, e troca só o valor de "quantidade".
            # O "preco" desse produto continua intacto, sem ser mexido.
            print(f"Quantidade de '{nome}' atualizada para {nova_quantidade}.")
        else:
            print(f"Produto '{nome}' não encontrado.")

    elif opcao == "4":
        nome = input("Nome do produto a remover: ")

        if nome in estoque:
            del estoque[nome]
            # "del" remove essa chave (e o valor junto) do dicionário completamente.
            print(f"Produto '{nome}' removido com sucesso.")
        else:
            print(f"Produto '{nome}' não encontrado.")