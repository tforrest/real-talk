
function createTable(tableData) {
  var table = document.createElement('table');
  var tableBody = document.createElement('tbody');

  tableData.forEach(function(rowData) {
    var row = document.createElement('tr');

    rowData.forEach(function(cellData) {
      var cell = document.createElement('td');
      cell.appendChild(document.createTextNode(cellData));
      row.appendChild(cell);
    });

    tableBody.appendChild(row);
  });

  table.appendChild(tableBody);
  document.body.appendChild(table);
}

var data = [14][14];
var file = new File([""], "RealTalkSessionsRaw.csv");
var reader = new FileReader();
     reader.readAsText(file);
     reader.onload = function(event){
       var csv = event.target.result;
       var data = $.csv.toArrays(csv);
     }
console.log(data);
//createTable(data);

//entertainment (BOOL),exercise (BOOL),mood (N),productivity (N),schoolwork (BOOL),sleepHrs (N),sleepWell (BOOL),socialized (BOOL),work (BOOL),dayOfWeek
createTable([["Conflict", "Entertainment", "Exercise ", "Mood", "Productivity", "Schoolwork", "Hours of Sleep", "Sleep Quality", "Socialization", "Work", "Date"],
["NO","YES","NO","3","3","YES","1","7","YES","NO","Monday"],
["YES","YES","NO","2","2","YES","2","5","NO","NO","Tuesday"],
 ["NO","NO","YES","3","3","NO","3","6","YES","NO","Wednesday"],
 ["NO","NO","YES","4","4","YES","4","8","YES","NO","Thursday"],
 ["NO","YES","NO","4","3","YES","5","7","YES","YES","Friday"],
 ["YES","NO","NO","3","3","YES","6","6","NO","YES","Saturday"],
 ["NO","NO","NO","2","3","NO","7","6","NO","NO","Sunday"],
 ["NO","NO","NO","2","2","NO","8","5","NO","NO","Monday"],
 ["NO","YES","NO","3","3","YES","9","7","NO","NO","Tuesday"],
 ["NO","YES","NO","3","3","YES","10","7","NO","NO","Wednesday"],
 ["NO","YES","NO","3","3","YES","11","7","NO","NO","Thursday"],
 ["NO","YES","NO","3","3","YES","12","7","NO","NO","Friday"],
 ["NO","YES","NO","3","3","YES","13","7","NO","NO","Saturday"],
 ["NO","YES","NO","3","3","YES","14","7","NO","NO","Sunday"]]);
