document.addEventListener("DOMContentLoaded", () => {
    // 1. Seleccionamos ambos formularios mediante las etiquetas internas de sus secciones
    const loginForm = document.querySelector(".form-section:nth-of-type(1) form");
    const registerForm = document.querySelector(".form-section:nth-of-type(2) form");

    // 2. Evento para el formulario de Inicio de Sesión
    if (loginForm) {
        loginForm.addEventListener("submit", (event) => {
            // Evita que el formulario intente recargar la página o enviarse a un servidor
            event.preventDefault(); 
            
            // Redirige a la pantalla del Dashboard de Administrador
            window.location.href = "dashboard_mensajes.html"; 
        });
    }

    // 3. Evento para el formulario de Registro
    if (registerForm) {
        registerForm.addEventListener("submit", (event) => {
            event.preventDefault(); 
            
            // Redirige a la pantalla del Dashboard de Administrador
            window.location.href = "dashboard_mensajes.html"; 
        });
    }
});