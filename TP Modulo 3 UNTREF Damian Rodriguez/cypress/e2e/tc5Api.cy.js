// #Este codigo es de Damian Rodriguez
// Caso 2 hacer un get a berry/2
it('TC5Api- Verifica propiedades de berry/2 en relación a berry/1', () => {
    let berry1, berry2

    cy.request('https://pokeapi.co/api/v2/berry/1').then(res1 => {
      berry1 = res1.body

      cy.request('https://pokeapi.co/api/v2/berry/2').then(res2 => {
        berry2 = res2.body

        expect(berry2.firmness.name).to.eq('super-hard')
        expect(berry2.size).to.be.greaterThan(berry1.size)
        expect(berry2.soil_dryness).to.eq(berry1.soil_dryness)
      })
    })
  })