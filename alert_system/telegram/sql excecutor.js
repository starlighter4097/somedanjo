


var mysql      = require('mysql');
let mysqlConfig={
    host     : 'localhost',
    user     : 'root1',
    password : 'password',
    database : 'alertsystem'
  };

function ExcecuteSQLquerry(sql)
{


let connection = mysql.createConnection(mysqlConfig);


connection.query(sql, (error, results, fields) => {
  if (error) {
    return console.error(error.message);
  }
  //console.log(results);
  
  results.forEach((item)=>{
               console.log(item);
               
    
            });
  
  
});

connection.end(); 
}
sql = `select * from attendance;`;


ExcecuteSQLquerry(sql);
        