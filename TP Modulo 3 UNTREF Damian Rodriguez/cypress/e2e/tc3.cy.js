// #Este codigo es de Damian Rodriguez
// Caso 3: Flujo completo de compra con manejo del carrito

describe('Caso 3 - Flujo completo de compra', () => {
  it('Debe completar el flujo de compra correctamente', () => {
    // Visitar la página de inicio
    cy.visit('https://www.saucedemo.com/');

    // Login como standard_user
    cy.get('[data-test="username"]').type('standard_user');
    cy.get('[data-test="password"]').type('secret_sauce');
    cy.get('[data-test="login-button"]').click();

    // Verificar que estamos en la página de productos
    cy.url().should('include', '/inventory.html');

    // Agregar un elemento al carrito
    cy.get('.inventory_item').first().find('button[id^="add-to-cart"]').click();

    // Ir al carrito
    cy.get('.shopping_cart_link').click();
    cy.url().should('include', '/cart.html');

    // Remover el producto
    cy.get('button[id^="remove"]').click();

    // Verificar que el carrito está vacío
    cy.get('.cart_item').should('not.exist');

    // Ir a Continue Shopping
    cy.get('[data-test="continue-shopping"]').click();
    cy.url().should('include', '/inventory.html');

    // Agregar dos elementos
    cy.get('.inventory_item').eq(0).find('button[id^="add-to-cart"]').click();
    cy.get('.inventory_item').eq(1).find('button[id^="add-to-cart"]').click();

    // Ir al carrito
    cy.get('.shopping_cart_link').click();
    cy.url().should('include', '/cart.html');

    // Verificar que los productos existen en el carrito
    cy.get('.cart_item').should('have.length', 2);

    // Hacer el checkout
    cy.get('[data-test="checkout"]').click();
    cy.url().should('include', '/checkout-step-one.html');

    // Completar información de envío
    cy.get('[data-test="firstName"]').type('Damian');
    cy.get('[data-test="lastName"]').type('Rodriguez');
    cy.get('[data-test="postalCode"]').type('010101');
    cy.get('[data-test="continue"]').click();

    // Verificar que estamos en la página de checkout
    cy.url().should('include', '/checkout-step-two.html');

    // Finalizar la compra
    cy.get('[data-test="finish"]').click();

    // Verificar que la compra se realizo exitosamente
    cy.url().should('include', '/checkout-complete.html');
    cy.get('.complete-header').should('contain', 'Thank you for your order');
  });
});
