// #Este codigo es de Damian Rodriguez
// Caso 2: Validación de errores en el proceso de checkout

describe('Caso 2 - Validación de errores en checkout', () => {
  it('Debe mostrar los mensajes de error apropiados durante el checkout', () => {
    // Visitar la página de inicio
    cy.visit('https://www.saucedemo.com/');

    // Login como usuario standar
    cy.get('[data-test="username"]').type('standard_user');
    cy.get('[data-test="password"]').type('secret_sauce');
    cy.get('[data-test="login-button"]').click();

    // Verificar que estamos en la página de productos
    cy.url().should('include', '/inventory.html');

    // Agregar todos los elementos al carrito
    cy.get('.inventory_item').each(($item) => {
      cy.wrap($item).find('button[id^="add-to-cart"]').click();
    });

    // Verificar que el contador del carrito muestra corretamente la cantidad de productos y Verificar que el contador del carrito coincida con el número de productos
    cy.get('.shopping_cart_badge').then(($badge) => {
      const itemCount = parseInt($badge.text());
      cy.get('.inventory_item').its('length').then((totalItems) => {
        expect(itemCount).to.equal(totalItems);
      });
    });

    // Ir al carrito
    cy.get('.shopping_cart_link').click();
    cy.url().should('include', '/cart.html');

    // Verificar que todos los productos están en el carrito
    cy.get('.cart_item').its('length').then((cartItems) => {
      // Almacenar el número de productos para comparar
      cy.get('.shopping_cart_badge').then(($badge) => {
        const itemCount = parseInt($badge.text());
        expect(cartItems).to.equal(itemCount);
      });
    });

    // Ir al checkout
    cy.get('[data-test="checkout"]').click();
    cy.url().should('include', '/checkout-step-one.html');

    // Ingresar solo el nombre y hacer clic en Continue
    cy.get('[data-test="firstName"]').type('juan');
    cy.get('[data-test="continue"]').click();

    // Verificar el mensaje de error para apellido requerido
    cy.get('[data-test="error"]').should('contain', 'Error: Last Name is required');

    // Ingresar apellido y hacer clic en Continue
    cy.get('[data-test="lastName"]').type('perez');
    cy.get('[data-test="continue"]').click();

    // Verificar el mensaje de error para código postal requerido
    cy.get('[data-test="error"]').should('contain', 'Error: Postal Code is required');
  });
});
