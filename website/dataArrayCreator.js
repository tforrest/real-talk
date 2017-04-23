 <script src="http://jquery-csv.googlecode.com/git/src/jquery.csv.js"></script>

 var file = new File([""], "RealTalkSessionsRaw.csv");
 var reader = new FileReader();
      reader.readAsText(file);
      reader.onload = function(event){
        var csv = event.target.result;
        var data = $.csv.toArrays(csv);
      }
