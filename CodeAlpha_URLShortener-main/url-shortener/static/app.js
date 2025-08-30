const form = document.getElementById("shorten-form");
const result = document.getElementById("result");
const shortUrlA = document.getElementById("short-url");
const copyBtn = document.getElementById("copy-btn");
const copiedSpan = document.getElementById("copied");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  copiedSpan.classList.add("hidden");

  const formData = new FormData(form);
  const url = formData.get("url");

  try {
    const res = await fetch("/api/shorten", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url }),
    });

    const data = await res.json();
    if (!res.ok) {
      alert(data.error || "Failed to shorten the URL");
      return;
    }

    shortUrlA.href = data.short_url;
    shortUrlA.textContent = data.short_url;
    result.classList.remove("hidden");
  } catch (err) {
    alert("Network error. Please try again.");
  }
});

copyBtn.addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(shortUrlA.href);
    copiedSpan.classList.remove("hidden");
    setTimeout(() => copiedSpan.classList.add("hidden"), 1500);
  } catch (e) {
    alert("Copy failed. You can copy the link manually.");
  }
});
