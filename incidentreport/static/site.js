var signup_button = document.getElementById('signup');
function add() {
    var new_report = document.getElementById('report');
    var table = document.getElementById('incident_table');
    var row = table.insertRow(table.rows.length);
    var incident = row.insertCell(0);
    var device = row.insertCell(1);
    var location = row.insertCell(2);
    var date_time = row.insertCell(3)
    incident.innerHTML = report.incident.value;
    device.innerHTML = report.device.value;
    location.innerHTML = report.location.value;
    date_time.innerHTML = report.date.value + ' ' + report.time.value 
    new_report.reset();
}