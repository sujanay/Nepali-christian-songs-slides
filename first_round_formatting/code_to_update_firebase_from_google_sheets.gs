// https://stackoverflow.com/questions/65862681/cannot-add-firebase-library-to-apps-script
// firebase library id: 1hguuh4Zx72XVC1Zldm_vTtcUUKUA6iBUOoGnJUWLfqDWx5WlOJHqYkrt

function writeDataToFirebase() {

  // Copy the spreadsheet ID from the url link
  var ss = SpreadsheetApp.openById("1m7lChx_ZGy9QqE2QxrT_RoQ0oLNN92znMSbrtRRjNyk");

  // Select first sheet
  var sheet = ss.getSheets()[0];
  var data = sheet.getDataRange().getValues();
  var dataToImport = {};
  for(var i = 1; i < data.length; i++) {
    var uuid = Utilities.getUuid()
    var id = data[i][0]
    var type = data[i][1]
    var typeLong = data[i][2];
    var title = data[i][3];
    var scale = data[i][4];
    var timeSignature = data[i][5];
    var content = String(data[i][6]);

    dataToImport[uuid] = {
      id:id,
      type:type,
      typeLong:typeLong,
      title:title,
      scale:scale,
      timeSignature:timeSignature,
      //formating string to center align and set font size to 24
      content:String('<p style="font-size: 36; text-align: center;">').concat(content, "</p>")
    };

  }
  //console.log(String('<p style="font-size: 24; text-align: center;">').concat(content, "</p>"))
  var firebaseUrl = "https://bhajan-2b87a-default-rtdb.firebaseio.com/bhajans";
  var base = FirebaseApp.getDatabaseByUrl(firebaseUrl);
  base.setData("", dataToImport);
}
