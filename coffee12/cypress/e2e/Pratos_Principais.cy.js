describe('Evidenciar pratos principais', () => {
    it('Adicionar item ao cardápio', () => {
        cy.visit('/');
        cy.get('.button').click()
        cy.get('#username').type('cafe3')
        cy.get('#password').type('cafe3')
        cy.get('button').click()
        cy.get('[href="/cadastrarPrato/"]').click()
        cy.get('#nome').type("Café Gelado")
        cy.get('#descricao').type("Café bem gelado")
        cy.get('#preco').type("12")
        cy.get('#preco_promocional').type("11")
        cy.get('#prato_principal').click()
        cy.get('button').click()
        cy.get('h3').should('contain',"Café Gelado")
        })
    it('Verificar pratos principais', () => {
        cy.visit('/')
        cy.get('.button').click()
        cy.get('#username').type('123')
        cy.get('#password').type('123')
        cy.get('button').click()
        cy.get('h3').should('contain',"Pratos Principais")
        cy.get('ul > :nth-child(1)').should('contain',"Café Gelado - R$12.00")
        })
    it('Apagando item', () => {
        cy.visit('/');
        cy.get('.button').click()
        cy.get('#username').type('cafe3')
        cy.get('#password').type('cafe3')
        cy.get('button').click()
        cy.get('[href="/excluirPrato/"]').click()
        cy.get('#nome').type("Café Gelado")
        cy.get('button').click()
        })
})