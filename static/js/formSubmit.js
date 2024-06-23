document
  .getElementById("contactForm")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const formObject = Object.fromEntries(formData.entries());

    try {
      const response = await fetch("/submit_contact", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formObject),
      });

      const result = await response.json();
      document.getElementById("responseMessage").textContent = result.message;
    } catch (error) {
      document.getElementById("responseMessage").textContent =
        "Error submitting form.";
    }
  });
