describe('Reservar mesas', () => {
    it('Reservando mesas', () => {
        cy.visit('/')
        cy.get('.button').click()
        cy.get('#username').type('123')
        cy.get('#password').type('123')
        cy.get('button').click()
        cy.get('.cafe > a').click()
        cy.get('[method="GET"] > .btn').click()
        cy.get('#id_data_hora').type("2024-07-19T16:00")
        cy.get('#id_numero_pessoas').type('6')
        cy.get('button').click()
        cy.get('.reserva-content > :nth-child(3)').should('contain',"Número de pessoas: 6")
        cy.get('.update-button').click()
        cy.get('#id_data_hora').clear()
        cy.get('#id_numero_pessoas').clear()
        cy.get('#id_data_hora').type("2024-07-19T16:00")
        cy.get('#id_numero_pessoas').type('7')
        cy.get('button').click()
        cy.get('.reserva-content > :nth-child(3)').should('contain',"Número de pessoas: 7")
        })
    it('Checagem da cafeteria', () => {
        cy.visit('/')
        cy.get('.button').click()
        cy.get('#username').type('cafe3')
        cy.get('#password').type('cafe3')
        cy.get('button').click()
        cy.get('[href="/reservas/listar/"]').click()
        cy.get('h2').should('contain',"123")
        cy.get('.reserva-content > :nth-child(3)').should('contain',"Número de pessoas: 7")
        cy.get('.update-button').click()
        })    
    it('Cancelando a reserva', () => {
        cy.visit('/')
        cy.get('.button').click()
        cy.get('#username').type('123')
        cy.get('#password').type('123')
        cy.get('button').click()
        cy.get('[href="/reservas/"]').click()
        cy.get('.cancel-button').click()
        })
})