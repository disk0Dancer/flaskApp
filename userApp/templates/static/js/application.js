$(document).ready(function() {

    $('.dropdown-toggle').dropdown();

    $('#filter').click(
        function(){
            get_flights();
        }
    );

    function get_flights(){
        var message = {
                source: $('#source').val()
            }
        $('#result_table').empty();
        $.ajax({
            type:'POST',
            url: '/get_flights',
            processData: false,  // tell jQuery not to process the data
            contentType: false,  // tell jQuery not to set contentType
            data: JSON.stringify(message),
            success: (data) => {
                    console.log(data);
                    for(i in data)
                    {
                        flight = data[i]
                        $('#result_table').append("<tr>" +
                        "<td>"+flight['flight']+"</td>" +
                        "<td>"+flight['source']+"</td>" +
                        "<td>"+flight['dest']+"</td>" +
                        "<td>"+flight['start_date']+"</td>" +
                        "<td>"+flight['days']+"</td>" +
                        "<td>"+flight['depart']+"</td>" +
                        "<td>"+flight['arrival']+"</td>" +
                        "</tr>")
                    }

                }
            });
    }
});
