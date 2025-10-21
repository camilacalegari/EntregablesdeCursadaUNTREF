import 'cypress-mochawesome-reporter/register';
describe('Caso 3 - Pokémon Pikachu', () => {
  it('Verifica los datos de Pikachu', () => {
    cy.request('https://pokeapi.co/api/v2/pokemon/pikachu/').then((response) => {
      const pikachu = response.body;

      // Verificamos que el status sea 200
      expect(response.status).to.eq(200);

      // Verificamos que la experiencia base esté entre 10 y 1000
      expect(pikachu.base_experience).to.be.greaterThan(10);
      expect(pikachu.base_experience).to.be.lessThan(1000);

      // Verificamos que uno de los tipos sea 'electric'
      const tipos = pikachu.types.map(t => t.type.name);
      expect(tipos).to.include('electric');
    });
  });
});
