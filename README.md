<h1>Teste S4 com Flask e SQLAlchemy</h1>

  Este código foi feito usando a versão 3.0.2 do Flask e 3.12.0 do Python.
  Para executa-lo em sua máquina basta clonar este repositório e instalar o Python (preferencialmente versão 3.12.0).

  Após abrir o projeto na sua IDE é recomendado criar um ambiente virtual na raiz do projeto para instalar as dependências.
  O comando para criar o ambiente virtual é python -m venv .venv (sendo .venv a pasta do ambiente virtual).
  Após criar o ambiente virtual ative-o com o comando: 
  ```bash
  .venv\Scripts\activate
  ```

  Com o ambiente virtual ativo basta instalar as dependências que foram utilizadas no projeto, seguem os comandos para a instalação de ambas as dependências utilizadas:
  ```bash
  pip install flask
  ```
 
  Este comando instala o framework Flask no projeto.

  ```bash
  pip install flask-sqlalchemy
  ```

  Este comando instala a ORM que será usada para criar os modelos e acessar o banco de dados.

  Por se tratar de um Micro Framework o Flask não tem um padrão de arquivos bem definido, então vai depender da arquitetura escolhida para o projeto.
  Neste projeto eu utilizei uma arquitetura bem simples por se tratar de um código de demonstração. 
  A base de dados utilizada é o SQLite por se tratar de um banco de dados de facil implementação, caso queiram testar com outro banco de dados basta trocar a variável de 
  conexão, a ORM irá funcionar normalmente com outro banco de dados SQL.

  Para implmentar a autenticação de usuários e as funcionalidades de CRUD foi utilizada a classe User.
  Essa classe é manipulada pela classe auth.py, que é uma blueprint pra acessar os endpoints de login e registro de usuário.

  E pra implementação do CRUD de Produtos foi usada a classe products.py, que também é uma blueprint de acesso a todos os endpoints de CRUD.
  
  
