function plantAdd(plant_id){
    $.ajax({
        method: 'GET',
        data: {'plant_id': plant_id},
        url: 'add_plant/',
        success: function (response) {
            alert(response.messages)
            console.log(response)
        },
        error: function(response){
            console.log(response.error())
        }
    })
}