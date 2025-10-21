describe('Pruebas PokeAPI', () => {
  it('Debe obtener un Pokémon por ID', () => {
    cy.request('https://pokeapi.co/api/v2/pokemon/1')
      .should((response) => {
        expect(response.status).to.eq(200);
        expect(response.body.name).to.eq('bulbasaur');
      });
  });
});
