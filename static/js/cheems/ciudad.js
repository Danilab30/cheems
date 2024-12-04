function registrar(id){
    var url = "/ciudad-registro"
    $.get(url, function(data){
        $('#modal_info').html(data);
        $('#modal_info').modal({ backdrop: 'static', keyboard: false});
        $('#modal_info').modal('show');
        
        if (id) {
            document.getElementById('form-id').value = id;
        }
    })
}

function save_ciudad(){
    const id = document.getElementById('form-id').value;
    const nombre = document.getElementById('form-nombre').value;
    const codigo = document.getElementById('form-codigo').value;
    
    const data = {nombre, codigo};

    let url = '/ciudad';
    let method = 'POST';

    if (id) {
        url = `/ciudad/${id}`;
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
    const url = `/ciudad-eliminar/${id}`;
    
    if (confirm('¿Estás seguro de que deseas eliminar esta ciudad?')) {
        fetch(url, {
            method: 'DELETE',
        })
        .then(response => {
            if (response.status === 200) {
                alert('La ciudad se eliminó correctamente.');
                location.reload();
            } else if (response.status === 404) {
                alert('La ciudad no existe.');
            } else {
                alert(`Ocurrió un error al eliminar: ${response.status}`);
            }
        })
        .catch(error => console.error('Error:', error));
    }
}
