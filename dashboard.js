document.addEventListener('DOMContentLoaded', () => {
    const batchSelect = document.getElementById('batch');
    const currentYear = new Date().getFullYear();
    const startYear = currentYear - 10;
    const endYear = currentYear + 10;

    for (let year = startYear; year <= endYear; year++) {
        const option = document.createElement('option');
        option.value = year;
        option.textContent = year;
        batchSelect.appendChild(option);
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const batchSelect = document.getElementById('batchanalyse');
    const currentYear = new Date().getFullYear();
    const startYear = currentYear - 10;
    const endYear = currentYear + 10;

    for (let year = startYear; year <= endYear; year++) {
        const option = document.createElement('option');
        option.value = year;
        option.textContent = year;
        batchSelect.appendChild(option);
    }
});

function showSection(sectionId) {
    document.getElementById('batchSection').style.display = 'none';
    document.getElementById('staffSection').style.display = 'none';
    document.getElementById('analysisSection').style.display = 'none';
    document.getElementById(sectionId).style.display = 'block';
}
