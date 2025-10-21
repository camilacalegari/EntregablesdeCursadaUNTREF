describe('Casos de prueba saucedemo', () => {
  beforeEach(() => {
   cy.visit('https://www.saucedemo.com/')

   cy.get('#user-name').type('standard_user')
    cy.get('#password').type('secret_sauce')

    cy.get('#login-button').click()
  })
  
  it('Ordenar productos de menor a mayor precio', () => {
    cy.get('.product_sort_container').select('Price (low to high)')

    cy.get('.inventory_item_price').then(($prices) => {
      const prices = $prices.map((index, html) => parseFloat(html.innerText.replace('$', ''))).get()
      const sortedPrices = [...prices].sort((a, b) => a - b)
      expect(prices).to.deep.equal(sortedPrices)
    })
    
    
  })
  
  it('Checkout con campos vacios', () => {
    cy.get('.btn_inventory').each(($btn) => {
      cy.wrap($btn).click();
    });

    cy.get('a.shopping_cart_link').click();
    cy.get('.cart_item').should('have.length', 6);

    cy.get('#checkout').click();

    cy.get('#first-name').type('John');
    cy.get('#continue').click();
    cy.get('.error-message-container.error').should('be.visible').and('contain', 'Error: Last Name is required');

    cy.get('#last-name').type('Doe');
    cy.get('#continue').click();
    cy.get('.error-message-container.error').should('be.visible').and('contain', 'Error: Postal Code is required');


  })

  it('Checkout exitoso', () => {
    cy.get('.btn_inventory').first().click();
    cy.get('a.shopping_cart_link').click();
    cy.get('#remove-sauce-labs-backpack').click();
    cy.get('[data-test="shopping-cart-badge"]').should('not.exist');
    cy.get('#continue-shopping').click();

    cy.get('.btn_inventory').first().click();
    cy.get('.btn_inventory').last().click();
    cy.get('.shopping_cart_link').click();
    cy.get('.cart_item').should('have.length', 2);

    cy.get('#checkout').click();
    cy.get('#first-name').type('Jane');
    cy.get('#last-name').type('Smith');
    cy.get('#postal-code').type('54321');
    cy.get('#continue').click();

    cy.url().should('include', '/checkout-step-two.html');
    
    cy.get('#finish').click();

    cy.get('.checkout_complete_container').should('be.visible').and('contain', 'Thank you for your order!');

  })

})