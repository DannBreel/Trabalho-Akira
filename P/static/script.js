function toggleMenu() {

    const sidebar = document.getElementById("sidebar")
    const overlay = document.getElementById("overlay")

    sidebar.classList.toggle("active")
    overlay.classList.toggle("active")
}

function abrirModal() {

    document.getElementById("modalSalvar").style.display = "flex"
}

function fecharModal() {

    document.getElementById("modalSalvar").style.display = "none"
}

function toggleEdit(id) {

    const form = document.getElementById(`edit-${id}`)

    if (form.style.display === "flex") {
        form.style.display = "none"
    }
    else {
        form.style.display = "flex"
    }
}