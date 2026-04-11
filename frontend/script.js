const form = document.getElementById("predictionForm");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async function (event) {
	event.preventDefault();

	const formData = new FormData(form);

	const payload = {
		radius_mean: parseFloat(formData.get("radius_mean")),
		texture_mean: parseFloat(formData.get("texture_mean")),
		perimeter_mean: parseFloat(formData.get("perimeter_mean")),
		area_mean: parseFloat(formData.get("area_mean")),
		smoothness_mean: parseFloat(formData.get("smoothness_mean")),
		concavity_mean: parseFloat(formData.get("concavity_mean")),
		concave_points_mean: parseFloat(formData.get("concave_points_mean")),
		symmetry_mean: parseFloat(formData.get("symmetry_mean"))
	};

	resultDiv.innerHTML = "Processando...";

	try {
		const response = await fetch("http://127.0.0.1:5000/predict", {
			method: "POST",
			headers: {
				"Content-Type": "application/json"
			},
			body: JSON.stringify(payload)
		});

		const data = await response.json();

		if (!response.ok) {
			resultDiv.innerHTML = `<span class="error">Erro: ${data.error}</span>`;
			return;
		}

		const classe = data.prediction === 1 ? "maligno" : "benigno";

		resultDiv.innerHTML = `
      <div>
        <div><strong>Predição:</strong> ${data.prediction}</div>
        <div class="${classe}"><strong>Diagnóstico:</strong> ${data.diagnosis}</div>
      </div>
    `;
	} catch (error) {
		resultDiv.innerHTML = `<span class="error">Erro ao conectar com a API.</span>`;
	}
});