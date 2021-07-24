setInterval(trackTime, 1000);
const second = {sec: 1};
let saveId = document.getElementById("saveId").value;
function trackTime() {
    console.log("hello")

    fetch(`http://localhost:5000/update_time/${saveId}`, {method: "POST", body: second})
        .catch((err) => console.log(err));
}