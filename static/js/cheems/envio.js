function registrar(id){
    var url = "/envio-registro"
    $.get(url, function(data){
        $('#modal_info').html(data);
        $('#modal_info').modal({ backdrop: 'static', keyboard: false});
        $('#modal_info').modal('show');
    })
}

function save(){
    
    const origen = document.getElementById('form-origen').value;
    const destino = document.getElementById('form-destino').value;
    const fecha_envio = document.getElementById('form-fecha_envio').value;
    const remitente = document.getElementById('form-remitente').value;
    const destinatario = document.getElementById('form-destinatario').value;
    const guia = document.getElementById('form-guia').value;

    const data = {origen, destino, fecha_envio, remitente, destinatario, guia};



    fetch('/ciudad', {
        method: 'POST',
        headers: { 'Content-Type' : 'application/json'},
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.status === 201) {
            alert('El registro se guardó correctamente');
            location.reload();
        } else {
            alert(`Ocurrió un error al guardar: ${response.status}`);
        }
    })
    .catch(error => console.error('Error:', error));
}