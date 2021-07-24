function new_save(elem) {
    elem.remove();
    let form = document.getElementById("new-save-form");
    form.innerHTML = "<form class='flex flex-column save-form' action='/new_save' method='post'><div class='save-label'>" +
    "<label for='new-save'>Save Name:</label><input class='color-black' type='text' name='new-save' id='new-save'>" +
    "</div><button class='color-black btn-new-save'>Create New Save</button></form>";
}

const handleSubmit = (e) => {
    let form = new FormData(e);
    for (var pair of form.entries()){
        console.log(pair[0], pair[1]);
    }
    fetch("http://localhost:5000/decision_interpreter", {method: "POST", body: form})
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            if (data.display) {
                let display_error = document.getElementById("decisionError");
                display_error.innerHTML = "";

                let display_room = document.getElementById("display-room");
                display_room.innerHTML = data.display + "<br><br>";

                let decision = document.getElementById("decision");
                decision.value = "";

            } else {
                let display_error = document.getElementById("decisionError");
                display_error.innerHTML = "<p></p><p>Unknown Command</p>";
            }
        })
        .catch((err) => console.log(err));
    }