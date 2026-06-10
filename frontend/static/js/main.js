async function confirmarAsistencia(eventoId) {
    try {
        const response = await fetch(`/api/confirmar/${eventoId}`, {
            method: 'POST'
        });
        const data = await response.json();
        if (response.ok) {
            alert('✓ Asistencia confirmada');
            location.reload();
        } else {
            alert('✗ ' + (data.error || 'Error'));
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function cancelarAsistencia(eventoId) {
    if (confirm('¿Estás seguro?')) {
        try {
            const response = await fetch(`/api/cancelar/${eventoId}`, {
                method: 'POST'
            });
            const data = await response.json();
            if (response.ok) {
                alert('✗ Asistencia cancelada');
                location.reload();
            } else {
                alert('Error');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    }
}

async function borrarEvento(eventoId) {
    if (!confirm('¿Eliminar este evento? Esta acción no se puede deshacer.')) return;
    try {
        const response = await fetch(`/api/eventos/${eventoId}/`, {
            method: 'DELETE'
        });
        let data = null;
        try { data = await response.json(); } catch(e) { /* respuesta no JSON */ }

        if (response.ok) {
            alert('✓ Evento borrado');
            window.location.href = '/';
        } else {
            alert('✗ ' + (data && (data.detail || data.error) ? (data.detail || data.error) : ('Error: ' + response.status)));
        }
    } catch (error) {
        console.error('Error borrando evento:', error);
        alert('No se pudo borrar el evento. Revisa la consola del navegador o la consola del servidor.');
    }
}
