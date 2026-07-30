document.addEventListener('DOMContentLoaded', function () {
    // --- 1. MOSTRAR / OCULTAR CONTRASEÑAS ---
    // Configuración para el Login
    const togglePassword = document.querySelector('#togglePassword');
    const loginPasswordInput = document.querySelector('#login-password');
    if (togglePassword && loginPasswordInput) {
        togglePassword.addEventListener('click', function () {
            const type = loginPasswordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            loginPasswordInput.setAttribute('type', type);
            this.classList.toggle('fa-eye-slash');
        });
    }
    // Configuración para el Registro
    const toggleRegPassword = document.querySelector('#toggleRegPassword');
    const regPasswordInput = document.querySelector('#reg-password');
    if (toggleRegPassword && regPasswordInput) {
        toggleRegPassword.addEventListener('click', function () {
            const type = regPasswordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            regPasswordInput.setAttribute('type', type);
            this.classList.toggle('fa-eye-slash');
        });
    }
    // --- 2. VALIDACIÓN E INGRESO DE FORMULARIOS ---
    // Definimos la página común a la que irán ambos botones
    const destinoUrl = 'templates/admin_usuarios.html';
    // Función auxiliar para validar correos institucionales
    function esCorreoInstitucional(email) {
        return email.endsWith('@liceovvh.cl') || email.endsWith('@comeduc.cl');
    }
    // CONTROLADOR DEL FORMULARIO DE INICIO DE SESIÓN
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const email = document.getElementById('login-email').value.trim();
            
            if (!esCorreoInstitucional(email)) {
                alert('Correo no válido. Solo se permiten correos institucionales.');
                return;
            }
            // Si todo está bien, redirige y limpia
            window.location.href = destinoUrl;
            loginForm.reset();
        });
    }
    // CONTROLADOR DEL FORMULARIO DE REGISTRO
    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const email = document.getElementById('reg-email').value.trim();
            const password = document.getElementById('reg-password').value;
            const confirmPassword = document.getElementById('reg-confirm').value;
            // Validación de correo institucional
            if (!esCorreoInstitucional(email)) {
                alert('Correo no válido. Solo se permiten correos institucionales para el registro.');
                return;
            }
            // Validación extra para el registro: verificar que las contraseñas coincidan
            if (password !== confirmPassword) {
                alert('Las contraseñas no coinciden. Por favor, verifícalas.');
                return;
            }
            // Si pasa los filtros, te manda a la misma página
            window.location.href = destinoUrl;
            registerForm.reset();
        });
    }
});