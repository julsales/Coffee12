describe('Receber Feedbacks', () => {
    it('Dar feedback a uma cafeteria', () => {
        cy.visit('/');
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
    it('Receber feedback', () => {
        cy.visit('/');
        cy.get('.button').click()
        cy.get('#username').type('cafe3')
        cy.get('#password').type('cafe3')
        cy.get('button').click()
        cy.get('[href="/cafeteria/15/feedbacks/"]').click()
        cy.get('.feedback-container > :nth-child(2) > :nth-child(1)').should('contain',"Usuário: 123")
        cy.get('.feedback-container > :nth-child(2) > :nth-child(2)').should('contain',"Avaliação: 5")
        cy.get('.feedback-container > :nth-child(2) > :nth-child(3)').should('contain',"Comentário: Muito bom amei")
        })
})