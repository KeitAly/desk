{
    'name':'deks',
    'version':'1.0',
    'author':'the best',
    'description':' ',
    'depends':['base','web'],
    'data':[
        'security/ir.model.access.csv',
        'views/partenaire.xml',
        'views/immobilier.xml',
        'views/location.xml',
        'views/menu.xml',
        'reports/contrat_report.xml',
        
    ],
    'assets':{
        'web.assets_backend':['desk/static/css/global.css']
    }
   
}