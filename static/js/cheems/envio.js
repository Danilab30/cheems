function registrar(id){
    var url = "/envio-registro"
    $.get(url, function(data){
        $('#modal_info').html(data);
        $('#modal_info').modal({ backdrop: 'static', keyboard: false});
        $('#modal_info').modal('show');

        if (id) {
            document.getElementById('form-id').value = id;
        }
    })
}

function save_envio(){
    const id = document.getElementById('form-id').value;
    const origen = document.getElementById('form-origen').value;
    const destino = document.getElementById('form-destino').value;
    const remitente = document.getElementById('form-remitente').value;
    const destinatario = document.getElementById('form-destinatario').value;
    const guia = document.getElementById('form-guia').value;

    const data = {origen, destino, remitente, destinatario, guia};

    let url = '/envio';
    let method = 'POST';

    if (id) {
        url = `/envio/${id}`;
        method = 'PUT';
    }

    fetch(url, {
        method: method,
        headers: { 'Content-Type' : 'application/json'},
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.status === 201 || response.status === 200) {
            alert('El registro se guardó correctamente');
            location.reload();
        } else {
            alert(`Ocurrió un error al guardar: ${response.status}`);
        }
    })
    .catch(error => console.error('Error:', error));
}
function eliminar(id) {
    const url = `/envio-eliminar/${id}`;
    
    if (confirm('¿Estás seguro de que deseas eliminar este envio?')) {
        fetch(url, {
            method: 'DELETE',
        })
        .then(response => {
            if (response.status === 200) {
                alert('El envio se eliminó correctamente.');
                location.reload();
            } else if (response.status === 404) {
                alert('El envio no existe.');
            } else {
                alert(`Ocurrió un error al eliminar: ${response.status}`);
            }
        })
        .catch(error => console.error('Error:', error));
    }
}
