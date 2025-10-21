const { defineConfig } = require('cypress');

module.exports = defineConfig({
  e2e: {
    specPattern: 'Punto_3_pokeapi/tests/**/*.cy.{js,jsx,ts,tsx}',
    supportFile: 'Punto_3_pokeapi/support/e2e.js',
    setupNodeEvents(on, config) {
      require('cypress-mochawesome-reporter/plugin')(on);
      return config;
    },
  },
  reporter: 'cypress-mochawesome-reporter',
  reporterOptions: {
    reportDir: 'Punto_3_pokeapi/reports/mochawesome',
    overwrite: false,
    html: true,
    json: true
  },
  fixturesFolder: 'Punto_3_pokeapi/fixtures'
});