function filtrarCanciones() {
        const input = document.getElementById('inputBuscador');
        const filtro = input.value.toLowerCase().trim();
        const lista = document.getElementById('contenedorCanciones');
        const items = lista.getElementsByClassName('item-cancion');
        const mensajeVacio = document.getElementById('sinResultados');
        let coincidencias = 0;

        for (let i = 0; i < items.length; i++) {
            const titulo = items[i].querySelector('.titulo-cancion').textContent.toLowerCase();
            if (titulo.includes(filtro)) {
                items[i].style.display = "flex";
                coincidencias++;
            } else {
                items[i].style.display = "none";
            }
        }

        /* Mostrar mensaje si no hay resultados */
        if (mensajeVacio) {
            mensajeVacio.style.display = (coincidencias === 0 && items.length > 0) ? "block" : "none";
        }
    }