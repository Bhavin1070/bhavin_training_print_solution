{
	'name' : 'Print Service',
	'summary' : 'This is a Print service Application',
	'description' : 'This Application Provide online printing services and couriar services',
	'author' : 'Bhavin Patel',
	'version' : '0.1',
	'depends' : ['base', 'web_dashboard'],
	'data' : [
		'security/ir.model.access.csv',
		'data/data.xml',
		'report/report.xml',
		'views/main_template.xml',
	],
	'demo' : [
	],
	'application': True
}