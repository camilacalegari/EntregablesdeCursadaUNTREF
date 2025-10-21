// #Este codigo es de Damian Rodriguez
// Caso 1 Hacer un get a berry/1
it('TC4Api - Verificar propiedades de berry/1', () => {
    cy.request('https://pokeapi.co/api/v2/berry/1').then((response) => {
      expect(response.body.size).to.eq(20)
      expect(response.body.soil_dryness).to.eq(15)
      expect(response.body.firmness.name).to.eq('soft')
    })
  })