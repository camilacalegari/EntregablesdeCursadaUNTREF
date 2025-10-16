require('cypress-xpath');
//Agregamos un command para simplificar el proceso de login
Cypress.Commands.add('loginStandardUser', () => {
  cy.visit('https://www.saucedemo.com/')
  cy.get('#user-name').type('standard_user')
  cy.get('#password').type('secret_sauce')
  cy.get('#login-button').click()
})

describe(' Punto 3 - Automation ', () => {
it('Caso 1 - Verifica orden por precio (low to high)', () => {

  cy.loginStandardUser();
  cy.get('.product_sort_container').select(2);

  let valor1, valor2, valor3, valor4, valor5, valor6;

  cy.xpath('//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div/text()[2]')
    .invoke('text').then((texto) => {
      valor1 = texto.trim();
    });

  cy.xpath('//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div/text()[2]')
    .invoke('text').then((texto) => {
      valor2 = texto.trim();
    });

  cy.xpath('//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div/text()[2]')
    .invoke('text').then((texto) => {
      valor3 = texto.trim();
    });

  cy.xpath('//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div/text()[2]')
    .invoke('text').then((texto) => {
      valor4 = texto.trim();
    });

  cy.xpath('//*[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div/text()[2]')
    .invoke('text').then((texto) => {
      valor5 = texto.trim();
    });

  cy.xpath('//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div/text()[2]')
    .invoke('text').then((texto) => {
      valor6 = texto.trim();
    });

  cy.then(() => {
    cy.log(`Valor 1: ${valor1}`);
    cy.log(`Valor 2: ${valor2}`);
    cy.log(`Valor 3: ${valor3}`);
    cy.log(`Valor 4: ${valor4}`);
    cy.log(`Valor 5: ${valor5}`);
    cy.log(`Valor 6: ${valor6}`);

    if (
      parseFloat(valor1) <= parseFloat(valor2) &&
      parseFloat(valor2) <= parseFloat(valor3) &&
      parseFloat(valor3) <= parseFloat(valor4) &&
      parseFloat(valor4) <= parseFloat(valor5) &&
      parseFloat(valor5) <= parseFloat(valor6)
    ) {
      cy.log(' Los precios están ordenados de menor a mayor (permitiendo iguales)');
    } 
  });
});


    it('Caso 2 - Verifica errores en el proceso de compra', () => {
    cy.loginStandardUser()
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    cy.get('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    cy.get('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    cy.get('[data-test="add-to-cart-sauce-labs-fleece-jacket"]').click()
    cy.get('[data-test="add-to-cart-sauce-labs-onesie"]').click()
    cy.get('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
    // Ahora verificamos que se agregaron todos los productos (6 en total) al carrito de compra, 
    // en este caso usare como referencia, la cantidad de articulos que aparecen sobre el icono del carrito de compras
   
    if (cy.get('[data-test="shopping-cart-badge"]').contains("6"))
        { cy.log ("Primera validacion, verificamos la cantidad de articulos en el icono del carrito !")}

    cy.get('[data-test="shopping-cart-link"]').click()
    // agregamos una segunda verificacion dentro del carrito de compra, contamos la cantidad de articulos 
    if (cy.get('[data-test="inventory-item"]').should('have.length', 6))
        { cy.log ("Segunda validacion, contamos la cantidad de productos dentro del carrito !")}
    cy.get('[data-test="checkout"]').click()
    cy.get('[data-test="firstName"]').type('Juan')
    cy.get('[data-test="continue"]').click()
    cy.contains('Error: Last Name is required')

    cy.get('[data-test="lastName"]').type('Pérez')
    cy.get('[data-test="continue"]').click()
    cy.contains('Error: Postal Code is required')
  })

    it('Caso 3 - Verifica agregar, remover y finalizar compra', () => {
    cy.loginStandardUser()
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    cy.get('.shopping_cart_link').click()
    cy.get('[data-test="remove-sauce-labs-backpack"]').click()
    cy.get('.cart_item').should('not.exist')

    cy.get('[data-test="continue-shopping"]').click()
    cy.get('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    cy.get('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    cy.get('.shopping_cart_link').click()
    cy.get('.cart_item').should('have.length', 2)

    cy.get('[data-test="checkout"]').click()
    cy.get('[data-test="firstName"]').type('Juan')
    cy.get('[data-test="lastName"]').type('Pérez')
    cy.get('[data-test="postalCode"]').type('1234')
    cy.get('[data-test="continue"]').click()
    cy.get('[data-test="finish"]').click()
    cy.get('[data-test="complete-header"]').contains('Thank you for your order!')
  })

    it('Caso 4 - Verifica propiedades de berry/1', () => {
    cy.request('https://pokeapi.co/api/v2/berry/1').then((response) => {
      expect(response.body.size).to.eq(20)
      expect(response.body.soil_dryness).to.eq(15)
      expect(response.body.firmness.name).to.eq('soft')
    })
  })

    it('Caso 5 - Verifica propiedades de berry/2 en relación a berry/1', () => {
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


    it('Caso 6 - Verifica experiencia y tipo de Pikachu', () => {
    cy.request('https://pokeapi.co/api/v2/pokemon/pikachu').then((response) => {
      expect(response.body.base_experience).to.be.within(11, 999)
      const tipos = response.body.types.map(t => t.type.name)
      expect(tipos).to.include('electric')
    })
  })

})
