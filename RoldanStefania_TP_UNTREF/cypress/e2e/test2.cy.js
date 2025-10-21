import 'cypress-mochawesome-reporter/register';
describe('Caso 2 - Berry API', () => {
  it('Verifica los datos de la Berry 2 en comparación con Berry 1', () => {
    let sizeBerry1;
    let soilDrynessBerry1;

    // Primero obtenemos Berry 1 para comparar
    cy.request('https://pokeapi.co/api/v2/berry/1').then((response1) => {
      const berry1 = response1.body;
      sizeBerry1 = berry1.size;
      soilDrynessBerry1 = berry1.soil_dryness;

      // Ahora obtenemos Berry 2
      cy.request('https://pokeapi.co/api/v2/berry/2').then((response2) => {
        const berry2 = response2.body;

        // Verificamos firmness.name
        expect(berry2.firmness.name).to.eq('super-hard');

        // Verificamos que el size sea mayor al de Berry 1
        expect(berry2.size).to.be.greaterThan(sizeBerry1);

        // Verificamos que soil_dryness sea igual al de Berry 1
        expect(berry2.soil_dryness).to.eq(soilDrynessBerry1);
      });
    });
  });
});
