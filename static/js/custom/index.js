$('#suggestion-form').submit(function(event){
    var suggestion = $('#suggestions').val();
    var eAddress = $('#email').val();
    var baseUrl = $('#base-url').val();
    console.log(baseUrl);
    if($('#suggestions').val() == ''){
        $.toast({
            heading: 'Incomplete',
            text: 'Please enter comment',
            showHideTransition: 'fade',
            icon: 'error'
        })
        
    } else{
        $.ajax({url: baseUrl+"suggestions", 
        type:'POST',
        data:{'suggest':suggestion,'email':eAddress},
        success: function(result){
            $.toast({
                heading: 'Thank you',
                text: 'sent successfully',
                showHideTransition: 'fade',
                icon: 'success'
            })
            $('#suggestions').val('');
            $('#email').val('');
          }});
    }
   
});