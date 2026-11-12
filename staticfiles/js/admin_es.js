(function () {
    const placeholders = {
        "Type to search": "Escribe para buscar...",
        "Search apps and models...": "Buscar módulos y tablas...",
        "Search": "Buscar",
        "Filter": "Filtrar"
    };

    const textosExactos = {
        // Botón lateral y buscador rápido (Ctrl + K)
        "Search apps and models...": "Buscar módulos y tablas...",
        "Type to search": "Escribe para buscar...",
        "Navigate": "Navegar",
        "Select": "Seleccionar",
        "Clear": "Limpiar",
        "Close": "Cerrar",
        "No results found": "No se encontraron resultados",
        "Recent searches": "Búsquedas recientes",
        "Navigation": "Navegación",
        "Dashboard": "Panel principal",
        "Home": "Inicio",
        "Toggle sidebar": "Alternar menú lateral",

        // Menú de usuario y tema
        "Account": "Cuenta",
        "View site": "Ver sitio web",
        "View on site": "Ver en el sitio web",
        "Change password": "Cambiar contraseña",
        "Log out": "Cerrar sesión",
        "Theme": "Tema",
        "Light": "Claro",
        "Dark": "Oscuro",
        "System": "Sistema",
        "Welcome back to": "Bienvenido a",
        "Return to site": "Volver al sitio web",

        // Tablas, filtros y acciones masivas
        "Select action": "Seleccionar acción",
        "Action:": "Acción:",
        "Action": "Acción",
        "Run": "Ejecutar",
        "Go": "Ir",
        "Filters": "Filtros",
        "Filter": "Filtrar",
        "Reset filters": "Limpiar filtros",
        "Apply filters": "Aplicar filtros",
        "Clear all filters": "Borrar todos los filtros",
        "Show all": "Mostrar todo",
        "Previous": "Anterior",
        "Next": "Siguiente",
        "All": "Todos",
        "Yes": "Sí",
        "No": "No",
        "Unknown": "Desconocido",

        // Filtros de fecha
        "Any date": "Cualquier fecha",
        "Today": "Hoy",
        "Past 7 days": "Últimos 7 días",
        "This month": "Este mes",
        "This year": "Este año",
        "No date": "Sin fecha",
        "Has date": "Con fecha",

        // Formularios y botones de guardado
        "Save": "Guardar",
        "Save and continue editing": "Guardar y continuar editando",
        "Save and add another": "Guardar y añadir otro",
        "Save as new": "Guardar como nuevo",
        "Delete": "Eliminar",
        "History": "Historial",
        "Add": "Añadir",
        "Change": "Modificar",
        "View": "Ver",
        "Choose a file": "Seleccionar archivo",
        "No file chosen": "Ningún archivo seleccionado",
        "Currently:": "Actualmente:",
        "Now": "Ahora",
        "Date:": "Fecha:",
        "Time:": "Hora:",
        "Note:": "Nota:",
        "Optional": "Opcional",
        "Required": "Obligatorio",

        // Confirmaciones e historial
        "Are you sure?": "¿Estás seguro?",
        "Yes, I’m sure": "Sí, estoy seguro",
        "Yes, I'm sure": "Sí, estoy seguro",
        "No, take me back": "No, volver atrás",
        "Date/time": "Fecha y hora",
        "User": "Usuario",
        "Recent actions": "Acciones recientes",
        "My actions": "Mis acciones",
        "None available": "Ninguna disponible"
    };

    const reglasDinamicas = [
        { regex: /^(\d+)\s+of\s+(\d+)\s+selected$/i, reemplazo: "$1 de $2 seleccionados" },
        { regex: /^Delete selected\s+(.+)$/i, reemplazo: "Eliminar $1 seleccionados" },
        { regex: /^Select\s+(.+)\s+to change$/i, reemplazo: "Seleccione $1 para modificar" },
        { regex: /^Select\s+(.+)\s+to view$/i, reemplazo: "Seleccione $1 para ver" },
        { regex: /^Add\s+(.+)$/i, reemplazo: "Añadir $1" },
        { regex: /^Change\s+(.+)$/i, reemplazo: "Modificar $1" }
    ];

    function traducirCadena(texto) {
        if (textosExactos[texto]) {
            return textosExactos[texto];
        }
        for (const regla of reglasDinamicas) {
            if (regla.regex.test(texto)) {
                return texto.replace(regla.regex, regla.reemplazo);
            }
        }
        return null;
    }

    function activarVistaPreviaSalario() {
        const inputSalario = document.getElementById("id_salario");
        if (!inputSalario || inputSalario.dataset.copActivo) return;
        inputSalario.dataset.copActivo = "true";

        const preview = document.createElement("div");
        preview.style.marginTop = "6px";
        preview.style.fontWeight = "600";
        preview.style.color = "#0284c7";
        preview.style.fontSize = "0.9rem";
        inputSalario.parentNode.insertAdjacentElement("afterend", preview);

        const actualizar = () => {
            const soloNumeros = inputSalario.value.replace(/\D/g, "");
            if (!soloNumeros) {
                preview.textContent = "Valor exacto: $ 0 COP";
                return;
            }
            const formateado = Number(soloNumeros).toLocaleString("es-CO");
            preview.textContent = `Valor exacto: $ ${formateado} COP`;
        };

        inputSalario.addEventListener("input", actualizar);
        actualizar();
    }

    function traducirInterfaz() {
        if (!document.body) return;

        // 1. Placeholders de buscadores e inputs
        document.querySelectorAll("input[placeholder], textarea[placeholder]").forEach((el) => {
            const actual = el.getAttribute("placeholder").replace(/\s+/g, " ").trim();
            if (placeholders[actual]) {
                el.setAttribute("placeholder", placeholders[actual]);
            }
        });

        // 2. Botones tipo <input type="submit" value="...">
        document.querySelectorAll('input[type="submit"], input[type="button"]').forEach((el) => {
            const val = (el.value || "").replace(/\s+/g, " ").trim();
            const trad = traducirCadena(val);
            if (trad) el.value = trad;
        });

        // 3. Tooltips y etiquetas de accesibilidad
        document.querySelectorAll("[title], [aria-label]").forEach((el) => {
            ["title", "aria-label"].forEach((attr) => {
                const val = el.getAttribute(attr);
                if (val) {
                    const trad = traducirCadena(val.replace(/\s+/g, " ").trim());
                    if (trad) el.setAttribute(attr, trad);
                }
            });
        });

        // 4. Todos los nodos de texto visibles (incluyendo botones con saltos de línea)
        const etiquetasIgnoradas = new Set(["SCRIPT", "STYLE", "TEXTAREA", "INPUT", "CODE", "PRE"]);
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
        let nodo;

        while ((nodo = walker.nextNode())) {
            const padre = nodo.parentElement;
            if (!padre || etiquetasIgnoradas.has(padre.tagName)) continue;

            const limpio = nodo.nodeValue.replace(/\s+/g, " ").trim();
            if (!limpio) continue;

            const traduccion = traducirCadena(limpio);
            if (traduccion && traduccion !== limpio) {
                const inicio = nodo.nodeValue.match(/^\s*/)[0];
                const fin = nodo.nodeValue.match(/\s*$/)[0];
                nodo.nodeValue = inicio + traduccion + fin;
            }
        }

        // 5. Vista previa formateada en pesos colombianos (COP)
        activarVistaPreviaSalario();
    }

    function iniciar() {
        traducirInterfaz();
        const observer = new MutationObserver(() => {
            traducirInterfaz();
        });
        observer.observe(document.body, { childList: true, subtree: true });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", iniciar);
    } else {
        iniciar();
    }
})();