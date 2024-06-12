describe('Adicionar cafeteria aos favoritos', () => {
    
    it('Adicionando aos favoritos', () => {
        cy.visit('/');
        cy.get('.button').click()
        cy.get('#username').type('123')
        cy.get('#password').type('123')
        cy.get('button').click()
        cy.get('.btn').click()
        cy.get('[href="/favoritos/"]').click()
        cy.get('h2').should('contain',"São Braz Recife")
        cy.get('form > .btn').click()
        })
})