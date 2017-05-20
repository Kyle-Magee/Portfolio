var signup_button = document.getElementById('signup');
function add() {
    var new_student = document.getElementById('info');
    var table = document.getElementById('student_table');
    var row = table.insertRow(table.rows.length);
    var name = row.insertCell(0);
    var mathlvl = row.insertCell(1);
    var table_sitting = row.insertCell(2);
    var time = row.insertCell(3)
    var tutor = row.insertCell(4);
    var time_seen = row.insertCell(5);
    var check_in = row.insertCell(6);
    var check_out = row.insertCell(7);
    var time_done = row.insertCell(8);
    name.innerHTML = info.name.value;
    row.id = info.name.value + 'row';
    mathlvl.innerHTML = info.level.value;
    table_sitting.innerHTML = info.table_number.value;
    var cur_time = new Date();
    time.innerHTML = cur_time.getHours() + ':' + cur_time.getMinutes();
    tutor.innerHTML = dropdown;
    time_seen.id = 'time_seen'
    check_in.innerHTML = gen_button(info.name.value, 'visit_them', 'In');
    check_out.innerHTML = gen_button(info.name.value, 'leave_them', 'Out');
    new_student.reset();
}

function visit_them() {
    var target_row = document.getElementById(event.target.id + 'row');
    var time_seen = target_row.childNodes[5]
    target_row.setAttribute('style', 'background-color: yellow');
    var current_time = new Date();
    time_seen.innerHTML = current_time.getHours() + ':' + current_time.getMinutes();
}

function leave_them() {
    var target_row = document.getElementById(event.target.id + 'row');
    target_row.setAttribute('style', 'background-color: forestgreen');
    var cur_time = new Date();
    target_row.cells[8].innerHTML = cur_time.getHours() + ':' + cur_time.getMinutes();
    setTimeout(delete_row, 10000, target_row.rowIndex)

}

function gen_button(name, action, direction) {
    return '<button onclick="' + action + '()" id="' + name +'">Check ' + direction + '</button>' 
}

function delete_row(index) {
    var table = document.getElementById('student_table');
    table.deleteRow(index)
}



var dropdown = `<select name='tutors'>
                    <option value='nyger'>Nyger</option>
                    <option value='rebecca'>Rebecca</option>
                    <option value='christopher'>Christopher</option>
                    <option selected='selected'></option>
                </select>`;

var check_in_button = `<button onclick='visit_them()'>Check In</button>`;
var check_out_button = `<button onclick='finish_them()'>Check Out</button>`;