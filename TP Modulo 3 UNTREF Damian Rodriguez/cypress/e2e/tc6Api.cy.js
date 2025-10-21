// #Este codigo es de Damian Rodriguez
// caso3 Hacer un get a pikachu (https://pokeapi.co/api/v2/pokemon/pikachu/)

it('TC6Api - Verifica experiencia y tipo de Pikachu', () => {
    cy.request('https://pokeapi.co/api/v2/pokemon/pikachu').then((response) => {
      expect(response.body.base_experience).to.be.within(11, 999)
      const tipos = response.body.types.map(t => t.type.name)
      expect(tipos).to.include('electric')
    })
  })