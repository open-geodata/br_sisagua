# Siságua

<br>

O Sistema de Informação de Vigilância da Qualidade da Água para Consumo Humano ([Siságua](http://sisagua.saude.gov.br/sisagua/login.jsf)) é um instrumento do Programa Nacional de Vigilância da Qualidade da Água para consumo Humano (Vigiagua), construído com base no referido programa e na Portaria MS n° 2.914/2011 (atualmente, [Anexo XX da Portaria de Consolidação n° 05/2017](https://cevs-admin.rs.gov.br/upload/arquivos/201804/26143402-anexo-xx.pdf)), que tem como objetivo auxiliar o gerenciamento de riscos à saúde associados à qualidade da água destinada ao consumo humano, como parte integrante das ações de prevenção de agravos e de promoção da saúde, previstas no Sistema Único de Saúde.

O Siságua armazena informações cadastrais sobre os sistemas e soluções alternativas de abastecimento de água para consumo humano, bem como sobre a qualidade da água proveniente de cada uma das formas cadastradas, inferida pelos prestadores do serviço (controle) e pelo setor saúde (vigilância).

A entrada de dados é dividida, basicamente, em três partes:

1. O módulo de **Cadastro** tem como finalidade armazenar informações sobre as características físicas e operacionais das formas de abastecimento de água utilizadas pela população.
2. O módulo de **Controle** tem como finalidade armazenar informações sobre o monitoramento da qualidade da água realizado pelos responsáveis pelo abastecimento coletivo de água para consumo humano.
3. O módulo de **Vigilância** tem como finalidade armazenar informações sobre as inspeções sanitárias das formas de abastecimento de água e sobre o monitoramento da sua qualidade realizado pelo setor saúde.

Os dados da Plataforma Siságua estão disponíveis no [Portal de Dados Abertos](http://www.dados.gov.br/dataset?tags=SISAGUA) do Governo Federal. Importante mencionar que os dados disponibilizados pelo Portal não são sincronizados automaticamente com a Plataforma Siságua, ou seja, quando uma determinada vigilância sanitária municipal insere os dados no Siságua, estará disponibilizado apenas nessa Plataforma somente na próxima atualização dos repositórios do Portal de Dados Abertos, quando tais dados estarão disponíveis para acesso público.

<br>

---

### Etapas

1. Obter os dados em formato *.zip*
2. Converter os arquivos *.zip* para formato *.parquet*
3. Reparticionar os dados em formato *.parquet*, utilizando **estado** e **município**.


Para obtenção dos dados, há um arquivo na pasta *docs* com todas as URLs. COm isso é possível fazer o download utilizando um gerenciador de *download*. Sugere-se o [jdownloader](https://jdownloader.org). Para instalar em:
- [Windows](https://jdownloader.org/download/index)
- [Ubuntu e outras distribuições linux com *snap*](https://snapcraft.io/install/jdownloader2/ubuntu)

<br>

---

### Atualização

Dados baixados em 25.02.2022

<br>

---

### *TODO*

1. <strike>Criar um arquivo txt com links para fazer o *download*</strike>. Feito em 15.03.2022.
2. <strike>Usar um gerenciador de download</strike>
