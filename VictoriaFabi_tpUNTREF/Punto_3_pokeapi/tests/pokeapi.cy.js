describe('template spec', () => {
  it('passes', () => {
    cy.request('https://pokeapi.co/api/v2')
  })
});

// caso 1 Hacer un get a berry/1 ● Verifi car que el size sea 20 ● Verifi car que el soil_dryness sea 15 ● Verifi car que en fi rmness, el name sea soft.
describe('PokeAPI Berries', () => {
  it('Validates berry/1 properties', () => {
    cy.request('https://pokeapi.co/api/v2/berry/1').then((response) => {
      expect(response.status).to.eq(200);

      expect(response.body.size).to.eq(20);
      expect(response.body.soil_dryness).to.eq(15);
      expect(response.body.firmness.name).to.eq('soft');
    });
  });
});

// caso 2 Hacer un get a berry/2 ● Verifi car que en fi rmness, el name sea super-hard ● Verifi car que el size sea mayor al del punto anterior ● Verifi car que el soil_dryness sea igual al del punto anterior
describe('PokeAPI Berries', () => {
  it('Validates berry/2 properties', () => {
    cy.request('https://pokeapi.co/api/v2/berry/2').then((response) => {
      expect(response.status).to.eq(200); 
      expect(response.body.firmness.name).to.eq('super-hard');
      expect(response.body.size).to.be.greaterThan(20);
      expect(response.body.soil_dryness).to.eq(15);
    });
  });
});

// caso 3 Hacer un get a pikachu (https://pokeapi.co/api/v2/pokemon/pikachu/) ● Verifi car que su experiencia base es mayor a 10 y menor a 1000 ● Verifi car que su tipo es “electric”

describe('PokeAPI Pokemon', () => {
  it('Validates pikachu properties', () => {
    cy.request('https://pokeapi.co/api/v2/pokemon/pikachu/').then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body.base_experience).to.be.greaterThan(10);
      expect(response.body.base_experience).to.be.lessThan(1000);
      const types = response.body.types.map(typeInfo => typeInfo.type.name);
      expect(types).to.include('electric');
    });
  });
});
