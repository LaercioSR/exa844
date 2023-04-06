function doGet(request) {
  const sheet = SpreadsheetApp.getActiveSheet();
  const { message, author } = request.parameter;

  if(message && author) {
    sheet.appendRow([message, author, new Date()]);
  }

  const template = HtmlService.createTemplateFromFile("Blog.html");

  return template.evaluate();
}

function getMessages() {
  const sheet = SpreadsheetApp.getActiveSheet();

  const data = sheet.getRange(2, 1, sheet.getLastRow()-1, 3).getValues();

  return JSON.stringify(data)
}
