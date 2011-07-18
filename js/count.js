window.addEvent('domready', function(){
        $('count-button').addEvent('click', function(){
                var count = 0;
                $('students').getElements('input').each(function(e){
                        if(e.type == 'checkbox' && e.checked){
                                count++;
                        }
                });
                $('count-textbox').set('text',count);
        });
});
