async function play(choice) {
    const res = await fetch("/play", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ choice })
    });
    const data = await res.json();
    document.getElementById("user").textContent = data.user;
    document.getElementById("computer").textContent = data.computer;
    document.getElementById("result").textContent = data.result;
}
