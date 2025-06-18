function showTab(tab) {
    const buyForm = document.getElementById('buy-form');
    const sellForm = document.getElementById('sell-form');
    const activeButton = document.querySelector('.tab-button.active');
    activeButton.classList.remove('active');

    if (tab === 'buy') {
        buyForm.style.display = 'block';
        sellForm.style.display = 'none';
        document.querySelector('.tab-button:nth-child(1)').classList.add('active');
    } else {
        buyForm.style.display = 'none';
        sellForm.style.display = 'block';
        document.querySelector('.tab-button:nth-child(2)').classList.add('active');
    }
}

const price = 90000;
function updateTotal(inputId, outputId, prefix = '$') {
    const amount = parseFloat(document.getElementById(inputId).value);
    if (!isNaN(amount)) {
        const total = amount * price;
        document.getElementById(outputId).value = `${prefix}${total.toFixed(2)}`;
    } else {
        document.getElementById(outputId).value = '';
    }
}

document.getElementById('buy-amount').addEventListener('input', () => {
    updateTotal('buy-amount', 'total-cost');
});

document.getElementById('sell-amount').addEventListener('input', () => {
    updateTotal('sell-amount', 'total-worth');
});
