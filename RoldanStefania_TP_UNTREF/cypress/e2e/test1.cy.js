import 'cypress-mochawesome-reporter/register';
describe('Caso 1 - Berry API', () => {
  it('Verifica los datos de la Berry 1', () => {
    // Hacemos un GET a la API
    cy.request('https://pokeapi.co/api/v2/berry/1').then((response) => {
      // Verificamos que el status sea 200
      expect(response.status).to.eq(200);

      const berry = response.body;

      // Verificamos el size
      expect(berry.size).to.eq(20);

      // Verificamos el soil_dryness
      expect(berry.soil_dryness).to.eq(15);

      // Verificamos que el name de firmness sea "soft"
      expect(berry.firmness.name).to.eq('soft');
    });
  });
});
