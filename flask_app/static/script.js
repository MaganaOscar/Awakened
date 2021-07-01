function new_save(elem) {
    elem.remove();
    let form = document.getElementById("new-save-form");
    form.innerHTML = "<form class='flex flex-column save-form' action='/new_save' method='post'><div class='save-label'>" +
    "<label for='new-save'>Save Name:</label><input class='color-black' type='text' name='new-save' id='new-save'>" +
    "</div><button class='color-black btn-new-save'>Create New Save</button></form>";
}

const handleSubmit = (e) => {
    console.log(e);
    let form = new FormData(e);
    console.log(form);
    fetch("http://localhost:5000/decision_interpreter", {method: "POST", body: form})
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
        })
}