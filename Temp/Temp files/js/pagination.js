/* --------------- Pagination js Start --------------- */
$(document).ready(function(){
    $('#row_limit').dataTable({searching: false, ordering: false});
});
/* --------------- Pagination js End --------------- */


/* --------------- Search js Start --------------- */
$('#search_input').on('keyup',function(){
    var value = $(this).val()
    console.log('Value:', value)
    var data = searchTable(value, myArray)
    buildTable(data)
})

function searchTable(value, data){
    var filteredData = []

    for (var i = 0; i <data.length; i ++){
        value = value.toLowerCase()
        var name = data[i].name.toLowerCase()

        if(name.includes(value)){
            filteredData.push(data[i])
        }
    }
    return filteredData
}
/* --------------- Search js End --------------- */