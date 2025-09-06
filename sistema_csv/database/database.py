import json # Lidar com arquivos json
from pathlib import Path # Lidar com caminhos do windons 

    # JSON -> JavaScript Object Notation
class BancoFake:
    # Instanciando o início da classe
    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes": []} # Clientes iniciando como vazio

        # Carregar valores anteriores salvos
        self._carregar()

    def _carregar(self):
        """
        Carrega dados do arquivo JSON, se existir.
        Caso não exista, iniciando banco novo
        """
        caminho = Path(self.arquivo_db)
        # Verifica se o arquivo existe
        if caminho.is_file():
            # Abrindo arquivo no modo leitura em UTF-8 (PT-BR)
            with open(caminho, 'r', encoding="utf-8") as arquivo:
                # Carrega dados anteriores já salvos
                self.dados = json.load(arquivo)
        else:
            # Chamar função para criar novo arquivo
            self._salvar()

        def _salvar(self):
            """
            Salvar o conteúdo do self.dados no JSON
            """
            # Abrir o arquivo no modo W (Escrita)
            with open(self.arquivo_db, 'w', encoding="utf-8") as dados:
                # realizar um DUMP de Python para JSON
                # ensure_ascii = False -> Escritas, Emojis, não viram código
                # indent = identação -> 4 recuo
                json.dump(self.dados, dados, ensure_ascii=False, indent=4)

        def adicionar_clientes(self,cliente_dict):
            self.dados["clientes"].append(cliente_dict)
            self.salvar()

        def listar_clientes(self):
            return self.dados["clientes"]