// #Este codigo es de Damian Rodriguez
// Caso 1: Verificar ordenamiento de productos por precio (low to high)

describe('Caso 1 - Ordenamiento de productos', () => {
  it('Debe ordenar los productos por precio (low to high) correctamente', () => {
    // Visitar la página de inicio
    cy.visit('https://www.saucedemo.com/');

    // Login como usuario standar
    cy.get('[data-test="username"]').type('standard_user');
    cy.get('[data-test="password"]').type('secret_sauce');
    cy.get('[data-test="login-button"]').click();

    // Verificar que estamos en la página de productos
    cy.url().should('include', '/inventory.html');

    // Ordenar productos por precio (low to high)
    cy.get('.product_sort_container').select('lohi');

    // Obtener todos los precios de los productos
    cy.get('.inventory_item_price')
      .then($prices => {
        // Extraer los precios como números y Eliminar el símbolo $ y convertir a número
        const prices = Array.from($prices).map(el => {
          return parseFloat(el.innerText.replace('$', ''));
        });

        // Verificar que los precios estén ordenados de menor a mayor
        const sortedPrices = [...prices].sort((a, b) => a - b);
        
        // Comparar los arrays para verificar que están ordenados
        expect(prices).to.deep.equal(sortedPrices);
      });
  });
});
