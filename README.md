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

12. Adriano Barnard → abmp@cesar.school

## Links Importantes SR1

[Notion](https://distinct-rhubarb-0a9.notion.site/Notion-do-G12-3bfe1143afc6404eacf3dee57135c0dd?pvs=4)

[Google Sites](https://sites.google.com/cesar.school/queremoscafe-g12?usp=sharing)

[Google Drive](https://drive.google.com/drive/folders/1uxPJ6H_WYI4_X0wMdg2IrY-lmEsm_0Vb?usp=sharing)

[Diagrama de Atividades](https://lucid.app/lucidchart/972cf9c0-e0a0-48d4-ad8f-afb9259920fe/edit?beaconFlowId=7BD4ABDA3C7B83C2&invitationId=inv_3ca14424-7823-4e1f-a13d-d44c11858e4b&page=0_0)

[Protótipo De Baixa Fidelidade](https://lucid.app/lucidspark/826e0ab7-e4ec-4569-869a-10c4e6e42f82/edit?invitationId=inv_f55a1a31-7dd9-4893-a238-159cd9c78211&page=0_0#)


## Histórias do Usuário:

História 1: 
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

História 2:
- Eu como usuário, gostaria de seguir perfis e poder acompanhar as novidades dele e das minhas cafeterias favoritas.
    - Descrição: O usuário poderia ter acesso a uma aba onde tem ofertas, promoções ou eventos sendo promovidos em cafeterias seguidas.

História 3:
- Eu como usuário gostaria de poder dar feedbacks referentes à cafeterias que visitei
    - Descrição: o usuário pode avaliar com notas de 1 a 5, juntamente de comentários, cafeterias das quais ele já foi frequentou.

História 4:
- Eu como dono de cafeteria, gostaria de poder evidenciar os “pratos principais” e promoções do meu estabelecimento no perfil da minha cafeteria.
    - Descrição: o responsável pelo estabelecimento pode demonstrar os pratos principais e promoções de sua cafeteria em seu perfil. Exemplo:  “Promoção de Abril : MilkShake de Café R$ 18,00 por R$ 15,00 ; Tapioca de coco ralado R$ 15,50 por R$ 12,50 “

História 5:
- Eu como dono de cafeteria, gostaria de cadastrar o perfil da minha cafeteria na plataforma, juntamente de seu nome, endereço e horários de funcionamento.
    - Descrição: O dono da cafeteria poderá ter um perfil da cafeteria para registrar  horarios de funcionamento, endereço do estabelecimento, nome do estabelecimento.
      
História 6:
- Eu como dono de cafeteria, gostaria de poder editar o perfil da minha cafeteria na plataforma e registrar os itens disponíveis no cardápio
    - Descrição: O dono da cafeteria poderá editar o perfil da cafeteria para adicionar o cardápio e editar horários de funcionamento, endereço do estabelecimento.

## Diagrama de Atividades do Sistema:


![diagrama-de-atividades](https://github.com/julsales/Coffee12/assets/143560144/fbee1388-6fe5-4414-8629-d1aa3cb31d91)


## cenario de aceitação BDD (gherkin):

#Historia 1: 
-Funcionalidade: Recomendações de Cafeterias
-Como um usuário
    Eu quero escolher características de cafés que me agradam
    Para receber recomendações de cafeterias baseadas no meu perfil

  -Cenário: Receber recomendações com base nas preferências
    Dado que estou na página de preferências
    Quando eu seleciono "momento de trabalho" como finalidade
    E escolho "vou pelo café" como tipo de cardápio
    E informo que prefiro "ambientes tranquilos"
    E escolho "Pinheiros" como região preferida
    E submeto minhas preferências
    Então eu recebo uma lista de cafeterias recomendadas em Pinheiros que são tranquilas e focadas em café


#Historia 2: 
-Funcionalidade: Seguir Perfis e Acompanhar Novidades
  -Como um usuário
      Eu quero seguir perfis e acompanhar novidades
      Para estar atualizado com eventos e promoções das minhas cafeterias favoritas

  -Cenário: Seguir uma cafeteria e receber atualizações
      Dado que estou na página de perfil da cafeteria "Café do Bairro" 
      Quando eu clico em "Seguir"
      E volto para a aba de novidades
      Então eu vejo ofertas e eventos do "Café do Bairro" listados nas novidades


#Historia 3: 
-Funcionalidade: Dar Feedback sobre Cafeterias
  -Como um usuário
      Eu quero dar feedback sobre as cafeterias que visitei
      Para informar outros usuários sobre minha experiência

  -Cenário: Avaliar uma cafeteria
      Dado que visitei a cafeteria "Café do Bairro"
      E estou na página de feedback
      Quando eu dou uma nota de "4 estrelas"
      E escrevo um comentário "Ótimo ambiente e café excelente"
      E submeto meu feedback
      Então meu comentário e nota são salvos no perfil da "Café do Bairro" 


#Historia 4: 
-Funcionalidade: Destacar Promoções no Perfil da Cafeteria
  -Como dono de uma cafeteria
      Eu quero evidenciar pratos principais e promoções
      Para atrair mais clientes

-Cenário: Adicionar uma promoção ao perfil
      Dado que estou logado como o dono da "Café do Bairro"
      E estou na página de edição do perfil
      Quando eu adiciono a promoção "Milkshake de Café por R$ 15,00"
      E submeto as alterações
      Então a promoção "Milkshake de Café por R$ 15,00" é exibida no perfil da minha cafeteria


#Historia 5: 
-Funcionalidade: Cadastro de Perfil da Cafeteria
  -Como dono de uma cafeteria
      Eu quero cadastrar o perfil da minha cafeteria
      Para que clientes possam encontrar informações sobre meu estabelecimento

  -Cenário: Cadastrar nova cafeteria
      Dado que estou logado como dono de uma cafeteria
      Quando eu preencho o formulário de cadastro com o nome "Café Novo", endereço "123 Rua das Flores, Pinheiros, SP" e horário "8h às 18h"
      E submeto o cadastro
      Então o perfil do "Café Novo" é criado e visível para os usuários


#Historia 6: 
-Funcionalidade: Editar Perfil da Cafeteria
  -Como dono de uma cafeteria
     Eu quero editar o perfil da minha cafeteria
     Para atualizar informações e o cardápio

  -Cenário: Editar informações do perfil
     Dado que estou logado como o dono da "Café do Bairro"
     E estou na página de edição do perfil


