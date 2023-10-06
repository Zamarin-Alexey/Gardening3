$(document).ready(function(){
    $('#id_username').change(function () {
        $.ajax({
            data: $(this).serialize(),
            url: "validate_username",
            success: function (response) {
            if (response.is_taken == true) {
                $('#id_username').removeClass('is-valid').addClass('is-invalid');
                $('#id_username').after('Это имя пользователя недоступно!')
            }
            else {
                $('#id_username').removeClass('is-invalid').addClass('is-valid');
                $('#usernameError').remove();
            }
            },
        });
        return false;
    });

    $('#button-edit-user-profile').click(function (){
        $('#edit-user-form').css('display', 'block')
        $(this).css('display', 'None')
    })
})
