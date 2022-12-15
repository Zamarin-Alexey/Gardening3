
    console.log('ok')
    //  $('.btn-add-plant').click(function () {
    //     let id = $(this).parents('.card').attr('class').match(/\d+/)
    //     $.ajax({
    //         method: 'GET',
    //         data: {'plant_id': id[0]},
    //         url: `add_plant/`,
    //         success: function (response) {
    //         if (response.is_taken == true) {
    //             alert(response.message)
    //         }
    //         else {
    //             alert('Упс, произошла ошибка. Попробуйте позже')
    //         }
    //         },
    //     });
    //     return false;
    // });


function plantAdd(plant_id){
    console.log(plant_id)


            $.ajax({
                method: 'GET',
                data: {'plant_id': plant_id},
                url: 'add_plant/',
                success: function (response) {
                    console.log(response)
                    if (response.is_taken == true) {
                        console.log(response.mes)
                    } else {
                        alert('Упс, произошла ошибка. Попробуйте позже')
                    }
                },

            })
        };
    // $('.btn-add-plant').click(function () {
    //     let id = $(this).parents('.card').attr('class').match(/\d+/)
    //     $.ajax({
    //         method: 'GET',
    //         data: {'plant_id': id[0]},
    //         url: `add_plant/`,
    //         success: function (response) {
    //         if (response.is_taken == true) {
    //             alert(response.message)
    //         }
    //         else {
    //             alert('Упс, произошла ошибка. Попробуйте позже')
    //         }
    //         },
    //     });
    //     return false;
    // });
