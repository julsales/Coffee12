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


## Links Importantes SR1

[Notion](https://distinct-rhubarb-0a9.notion.site/Notion-do-G12-3bfe1143afc6404eacf3dee57135c0dd?pvs=4)

[Google Sites](https://sites.google.com/cesar.school/queremoscafe-g12?usp=sharing)

[Google Drive](https://drive.google.com/drive/folders/1uxPJ6H_WYI4_X0wMdg2IrY-lmEsm_0Vb?usp=sharing)

[Diagrama de Atividades](https://lucid.app/lucidchart/972cf9c0-e0a0-48d4-ad8f-afb9259920fe/edit?beaconFlowId=7BD4ABDA3C7B83C2&invitationId=inv_3ca14424-7823-4e1f-a13d-d44c11858e4b&page=0_0)

[Protótipo De Baixa Fidelidade](https://lucid.app/lucidspark/826e0ab7-e4ec-4569-869a-10c4e6e42f82/edit?invitationId=inv_f55a1a31-7dd9-4893-a238-159cd9c78211&page=0_0#)

## ScreenCast's:

[Screencast Mockup de Baixa Fidelidade](https://youtu.be/ejQEUXkaveA)

[Screencast Implementação](https://youtu.be/7aSX_eD-i7M)

[Screencast Implementação Para o SR2](https://youtu.be/SWBmWlas7Jo)


## Deployment na Azure

https://cafedagente.azurewebsites.net

## Histórias do Usuário:

História 1: Requisitar itens esquecidos na cafeteria ( Implementada )
- Eu como usuário, gostaria de poder requisitar alguns itens que eu possa ter perdido no estabelecimento.
    - Descrição: O usuário envia uma requisição ao estabelecimento que pode responder se encontrou ou não o item do cliente.

Cenário 1: Usuário envia uma solicitação de item perdido<br>
    **Dado** que o usuário está na página de solicitação de itens perdidos<br>
    **Quando** o usuário insere a descrição do item "Guarda-chuva preto com cabo de madeira"<br>
    **E** o usuário clica no botão de enviar<br>
    **Então** o sistema deve salvar a solicitação<br>
    **E** o sistema deve exibir uma mensagem de confirmação "Sua solicitação foi enviada"<br>

  Cenário 2: Estabelecimento responde a uma solicitação de item perdido<br>
    **Dado** que o estabelecimento recebeu uma solicitação de item perdido<br>
    **Quando** o estabelecimento encontra o item descrito como "Guarda-chuva preto com cabo de madeira"<br>
    **E** o estabelecimento atualiza o status da solicitação para "Encontrado"<br>
    **Então** o usuário deve ser notificado de que seu item foi encontrado<br>

  Cenário 3: Estabelecimento responde negativamente a uma solicitação de item perdido<br>
    **Dado** que o estabelecimento recebeu uma solicitação de item perdido<br>
    **Quando** o estabelecimento não encontra o item descrito como "Guarda-chuva preto com cabo de madeira"<br>
    **E** o estabelecimento atualiza o status da solicitação para "Não Encontrado"<br>
    **Então** o usuário deve ser notificado de que seu item não foi encontrado<br>

História 2: Remoção de itens do cardápio ( Implementada )
- Eu como dono de cafeteria, gostaria de poder remover itens específicos do meu cardápio.
    - Descrição: O dono da cafeteria, poderia remover itens do cardápio, seja para altera-los ou para simplesmente retira-los do menu do estabelecimento.
      
Cenário 1: Dono de cafeteria remove um item do cardápio<br>
**Dado** que o dono da cafeteria está logado na plataforma administrativa<br>
**E** o dono acessa a página de gerenciamento do cardápio<br>
**Quando** o dono digita o nome do item "Café Espresso" para remoção<br>
**E** o dono confirma a remoção do item<br>
**Então** o sistema deve remover o item "Café Espresso" do cardápio<br>


História 3: Dar Feedbacks sobre Cafeterias Visitadas (Implementada)
- Eu como usuário gostaria de poder dar feedbacks referentes à cafeterias que visitei
    - Descrição: o usuário pode avaliar com notas de 1 a 5, juntamente de comentários, cafeterias das quais ele já foi frequentou.

Cenário 1: Usuário dá feedback sobre cafeteria visitada<br>
**Dado** que o usuário está logado na plataforma<br>
**E** o usuário está visualizando o perfil da cafeteria que visitou<br>
**Quando** o usuário clica no botão "Dar Feedback" no perfil da cafeteria<br>
**E** o usuário seleciona uma nota de avaliação de 0 a 5<br>
**E** o usuário escreve um comentário sobre sua experiência<br>
**E** o usuário confirma o envio do feedback<br>
**Então** o sistema deve registrar o feedback com a nota e o comentário fornecidos pelo usuário<br>

História 4: Evidenciar Pratos Principais e Promoções (Implementada)
- Eu como dono de cafeteria, gostaria de poder evidenciar os “pratos principais” e promoções do meu estabelecimento no perfil da minha cafeteria.
    - Descrição: o responsável pelo estabelecimento pode demonstrar os pratos principais e promoções de sua cafeteria em seu perfil. Exemplo:  “Promoção de Abril : MilkShake de Café R$ 18,00 por R$ 15,00 ; Tapioca de coco ralado R$ 15,50 por R$ 12,50 “

Cenário 1: Exibir prato principal sem promoção no perfil da cafeteria<br>
**Dado** que o dono da cafeteria está logado na plataforma<br>
**E** o dono da cafeteria cadastrou um prato principal chamado "Frango Grelhado"<br>
**E** o preço do "Frango Grelhado" é R$ 25,00 e não há promoção<br>
**Quando** o dono da cafeteria visualiza o perfil da cafeteria<br>
**Então** o sistema deve exibir o "Frango Grelhado" com o preço R$ 25,00 sem indicar promoção<br>

Cenário 2: Exibir prato principal com promoção no perfil da cafeteria<br>
**Dado que o dono da cafeteria está logado na plataforma<br>
**E** o dono da cafeteria cadastrou um prato principal chamado "Milkshake de Morango"<br>
**E** o preço do "Milkshake de Morango" é R$ 15,00 e há uma promoção de R$ 12,00<br>
**Quando** o dono da cafeteria visualiza o perfil da cafeteria<br>
**Então** o sistema deve exibir o "Milkshake de Morango" com o preço cortado de R$ 15,00 e o preço promocional de R$ 12,00 ao lado



História 5: Cadastrar Perfil da Cafeteria (Implementada)
- Eu como dono de cafeteria, gostaria de cadastrar o perfil da minha cafeteria na plataforma, juntamente de seu nome, endereço e horários de funcionamento.
    - Descrição: O dono da cafeteria poderá ter um perfil da cafeteria para registrar  endereço do estabelecimento, nome do estabelecimento, telefone.

Cenário: Cadastrar perfil da cafeteria na plataforma<br>
**Dado** que o dono da cafeteria está logado na plataforma como usuário<br>
**E** não possui uma cafeteria cadastrada no sistema<br>
**Quando** o dono da cafeteria acessa a página de cadastro do perfil da cafeteria<br>
**E** o dono da cafeteria preenche o campo "Nome do Estabelecimento" com "Café da Esquina"<br>
**E** o dono da cafeteria preenche o campo "Endereço" com "Rua das Flores, 123"<br>
**E** o dono da cafeteria preenche o campo "Telefone" com "(XX) XXXX-XXXX"<br>
**E** o dono da cafeteria clica no botão de cadastrar perfil<br>
**Então** o sistema deve registrar o perfil da cafeteria com o nome "Café da Esquina", endereço "Rua das Flores, 123" e telefone "(XX) XXXX-XXXX"

  
História 6: Editar Perfil da Cafeteria e Adicionar Cardápio (Implementada)
- Eu como dono de cafeteria, gostaria de poder editar o perfil da minha cafeteria na plataforma e registrar os itens disponíveis no cardápio
    - Descrição: O dono da cafeteria poderá editar o perfil da cafeteria para adicionar o cardápio e editar endereço do estabelecimento, nome, telefone.



Cenário: Editar perfil da cafeteria na plataforma<br>
**Dado** que o dono da cafeteria está logado na plataforma como usuário<br>
**E** o dono da cafeteria possui um perfil cadastrado com o nome "Café da Esquina", endereço "Rua das Flores, 123" e telefone "(XX) XXXX-XXXX"<br>
**Quando**o dono da cafeteria acessa a página de edição do perfil da cafeteria<br>
**E** o dono da cafeteria edita o campo "Nome do Estabelecimento" para "Café do Bairro"<br>
**E** o dono da cafeteria edita o campo "Endereço" para "Avenida Principal, 456"<br>
**E** o dono da cafeteria edita o campo "Telefone" para "(YY) YYYY-YYYY"<br>
**E** o dono da cafeteria clica no botão de salvar alterações<br>
**Então** o sistema deve atualizar o perfil da cafeteria com o nome "Café do Bairro", endereço "Avenida Principal, 456" e telefone "(YY) YYYY-YYYY"

História 7: Reserva de Mesas Online (Implementada)
- Eu como usuário, gostaria de poder reservar mesas em cafeterias diretamente pela plataforma.
    - Descrição: Os usuários poderão verificar a disponibilidade e fazer reservas de mesas em suas cafeterias favoritas através da plataforma, evitando filas e garantindo um lugar.

Cenário 1: Usuário envia solicitação de reserva de mesa<br>
**Dado** que o usuário está na página de reserva de mesa da cafeteria desejada<br>
**Quando** o usuário seleciona a data, horário e quantidade de pessoas desejados para a reserva<br>
**E** o usuário clica no botão "Enviar Reserva"<br>
**Então** o sistema registra a solicitação de reserva do usuário<br>

Cenário 2: Dono do estabelecimento visualiza e confirma reserva de mesa<br>
**Dado** que o dono da cafeteria está na página de gerenciamento de reservas<br>
**Quando** o dono visualiza a lista de solicitações de reserva de mesas pendentes<br>
**E** encontra uma solicitação para a data e horário desejados<br>
**Então** o dono verifica a disponibilidade de mesas para a quantidade de pessoas informada na solicitação<br>
**E** se houver mesas disponíveis para a quantidade de pessoas especificada na reserva<br>
**Então** o dono confirma a reserva e exibe uma mensagem de confirmação ao usuário<br>


Cenário 3: Dono do estabelecimento não encontra mesas disponíveis<br>
**Dado** que o dono da cafeteria está na página de gerenciamento de reservas<br>
**Quando** o dono visualiza a lista de solicitações de reserva de mesas pendentes<br>
**E** encontra uma solicitação para a data e horário desejados<br>
**E** verifica que não há mesas disponíveis para a quantidade de pessoas informada na solicitação<br>
**Então** o dono informa ao usuário que não há mesas disponíveis para a data e horário especificados<br>

 
História 8: Adicionae Cafeterias aos Favoritos (Implementada)
- Eu como usuário, gostaria adicionar cafeterias aos favoritos para que elas estajam de mais fácil acesso ao visitar a página principal.
    - Descrição: Os perfis das cafeterias poderão ser adicionadas aos favoritos e estarão disponíveis em uma aba dedicada às cafeterias favoritas na página principal.
Cenário 1: Usuário adiciona cafeteria aos favoritos<br>
**Dado** que o usuário está visualizando o perfil de uma cafeteria<br>
**Quando** o usuário clica no botão "Adicionar aos Favoritos"<br>
**Então** o sistema adiciona a cafeteria aos favoritos do usuário<br>
 
História 9: Visualizar feedbacks (Implementada)
- Eu como dono de cafeteria, gostaria de poder visualizar os feedbacks direcionados ao meu estabelecimento.
    - Descrição: o responsável pelo estabelecimento pode acessar e visualizar os feedbacks recebidos, possibilitando a análise de comentários, críticas e sugestões dos clientes para melhorar a qualidade do serviço e produtos    oferecidos. Exemplo: "Feedback de Junho: 'Excelente atendimento e ambiente acolhedor, porém a tapioca estava um pouco seca' - João Silva; 'Adorei o novo milkshake de café, voltarei mais vezes!' - Maria Oliveira".

Cenário 1: Dono de cafeteria visualiza feedbacks recebidos<br>
**Dado** que o dono de cafeteria está logado na plataforma<br>
**Quando** o dono acessa a seção de feedbacks do seu estabelecimento<br>
**Então** o sistema exibe uma lista dos feedbacks recebidos, incluindo comentários, notas e nomes dos clientes<br>
**E** o dono pode visualizar detalhes de cada feedback para análise<br>
 
História 10: Histórico de Visitas (Implementada)
- Eu como usuário, gostaria de ver um histórico das cafeterias que visitei através da plataforma.
    - Descrição: O sistema manterá um registro das visitas anteriores dos usuários às cafeterias, permitindo que revisitem facilmente.

Cenário 1: Usuário visualiza histórico de visitas<br>
**Dado** que o usuário está logado na plataforma<br>
**Quando** o usuário acessa a seção de histórico de visitas<br>
**Então** o sistema exibe uma lista das cafeterias previamente visitadas pelo usuário, ordenadas por data da visita mais recente<br>
 




## Diagrama de Atividades do Sistema:


![diagrama-de-atividades](https://github.com/julsales/Coffee12/assets/143560144/fbee1388-6fe5-4414-8629-d1aa3cb31d91)



# BugTracker
![image](https://github.com/julsales/Coffee12/assets/134211506/abe919d3-0ded-468b-a0a6-e37f24922257)


# Programação em Pares
Durante o desenvolvimento do Coffee12, decidimos adotar o Pair Programming, uma prática ágil onde dois desenvolvedores trabalham juntos no mesmo código no mesmo computador, seja de forma síncrona, ou assíncrona, com o objetivo de melhorar a qualidade do código, tentar acelerar o desenvolvimento e tentar aprender com o outro.

De começo ficamos com o pé um pouco atrás preocupados com produtividade, mas depois de algum tempo juntos percebemos que a colaboração direta resultava em um código mais limpo, com menos erros e até ideias melhores às vezes.

Seguimos o modelo de "piloto" e "navegador", alternando papéis regularmente para ter a garantia de que ambos estavam participando ativamente.

A maior vantagem encontrada foi a redução na quantidade de bugs, como eram duas pessoas analisando o código, às vezes um via um erro que o outro não via, assim, ajudando na manutenção do código.

Nosso maior desafio foi manter a concentração era um pouco desafiador às vezes, afinal fazer código pode ser bem cansativo.

No fim das contas, o Pair Programming se provou um método eficiente de trabalho, melhorando a qualidade do código e até fortalecendo laços na equipe. Uma boa experiência de aprendizado.

# Telas Protótipo lo-fi

![Telas juntas](https://github.com/julsales/Coffee12/assets/133444972/0b58f532-cfb2-4aa4-b0ed-8207404af77f)


  

## Todas as Etapas que Fizemos até Agora Para o SR1
![Captura de tela 2024-05-13 114153](https://github.com/julsales/Coffee12/assets/152215002/7eba2202-37d5-4255-b85a-ae35ee4f9383)
![Captura de tela 2024-05-13 114022](https://github.com/julsales/Coffee12/assets/152215002/80d2057e-8c5c-497b-b725-d46982483985)
![Captura de tela 2024-05-13 114037](https://github.com/julsales/Coffee12/assets/152215002/ebd1b728-d87f-4169-b98e-7f5144d6c0c9)
![Captura de tela 2024-05-13 114204](https://github.com/julsales/Coffee12/assets/152215002/13b005c4-6d1d-4551-8217-90005ee44449)
