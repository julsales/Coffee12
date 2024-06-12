describe('Excluir item do cardápio', () => {  
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
        cy.get('button').click()
        cy.get('h3').should('contain',"Café Gelado")
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