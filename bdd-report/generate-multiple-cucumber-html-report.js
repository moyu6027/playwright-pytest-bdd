const report = require('multiple-cucumber-html-reporter');

report.generate({
	jsonDir: 'bdd-report/',
	reportPath: 'bdd-report/',
	metadata:{
        browser: {
            name: 'chrome',
            version: '94.0.4595.0'
        },
        device: 'Docker test machine',
        platform: {
            name: 'ubuntu',
            version: '18.04'
        }
    }
});