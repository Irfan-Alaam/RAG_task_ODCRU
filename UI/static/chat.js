async function send() {
  const input = document.getElementById("question");
  const q = input.value.trim();

  if (!q) return;

  addMessage("You", q);
  input.value = "";

  const res = await fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question: q })
  });

  const data = await res.json();
  addMessage("Assistant", data.answer);
}

function addMessage(sender, text) {
  const chat = document.getElementById("chat");
  const div = document.createElement("div");
  div.className = sender === "You" ? "user" : "assistant";
  div.innerText = sender + ": " + text;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

function quick(text) {
  document.getElementById("question").value = text;
  send();
}

document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("question").addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      e.preventDefault();
      send();
    }
  });
});
