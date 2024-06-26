describe('Ver o histórico de cafeterias visitadas', () => {
    it('Historico de cafeterias', () => {
        cy.visit('/')
        cy.get('.button').click()
        cy.get('#username').type('123')
        cy.get('#password').type('123')
        cy.get('button').click()
        cy.get('.cafe > a').click()
        cy.get('[action^="/add_to_historico"] > .btn').should('be.visible').click()
        cy.get('[href="/historico/"]').click()
        cy.get('h2').should('contain', "São Braz Recife")
        cy.get('.remove-button').click({ multiple: true })
        })
})