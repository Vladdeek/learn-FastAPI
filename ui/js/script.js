async function addUser() {
    let name = document.getElementById("name").value;
    let age = document.getElementById("age").value;

    if (!name || !age) {
        document.getElementById("result").innerText = "Заполните все поля!";
        return;
    }

    let userData = { name, age: parseInt(age) };

    try {
        let response = await fetch("http://127.0.0.1:8000/users/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(userData)
        });

        if (response.ok) {
            let data = await response.json();
            document.getElementById("result").innerText = "Пользователь добавлен: " + JSON.stringify(data);
        } else {
            let errorData = await response.json();
            document.getElementById("result").innerText = "Ошибка: " + errorData.detail;
        }
    } catch (error) {
        console.error("Ошибка запроса:", error);
        document.getElementById("result").innerText = "Ошибка соединения с сервером";
    }
}