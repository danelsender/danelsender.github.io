function sample() {
    const x = 3;

    const url = "http://localhost:8000/sample";

    const params = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ 
            x: x,
         }),
    };

    fetch(url, params).then((response) => {
        console.log(response);
        }).catch((error) => {
            console.log(error);
        });
}


function openTab(name) {
    name_str = name.toString();
    window.open(name_str, "_blank");
    }