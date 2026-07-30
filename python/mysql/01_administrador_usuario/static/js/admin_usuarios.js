document.addEventListener('DOMContentLoaded', function () {

    // --- 1. REDIRECCIÓN DEL BOTÓN NUEVO USUARIO ---
    const btnNuevo = document.getElementById('btn-nuevo');
    
    if (btnNuevo) {
        btnNuevo.addEventListener('click', function () {
            window.location.href = 'nuevo_usuario.html';
        });
    }

    // --- 2. CARGA DINÁMICA DE USUARIOS ---
    const tableBody = document.getElementById('user-table-body');

    // Lista simulada de usuarios
    const usuariosDemo = [
        { nombre: 'Juan Pérez', email: 'juan.perez@liceovvh.cl', tipo: 'Administrador' },
        { nombre: 'María Rossi', email: 'maria.rossi@comeduc.cl', tipo: 'Docente' },
        { nombre: 'Diego Silva', email: 'diego.silva@liceovvh.cl', tipo: 'Estudiante' }
    ];

    if (tableBody) {
        tableBody.innerHTML = ''; // Limpiamos la tabla

        usuariosDemo.forEach(usuario => {
            const fila = document.createElement('tr');

            // Insertamos los datos y los tres botones en la celda de acciones
            fila.innerHTML = `
                <td>${usuario.nombre}</td>
                <td>${usuario.email}</td>
                <td>${usuario.tipo}</td>
                <td>
                    <button class="btn-action btn-edit" style="cursor:pointer; margin-right:5px; background:none; border:none;">✏️ Editar</button>
                    <button class="btn-action btn-delete" style="cursor:pointer; color:red; background:none; border:none;">🗑️ Eliminar</button>
                    <button class="btn-action btn-message" style="cursor:pointer; margin-right:5px; background:none; border:none;">💬 Mensaje</button>
                </td>
            `;

            // Acción: Enviar Mensaje
            fila.querySelector('.btn-message').addEventListener('click', () => {
                // Redirige al formulario de envío de mensajes
                window.location.href = 'enviar_mensaje.html';
            });

            // Acción: Editar Usuario
            fila.querySelector('.btn-edit').addEventListener('click', () => {
                window.location.href = 'editar_usuario.html';
            });

            // Acción: Eliminar Usuario
            fila.querySelector('.btn-delete').addEventListener('click', () => {
                if (confirm(`¿Estás seguro de que deseas eliminar a ${usuario.nombre}?`)) {
                    fila.remove();
                }
            });

            tableBody.appendChild(fila);
        });
    }
});