# Pruebas Automatizadas con Cypress - SauceDemo

Este proyecto tiene los 3 casos de pruebas automatizadas para la web [SauceDemo](https://www.saucedemo.com/) utilizando Cypress.

## Casos de Prueba

### Caso 1
- El usuario se loguea al sitio como usuario standard user
- Ordenar los elementos por "price (low to high)"
- Verificar que los elementos estén ordenados

### Caso 2
- El usuario se loguea al sitio como usuario standard user
- Incorporar al carrito todos los elementos
- Ir al carrito
- Verificar que todos los elementos están en el carrito
- Ir al checkout
- Ingresar nombre y clickear Continue
- Verificar que aparece el error "Error: Last Name is required"
- Ingresar un apellido y clickear Continue
- Verificar que aparece el error "Error: Postal Code is required"

### Caso 3
- El usuario se loguea al sitio como usuario standard user
- Agregar un elemento al carrito
- Ir al carrito
- Remover el artículo
- Verificar que el sitio no tiene artículos agregados
- Ir a Continue Shopping
- Agregar dos elementos
- Ir al carrito
- Verificar que los elementos existen
- Hacer el checkout
- Finalizar la compra
- Verificar que la compra fue realizada

## Ejecución de Pruebas

Para ejecutar las pruebas en modo headless:

```bash
npm test
```
Para abrir el Test Runner de Cypress:

```bash
npm run cypress:open
```

## Reportes

Los reportes HTML se van a generar automáticamente después de cada ejecución y se pueden encontrar en la carpeta `cypress/reports`.

## Autor

Damián Héctor Rodríguez
