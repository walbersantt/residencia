Sistema de Organização Inteligente de Relatórios Corporativos. 
1. Objetivo do Projeto
Este projeto foi desenvolvido como solução para um problema real de produtividade em uma empresa digital. O objetivo é automatizar a triagem de arquivos exportados para a pasta Dados_Brutos, organizando-os de forma lógica por setor e data, garantindo agilidade operacional e integridade dos dados.

2. Tecnologias UtilizadasLinguagem: Python 3.12
Bibliotecas Nativas:
os: Manipulação de diretórios e caminhos de arquivos.
shutil: Movimentação e gerenciamento de arquivos no sistema.
datetime: Tratamento de carimbos de tempo para pastas e logs.

3. Como Executar a Aplicação
Certifique-se de ter o Python instalado.
Crie a pasta central chamada Dados_Brutos no diretório especificado na variável caminho_raiz do código.
Coloque os arquivos descompactados seguindo o padrão Setor_NomeDoRelatorio_Data.extensao dentro dessa pasta.
Execute o script:Bashpython residencia1.py
Utilize o menu interativo no terminal para selecionar a ação desejada (Organizar ou Ver Logs).

4. Estrutura do Projeto
O sistema segue uma arquitetura modular simplificada:
residencia1.py: Script principal contendo a lógica de negócio e interface.
historico_organizacao.txt: Arquivo gerado automaticamente para registro de logs.
Diretórios Gerados:Setor/Ano/Mes/: Estrutura hierárquica final dos relatórios.Erros_Nomenclatura/: Pasta para arquivos que não seguem o padrão obrigatório.

5. Funcionalidades e Evoluções Implementadas
Com base no framework de pontuação, as seguintes trilhas foram desenvolvidas:
Organização por Setor (Nível Base): Identificação automática de Marketing, Financeiro, RH, etc.
Tratamento de Erros (Nível Intermediário): Detecção de nomes fora do padrão e gestão de arquivos duplicados.
Logs Automáticos (Nível Intermediário): Registro de horários, arquivos processados e falhas em arquivo externo.
Organização por Data (Nível Intermediário): Criação de subpastas por Ano e Mês para evitar poluição visual nos diretórios.
Interface no Terminal (Nível Avançado): Menu interativo com mensagens amigáveis para o usuário final.

6. Principais Desafios Encontrados
Padronização de Nomes: A extração precisa da data e do setor via manipulação de strings exigiu validações para evitar que o programa parasse ao encontrar arquivos com nomes incompletos.
Conflitos de Arquivo: Implementar a lógica de renomear arquivos duplicados (adicionando um timestamp) para garantir que nenhum dado fosse sobrescrito acidentalmente.
