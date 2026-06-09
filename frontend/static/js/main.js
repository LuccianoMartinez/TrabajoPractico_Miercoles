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