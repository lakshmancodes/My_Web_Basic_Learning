var student = {"name": "Shiva", "regno": "20MIS0345", 'marks': "99", "grades": "A"}
var n = 1;
var list1;
var list2;
console.log(student);

function addRow(){
    var table = document.getElementById("list");
    var NewRow = table.insertRow(n);
    list1 = document.getElementById("name").value;
    list2 = document.getElementById("reg-no").value;
    if(list1 == student["name"]  && student["regno"] == list2){
        var cel1 = NewRow.insertCell(0);
        var cel2 = NewRow.insertCell(1);
        var cel3 = NewRow.insertCell(2);
        var cel4 = NewRow.insertCell(3);
    
        cel1.innerHTML = list1;
        cel2.innerHTML = list2;
        cel3.innerHTML = student["marks"];
        cel4.innerHTML = student["grades"];

    }
    
   
    n++;

}