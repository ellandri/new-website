
const ctx = document.getElementById('pie-chart').getContext('2d');
const pieChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Homme', 'Femme'],
        datasets: [{
            data: [50, 30], // Example data
            backgroundColor: ['#36A2EB', '#FF6384']
        }]
    },
    options: {
        responsive: true
    }
});