# Coffee12
Repositório do grupo 12 da cadeira de Projetos 2 da Cesar School

## Grupo 
1.Clara Foster Maciel → cfm@cesar.school

2.Camila N. Farias → cnf@cesar.school

3.Júlia Furtado → jfms@cesar.school

4.Paulo Guilherme → phmg@cesar.school

5.Júlia Sales Novais → jsn@cesar.school

6.Luiz claudio →lcpmf@cesar.school

7.Maria Helena Urbano →mhgau@cesar.school

8.Pedro Dhalia→pmd2@cesar.school

9.Lucas Ferraz Santana Filgueiras → lfsf@cesar.school

10.Miguel José França → mjfa@cesar.school

11.Ícaro Barros → isb2@cesar.school


## Links Importantes

[Notion](https://distinct-rhubarb-0a9.notion.site/Notion-do-G12-3bfe1143afc6404eacf3dee57135c0dd?pvs=4)

[Google Sites](https://sites.google.com/cesar.school/queremoscafe-g12?usp=sharing)

[Google Drive](https://drive.google.com/drive/folders/1uxPJ6H_WYI4_X0wMdg2IrY-lmEsm_0Vb?usp=sharing)

[Diagrama de Atividades](https://lucid.app/lucidchart/972cf9c0-e0a0-48d4-ad8f-afb9259920fe/edit?beaconFlowId=7BD4ABDA3C7B83C2&invitationId=inv_3ca14424-7823-4e1f-a13d-d44c11858e4b&page=0_0)

[Protótipo De Baixa Fidelidade](https://lucid.app/lucidspark/826e0ab7-e4ec-4569-869a-10c4e6e42f82/edit?invitationId=inv_f55a1a31-7dd9-4893-a238-159cd9c78211&page=0_0#)

[Protótipo De Média Fidelidade](https://www.figma.com/design/X0xbd8GQEqfYpGZKV1Qcbi/Protótipo-G12?node-id=601-5967)

## ScreenCast's:

### SR1

[Screencast Mockup de Baixa Fidelidade](https://youtu.be/ejQEUXkaveA)

[Screencast Implementação Para o SR1](https://youtu.be/7aSX_eD-i7M)

### SR2

[Screencast Mockup de Media Fidelidade](https://youtu.be/-LEJ8bqCEFs)

[Screencast Implementação Para o SR2](https://youtu.be/SWBmWlas7Jo)

[Screencast de Testes do Sistema E CI\CD com Build e Deployment automatizado](https://youtu.be/z6082N5aFTo)


## Deployment na Azure

https://cafedagente.azurewebsites.net

## Histórias do Usuário:
<details>
  <summary>História 1: Requisitar itens esquecidos na cafeteria ( Implementada SR2 )</summary>

- Eu como usuário, gostaria de poder requisitar alguns itens que eu possa ter perdido no estabelecimento.
  - Descrição: O usuário envia uma requisição ao estabelecimento que pode responder se encontrou ou não o item do cliente.

**Cenário 1: Usuário envia uma solicitação de item perdido**
  - **Dado** que o usuário está na página de solicitação de itens perdidos
  - **Quando** o usuário insere a descrição do item "Guarda-chuva preto com cabo de madeira"
  - **E** o usuário clica no botão de enviar
  - **Então** o sistema deve salvar a solicitação
  - **E** o sistema deve exibir uma mensagem de confirmação "Sua solicitação foi enviada"

**Cenário 2: Estabelecimento responde a uma solicitação de item perdido**
  - **Dado** que o estabelecimento recebeu uma solicitação de item perdido
  - **Quando** o estabelecimento encontra o item descrito como "Guarda-chuva preto com cabo de madeira"
  - **E** o estabelecimento atualiza o status da solicitação para "Encontrado"
  - **Então** o usuário deve ser notificado de que seu item foi encontrado

**Cenário 3: Estabelecimento responde negativamente a uma solicitação de item perdido**
  - **Dado** que o estabelecimento recebeu uma solicitação de item perdido
  - **Quando** o estabelecimento não encontra o item descrito como "Guarda-chuva preto com cabo de madeira"
  - **E** o estabelecimento atualiza o status da solicitação para "Não Encontrado"
  - **Então** o usuário deve ser notificado de que seu item não foi encontrado
</details>

<details>
  <summary>História 2: Remoção de itens do cardápio ( Implementada SR2 )</summary>

- Eu como dono de cafeteria, gostaria de poder remover itens específicos do meu cardápio.
  - Descrição: O dono da cafeteria, poderia remover itens do cardápio, seja para altera-los ou para simplesmente retira-los do menu do estabelecimento.

**Cenário 1: Dono de cafeteria remove um item do cardápio**
  - **Dado** que o dono da cafeteria está logado na plataforma administrativa
  - **E** o dono acessa a página de gerenciamento do cardápio
  - **Quando** o dono digita o nome do item "Café Espresso" para remoção
  - **E** o dono confirma a remoção do item
  - **Então** o sistema deve remover o item "Café Espresso" do cardápio
</details>

<details>
  <summary>História 3: Dar Feedbacks sobre Cafeterias Visitadas ( Implementada SR2 )</summary>

- Eu como usuário gostaria de poder dar feedbacks referentes à cafeterias que visitei
  - Descrição: o usuário pode avaliar com notas de 1 a 5, juntamente de comentários, cafeterias das quais ele já foi frequentou.

**Cenário 1: Usuário dá feedback sobre cafeteria visitada**
  - **Dado** que o usuário está logado na plataforma
  - **E** o usuário está visualizando o perfil da cafeteria que visitou
  - **Quando** o usuário clica no botão "Dar Feedback" no perfil da cafeteria
  - **E** o usuário seleciona uma nota de avaliação de 0 a 5
  - **E** o usuário escreve um comentário sobre sua experiência
  - **E** o usuário confirma o envio do feedback
  - **Então** o sistema deve registrar o feedback com a nota e o comentário fornecidos pelo usuário
</details>

<details>
  <summary>História 4: Evidenciar Pratos Principais e Promoções ( Implementada SR2 )</summary>

- Eu como dono de cafeteria, gostaria de poder evidenciar os “pratos principais” e promoções do meu estabelecimento no perfil da minha cafeteria.
  - Descrição: o responsável pelo estabelecimento pode demonstrar os pratos principais e promoções de sua cafeteria em seu perfil. Exemplo:  “Promoção de Abril : MilkShake de Café R$ 18,00 por R$ 15,00 ; Tapioca de coco ralado R$ 15,50 por R$ 12,50 “

**Cenário 1: Exibir prato principal sem promoção no perfil da cafeteria**
  - **Dado** que o dono da cafeteria está logado na plataforma
  - **E** o dono da cafeteria cadastrou um prato principal chamado "Frango Grelhado"
  - **E** o preço do "Frango Grelhado" é R$ 25,00 e não há promoção
  - **Quando** o dono da cafeteria visualiza o perfil da cafeteria
  - **Então** o sistema deve exibir o "Frango Grelhado" com o preço R$ 25,00 sem indicar promoção

**Cenário 2: Exibir prato principal com promoção no perfil da cafeteria**
  - **Dado que o dono da cafeteria está logado na plataforma
  - **E** o dono da cafeteria cadastrou um prato principal chamado "Milkshake de Morango"
  - **E** o preço do "Milkshake de Morango" é R$ 15,00 e há uma promoção de R$ 12,00
  - **Quando** o dono da cafeteria visualiza o perfil da cafeteria
  - **Então** o sistema deve exibir o "Milkshake de Morango" com o preço cortado de R$ 15,00 e o preço promocional de R$ 12,00 ao lado
</details>

<details>
  <summary>História 5: Cadastrar Perfil da Cafeteria ( Implementada SR1 )</summary>

- Eu como dono de cafeteria, gostaria de cadastrar o perfil da minha cafeteria na plataforma, juntamente de seu nome, endereço e horários de funcionamento.
  - Descrição: O dono da cafeteria poderá ter um perfil da cafeteria para registrar  endereço do estabelecimento, nome do estabelecimento, telefone.

**Cenário: Cadastrar perfil da cafeteria na plataforma**
  - **Dado** que o dono da cafeteria está na página de cadastro de perfil da cafeteria
  - **Quando** o dono da cafeteria preenche o campo "Nome da Cafeteria" com "Café da Esquina"
  - **E** o dono da cafeteria preenche o campo "Endereço" com "Rua das Flores, 123"
  - **E** o dono da cafeteria preenche o campo "Telefone" com "(11) 98765-4321"
  - **E** o dono da cafeteria preenche o campo "Horário de Funcionamento" com "Seg a Sex: 08:00 - 18:00, Sáb: 09:00 - 14:00"
  - **E** o dono da cafeteria clica no botão "Cadastrar"
  - **Então** o sistema deve registrar o perfil da cafeteria com as informações fornecidas
</details>

<details>
  <summary>História 6: Alterar o Cardápio da Cafeteria ( Implementada SR1 )</summary>

- Eu como dono de cafeteria gostaria de poder alterar o cardápio da minha cafeteria.
  - Descrição: O dono da cafeteria pode adicionar ou remover itens de seu cardápio a qualquer momento.

**Cenário: Dono de cafeteria altera o cardápio**
  - **Dado** que o dono da cafeteria está logado na plataforma administrativa
  - **E** o dono da cafeteria acessa a página de gerenciamento do cardápio
  - **Quando** o dono da cafeteria adiciona um novo item chamado "Bolo de Cenoura"
  - **E** o dono da cafeteria remove um item chamado "Café Expresso"
  - **Então** o sistema deve exibir o item "Bolo de Cenoura" no cardápio
  - **E** o sistema deve remover o item "Café Expresso" do cardápio
</details>

<details>
  <summary>História 7: Cadastro de Pedidos na Cafeteria ( Implementada SR2 )</summary>

- Eu como dono de cafeteria gostaria de cadastrar um pedido na minha cafeteria.
  - Descrição: O dono da cafeteria pode cadastrar pedidos realizados pelos clientes no sistema para fins de gerenciamento e controle.

**Cenário: Dono de cafeteria cadastra um pedido**
  - **Dado** que o dono da cafeteria está logado na plataforma administrativa
  - **E** o dono da cafeteria acessa a página de cadastro de pedidos
  - **Quando** o dono da cafeteria insere o nome do cliente "João Silva"
  - **E** o dono da cafeteria seleciona o item "Café com Leite" do cardápio
  - **E** o dono da cafeteria clica no botão "Cadastrar Pedido"
  - **Então** o sistema deve registrar o pedido com o nome do cliente e o item selecionado
</details>

<details>
  <summary>História 8: Atualização de Pedidos na Cafeteria ( Implementada SR2 )</summary>

- Eu como dono de cafeteria gostaria de atualizar um pedido na minha cafeteria.
  - Descrição: O dono da cafeteria pode atualizar o status dos pedidos realizados pelos clientes, indicando se estão em preparação, prontos para entrega, etc.

**Cenário: Dono de cafeteria atualiza um pedido**
  - **Dado** que o dono da cafeteria está logado na plataforma administrativa
  - **E** o dono da cafeteria acessa a página de gerenciamento de pedidos
  - **Quando** o dono da cafeteria seleciona um pedido realizado por "Maria Oliveira"
  - **E** o dono da cafeteria altera o status do pedido para "Em Preparação"
  - **Então** o sistema deve atualizar o status do pedido para "Em Preparação"
</details>

<details>
  <summary>História 9: Consulta de Pedidos na Cafeteria ( Implementada SR2 )</summary>

- Eu como dono de cafeteria gostaria de consultar os pedidos realizados na minha cafeteria.
  - Descrição: O dono da cafeteria pode visualizar todos os pedidos realizados, juntamente com seus status e detalhes.

**Cenário: Dono de cafeteria consulta pedidos realizados**
  - **Dado** que o dono da cafeteria está logado na plataforma administrativa
  - **E** o dono da cafeteria acessa a página de consulta de pedidos
  - **Quando** o dono da cafeteria visualiza a lista de pedidos realizados
  - **Então** o sistema deve exibir todos os pedidos com seus respectivos status e detalhes
</details>

<details>
  <summary>História 10: Cadastro de Fornecedores da Cafeteria ( Implementada SR2 )</summary>

- Eu como dono de cafeteria gostaria de cadastrar fornecedores para minha cafeteria.
  - Descrição: O dono da cafeteria pode registrar fornecedores de produtos e insumos utilizados no estabelecimento.

**Cenário: Dono de cafeteria cadastra um fornecedor**
  - **Dado** que o dono da cafeteria está logado na plataforma administrativa
  - **E** o dono da cafeteria acessa a página de cadastro de fornecedores
  - **Quando** o dono da cafeteria insere o nome do fornecedor "Distribuidora de Alimentos XYZ"
  - **E** o dono da cafeteria insere o telefone do fornecedor "(11) 98765-4321"
  - **E** o dono da cafeteria insere o e-mail do fornecedor "contato@xyzalimentos.com"
  - **E** o dono da cafeteria clica no botão "Cadastrar Fornecedor"
  - **Então** o sistema deve registrar o fornecedor com as informações fornecidas
</details>

## Diagrama de Atividades do Sistema:

-SR1-
![diagrama-de-atividades](https://github.com/julsales/Coffee12/assets/143560144/fbee1388-6fe5-4414-8629-d1aa3cb31d91)

<br>

-SR2-
![Diagrama de atividade (2)](https://github.com/julsales/Coffee12/assets/142419446/abfcae11-b130-42cb-a513-3932332c97f0)

# BugTracker atualizado

![image](https://github.com/julsales/Coffee12/assets/142419446/4b7e10f2-798c-4f57-86aa-b697a844afd8)


# Programação em Pares
Durante o desenvolvimento do Coffee12, decidimos adotar o Pair Programming, uma prática ágil onde dois desenvolvedores trabalham juntos no mesmo código no mesmo computador, seja de forma síncrona, ou assíncrona, com o objetivo de melhorar a qualidade do código, tentar acelerar o desenvolvimento e tentar aprender com o outro.

De começo ficamos com o pé um pouco atrás preocupados com produtividade, mas depois de algum tempo juntos percebemos que a colaboração direta resultava em um código mais limpo, com menos erros e até ideias melhores às vezes.

Seguimos o modelo de "piloto" e "navegador", alternando papéis regularmente para ter a garantia de que ambos estavam participando ativamente.

A maior vantagem encontrada foi a redução na quantidade de bugs, como eram duas pessoas analisando o código, às vezes um via um erro que o outro não via, assim, ajudando na manutenção do código.

Nosso maior desafio foi manter a concentração era um pouco desafiador às vezes, afinal fazer código pode ser bem cansativo.

No fim das contas, o Pair Programming se provou um método eficiente de trabalho, melhorando a qualidade do código e até fortalecendo laços na equipe. Uma boa experiência de aprendizado.

[Docs do relato](https://docs.google.com/document/d/1kQpDnv8yoh_O1iIhTMe0Kr9lalcErUEXk4kpVVqKz8E/edit?usp=sharing)

# Telas Protótipo lo-fi

![Telas juntas](https://github.com/julsales/Coffee12/assets/133444972/0b58f532-cfb2-4aa4-b0ed-8207404af77f)

 

## Todas as Etapas que Fizemos até Agora Para o SR1
![Captura de tela 2024-05-13 114153](https://github.com/julsales/Coffee12/assets/152215002/7eba2202-37d5-4255-b85a-ae35ee4f9383)
![Captura de tela 2024-05-13 114022](https://github.com/julsales/Coffee12/assets/152215002/80d2057e-8c5c-497b-b725-d46982483985)
![Captura de tela 2024-05-13 114037](https://github.com/julsales/Coffee12/assets/152215002/ebd1b728-d87f-4169-b98e-7f5144d6c0c9)
![Captura de tela 2024-05-13 114204](https://github.com/julsales/Coffee12/assets/152215002/13b005c4-6d1d-4551-8217-90005ee44449)
