describe('Pruebas API - PokeAPI', () => {

  let berry1, berry2

  it('Caso 1 - Berry 1', () => {
    cy.request('https://pokeapi.co/api/v2/berry/1').then((response) => {
      expect(response.status).to.eq(200)

      berry1 = response.body

      expect(berry1.size).to.eq(20)
      expect(berry1.soil_dryness).to.eq(15)
      expect(berry1.firmness.name).to.eq('soft')
    })
  })

  it('Caso 2 - Berry 2', () => {
    cy.request('https://pokeapi.co/api/v2/berry/2').then((response) => {
      expect(response.status).to.eq(200)

      berry2 = response.body

      expect(berry2.firmness.name).to.eq('super-hard')
      expect(berry2.size).to.be.greaterThan(berry1.size)
      expect(berry2.soil_dryness).to.eq(berry1.soil_dryness)
    })
  })

  it('Caso 3 - Pikachu', () => {
    cy.request('https://pokeapi.co/api/v2/pokemon/pikachu').then((response) => {
      expect(response.status).to.eq(200)

      const pikachu = response.body

      expect(pikachu.base_experience).to.be.greaterThan(10)
      expect(pikachu.base_experience).to.be.lessThan(1000)
      expect(pikachu.types[0].type.name).to.eq('electric')

    })
  })

})
