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

[Screencast Mockup](https://youtu.be/ejQEUXkaveA)

[Screencast Implementação](https://youtu.be/7aSX_eD-i7M)


## Deployment na Azure

https://cafedagente.azurewebsites.net

## Histórias do Usuário:

História 1: Personalização de Recomendações de Cafeterias
- Eu como usuário, gostaria de escolher quais características de café me agradam mais e ter recomendações de cafeterias, baseado no meu perfil.
    - Descrição: Será feito perguntas como:
        - Quantas pessoas vão participar?
        - Qual é o objetivo?
         Ex: Usuário poderá escolher entre: encontro de amigos, momento de trabalho, momento de descanso, encontrar algo novo…
        - Onde a(s) pessoa(s) moram aproximadamente (bairros)
        - Que tipo de cardápio você prefere
        Ex: (Vou pelo café, vou pela comida, não importa…)
        - Tem algo que você não gosta?
        Ex: Ambientes barulhentos, ambientes coloridos demais.
          - Descrição: o sistema ira informar novas cafeterias com base nas preferencias que eu escolher para minha conta
            - Perguntas: 
            1: qual o tipo de café você mais gosta
            2: com qual finalidade você procura cafeterias?
            3: qual região você prefere?

História 2: Seguir Perfis e Acompanhar Novidades
- Eu como usuário, gostaria de seguir perfis e poder acompanhar as novidades dele e das minhas cafeterias favoritas.
    - Descrição: O usuário poderia ter acesso a uma aba onde tem ofertas, promoções ou eventos sendo promovidos em cafeterias seguidas.

História 3: Dar Feedbacks sobre Cafeterias Visitadas (Implementada)
- Eu como usuário gostaria de poder dar feedbacks referentes à cafeterias que visitei
    - Descrição: o usuário pode avaliar com notas de 1 a 5, juntamente de comentários, cafeterias das quais ele já foi frequentou.

História 4: Evidenciar Pratos Principais e Promoções (Implementada)
- Eu como dono de cafeteria, gostaria de poder evidenciar os “pratos principais” e promoções do meu estabelecimento no perfil da minha cafeteria.
    - Descrição: o responsável pelo estabelecimento pode demonstrar os pratos principais e promoções de sua cafeteria em seu perfil. Exemplo:  “Promoção de Abril : MilkShake de Café R$ 18,00 por R$ 15,00 ; Tapioca de coco ralado R$ 15,50 por R$ 12,50 “



História 5: Cadastrar Perfil da Cafeteria (Implementada)
- Eu como dono de cafeteria, gostaria de cadastrar o perfil da minha cafeteria na plataforma, juntamente de seu nome, endereço e horários de funcionamento.
    - Descrição: O dono da cafeteria poderá ter um perfil da cafeteria para registrar  endereço do estabelecimento, nome do estabelecimento, telefone.

  
História 6: Editar Perfil da Cafeteria e Adicionar Cardápio (Implementada)
- Eu como dono de cafeteria, gostaria de poder editar o perfil da minha cafeteria na plataforma e registrar os itens disponíveis no cardápio
    - Descrição: O dono da cafeteria poderá editar o perfil da cafeteria para adicionar o cardápio e editar endereço do estabelecimento, nome, telefone.

História 7: Reserva de Mesas Online
- Eu como usuário, gostaria de poder reservar mesas em cafeterias diretamente pela plataforma.
    - Descrição: Os usuários poderão verificar a disponibilidade e fazer reservas de mesas em suas cafeterias favoritas através da plataforma, evitando filas e garantindo um lugar.
 
História 8: Adicionae Cafeterias aos Favoritos (Implementada)
- Eu como usuário, gostaria adicionar cafeterias aos favoritos para que elas estajam de mais fácil acesso ao visitar a página principal.
    - Descrição: Os perfis das cafeterias poderão ser adicionadas aos favoritos e estarão disponíveis em uma aba dedicada às cafeterias favoritas na página principal.
 
História 9: Visualizar feedbacks (Implementada)
- Eu como dono de cafeteria, gostaria de poder visualizar os feedbacks direcionados ao meu estabelecimento.
    - Descrição: o responsável pelo estabelecimento pode acessar e visualizar os feedbacks recebidos, possibilitando a análise de comentários, críticas e sugestões dos clientes para melhorar a qualidade do serviço e produtos    oferecidos. Exemplo: "Feedback de Junho: 'Excelente atendimento e ambiente acolhedor, porém a tapioca estava um pouco seca' - João Silva; 'Adorei o novo milkshake de café, voltarei mais vezes!' - Maria Oliveira".
 
História 10: Histórico de Visitas (Implementada)
- Eu como usuário, gostaria de ver um histórico das cafeterias que visitei através da plataforma.
    - Descrição: O sistema manterá um registro das visitas anteriores dos usuários às cafeterias, permitindo que revisitem facilmente.
 



## cenario de aceitação BDD (gherkin):

Historia 1: 
-Funcionalidade: Recomendações de Cafeterias
-Como um usuário
    Eu quero escolher características de cafés que me agradam
    Para receber recomendações de cafeterias baseadas no meu perfil
<b>
  -Cenário: Receber recomendações com base nas preferências
    Dado que estou na página de preferências
    Quando eu seleciono "momento de trabalho" como finalidade
    E escolho "vou pelo café" como tipo de cardápio
    E informo que prefiro "ambientes tranquilos"
    E escolho "Pinheiros" como região preferida
    E submeto minhas preferências
    Então eu recebo uma lista de cafeterias recomendadas em Pinheiros que são tranquilas e focadas em café
<b>
<b>
Historia 2: 
-Funcionalidade: Seguir Perfis e Acompanhar Novidades
  -Como um usuário
      Eu quero seguir perfis e acompanhar novidades
      Para estar atualizado com eventos e promoções das minhas cafeterias favoritas
<b>
  -Cenário: Seguir uma cafeteria e receber atualizações
      Dado que estou na página de perfil da cafeteria "Café do Bairro" 
      Quando eu clico em "Seguir"
      E volto para a aba de novidades
      Então eu vejo ofertas e eventos do "Café do Bairro" listados nas novidades
<b>
<b>

Historia 3: 
-Funcionalidade: Dar Feedback sobre Cafeterias
  -Como um usuário
      Eu quero dar feedback sobre as cafeterias que visitei
      Para informar outros usuários sobre minha experiência
<b>
  -Cenário: Avaliar uma cafeteria
      Dado que visitei a cafeteria "Café do Bairro"
      E estou na página de feedback
      Quando eu dou uma nota de "4 estrelas"
      E escrevo um comentário "Ótimo ambiente e café excelente"
      E submeto meu feedback
      Então meu comentário e nota são salvos no perfil da "Café do Bairro" 
<b>
<b>

Historia 4: 
-Funcionalidade: Destacar Promoções no Perfil da Cafeteria
  -Como dono de uma cafeteria
      Eu quero evidenciar pratos principais e promoções
      Para atrair mais clientes
<b>
-Cenário: Adicionar uma promoção ao perfil
      Dado que estou logado como o dono da "Café do Bairro"
      E estou na página de edição do perfil
      Quando eu adiciono a promoção "Milkshake de Café por R$ 15,00"
      E submeto as alterações
      Então a promoção "Milkshake de Café por R$ 15,00" é exibida no perfil da minha cafeteria
<b>
<b>

Historia 5: 
-Funcionalidade: Cadastro de Perfil da Cafeteria
  -Como dono de uma cafeteria
      Eu quero cadastrar o perfil da minha cafeteria
      Para que clientes possam encontrar informações sobre meu estabelecimento
<b>
  -Cenário: Cadastrar nova cafeteria
      Dado que estou logado como dono de uma cafeteria
      Quando eu preencho o formulário de cadastro com o nome "Café Novo", endereço "123 Rua das Flores, Pinheiros, SP" e horário "8h às 18h"
      E submeto o cadastro
      Então o perfil do "Café Novo" é criado e visível para os usuários
<b>
<b>
Historia 6: 
-Funcionalidade: Editar Perfil da Cafeteria
  -Como dono de uma cafeteria
     Eu quero editar o perfil da minha cafeteria
     Para atualizar informações e o cardápio
     <b>
   -Cenário: Editar informações do perfil
     Dado que estou logado como o dono da "Café do Bairro"
     E estou na página de edição do perfil
<b>
<b>
## Diagrama de Atividades do Sistema:


![diagrama-de-atividades](https://github.com/julsales/Coffee12/assets/143560144/fbee1388-6fe5-4414-8629-d1aa3cb31d91)



# BugTracker
![image](https://github.com/julsales/Coffee12/assets/134211506/287ea9dc-aeb2-471c-bfdb-c169a8d9a5c2)

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
