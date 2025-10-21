import 'cypress-mochawesome-reporter/register';

describe('Caso 2 - Berry 2', () => {
  it('Verifica firmeza, tamaño y soil_dryness comparado con berry 1', () => {

    // Obtener datos de berry/1 primero
    cy.request('https://pokeapi.co/api/v2/berry/1').then((response1) => {
      const berry1 = response1.body

      // Luego obtener berry/2
      cy.request('https://pokeapi.co/api/v2/berry/2').then((response2) => {
        const berry2 = response2.body

        expect(response2.status).to.eq(200)
        expect(berry2.firmness.name).to.eq('super-hard')
        expect(berry2.size).to.be.greaterThan(berry1.size)
        expect(berry2.soil_dryness).to.eq(berry1.soil_dryness)

        cy.log(`✅ Berry 2 firmeza: ${berry2.firmness.name}, tamaño: ${berry2.size}, soil_dryness: ${berry2.soil_dryness}`)
      })
    })
  })
})
