
import 'cypress-mochawesome-reporter/register';

describe('Caso 3 - Pikachu', () => {
  it('Verifica experiencia base y tipo eléctrico', () => {
    cy.request('https://pokeapi.co/api/v2/pokemon/pikachu/').then((response) => {
      expect(response.status).to.eq(200)

      const data = response.body
      const baseExperience = data.base_experience
      const tipos = data.types.map(t => t.type.name)

      // Verificar que la experiencia base esté entre 10 y 1000
      expect(baseExperience).to.be.greaterThan(10)
      expect(baseExperience).to.be.lessThan(1000)

      // Verificar que el tipo sea "electric"
      expect(tipos).to.include('electric')

      cy.log(`✅ Pikachu tiene experiencia base ${baseExperience} y tipo ${tipos}`)
    })
  })
})
