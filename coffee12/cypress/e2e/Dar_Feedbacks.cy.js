describe('Dar feedback', () => {
    it('Dar feedback a uma cafeteria', () => {
        cy.visit('/')
        cy.get('.button').click()
        cy.get('#username').type('123')
        cy.get('#password').type('123')
        cy.get('button').click()
        cy.get('.cafe > a').click()
        cy.get('a.btn').should('be.visible').click()
        cy.get('#id_rating').type('5')
        cy.get('#id_comment').type('Muito bom amei')
        cy.get('button').click()
        })

})