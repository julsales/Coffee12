describe('Itens perdidos', () => {
    
    it('Requisitar itens perdidos', () => {
        cy.visit('/');
        cy.get('.button').click()
        cy.get('#username').type('123')
        cy.get('#password').type('123')
        cy.get('button').click()
        cy.get('.cafe > a').click()
        cy.get('[action="/add_to_historico/15/"] > .btn').click()
        cy.get('[href="/historico/"]').click()
        cy.get('.solicitar-button').click()
        cy.get('#descricao').type('Oculos de sol preto')
        cy.get('button').click()
        cy.get('.remove-button').click({ multiple: true })
        cy.get('[href="/minhas_requisicoes/"]').click()
        cy.get('tbody > :nth-child(1)').should('contain', "Oculos de sol preto")
        })
    it('Checagem da cafeteria', () => {
        cy.visit('/');
        cy.get('.button').click()
        cy.get('#username').type('cafe3')
        cy.get('#password').type('cafe3')
        cy.get('button').click()
        cy.get('[href="/solicita%C3%A7%C3%B5es/"]').click()
        cy.get('tbody > tr > :nth-child(1)').should('contain', "Oculos de sol preto")
        cy.get('[action^="/marcar_item_achado/"] > button').click();
        })
    it('Checar se o item foi achado', () => {
        cy.visit('/');
        cy.get('.button').click()
        cy.get('#username').type('123')
        cy.get('#password').type('123')
        cy.get('button').click()
        cy.get('[href="/minhas_requisicoes/"]').click()
        cy.get('tbody > tr > :nth-child(2)').should('contain', "achado")
        }) 
    it('Apagar item requisitado', () => {
        cy.visit('/');
        cy.get('.button').click()
        cy.get('#username').type('cafe3')
        cy.get('#password').type('cafe3')
        cy.get('button').click()
        cy.get('[href="/solicita%C3%A7%C3%B5es/"]').click()
        cy.get('tbody > tr > :nth-child(1)').should('contain', "Oculos de sol preto")
        cy.get('[action^="/remover_requisicao/"] > button').click({ multiple: true })
        cy.get('p').should('contain', "Nenhuma solicitação encontrada.")
        })
})