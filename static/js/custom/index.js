$('#suggestion-form').submit(function(event){
    if($('#suggestions').val() == ''){
        alert('Comment section cannot be empty!')
        event.preventDefault()
    }
    
});