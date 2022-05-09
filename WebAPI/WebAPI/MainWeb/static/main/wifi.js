$(document).ready(function(){

    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $("#createButton").click(function(){
        var serializerData = $("#createUserForm").serialize();
        var rowCount = $("tr").length;
        $.ajax({
            url: $("#createUserForm").data('url'),
            data: serializerData,
            type: 'POST',
            success : function(response){
                $("#dataList").append('<tr id="dataRT" data-id="'+response.dataList.id+'"><th scope="row">'+rowCount+'</th><td>'+response.dataList.username+'</td><td>'+response.dataList.password+'</td><td><a href="" class="btn btn-danger" data-id="'+response.dataList.id+'"><i class="bi bi-trash"></i></a></td></tr>')
            }
        })
        $("#createUserForm")[0].reset();
    });

    $("#dataList").on('click', 'button', function(event){
        event.stopPropagation();
        var dataId = $(this).data('id');
        console.log(dataId)
        $.ajax({
            url: '/main/' + dataId + '/delete/',
            data:{
                csrfmiddlewaretoken : csrfToken,
                data: dataId
            },
            type:'post',
            dataType:'json',
            success:function(){
                $('#dataTR[data-id="'+dataId+'"]').remove();
            }
        })
    })
});