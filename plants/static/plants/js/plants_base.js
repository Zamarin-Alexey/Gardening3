$(document).ready(function(){
    console.log('ok')
    $('.btn-add-plant').click(function () {
        let id = $(this).parents('.card').attr('class').match(/\d+/)
        $.ajax({
            data: {'plant_id': id[0]},
            url: `add_plant/`,
            success: function (response) {
            if (response.is_taken == true) {
                alert(response.message)
            }
            else {
                alert('Упс, произошла ошибка. Попробуйте позже')
            }
            },
        });
        return false;
    });
})
