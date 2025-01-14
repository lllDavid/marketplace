function showTab(tab) {
    if (tab === 'buy') {
        document.getElementById('buy-form').style.display = 'block';
        document.getElementById('sell-form').style.display = 'none';
        document.querySelector('.tab-button.active').classList.remove('active');
        document.querySelector('.tab-button:nth-child(1)').classList.add('active');
    } else {
        document.getElementById('buy-form').style.display = 'none';
        document.getElementById('sell-form').style.display = 'block';
        document.querySelector('.tab-button.active').classList.remove('active');
        document.querySelector('.tab-button:nth-child(2)').classList.add('active');
    }
}

// @todo: Get actual values for coins from db/api
document.getElementById('buy-amount').addEventListener('input', function () {
    const amount = parseFloat(this.value);
    const price = 90000;
    if (!isNaN(amount)) {
        const totalCost = amount * price;
        document.getElementById('total-cost').value = `$${totalCost.toFixed(2)}`;
    } else {
        document.getElementById('total-cost').value = '';
    }
});

// @todo: Get actual values for coins from db/api
document.getElementById('sell-amount').addEventListener('input', function () {
    const amount = parseFloat(this.value);
    const price = 90000;
    if (!isNaN(amount)) {
        const totalWorth = amount * price;
        document.getElementById('total-worth').value = `$${totalWorth.toFixed(2)}`;
    } else {
        document.getElementById('total-worth').value = '';
    }
});

document.getElementById('payment-method').addEventListener('change', function () {
    if (this.value === 'fiat') {
        document.getElementById('buy-limit-container').style.display = 'none';
    } else {
        document.getElementById('buy-limit-container').style.display = 'block';
    }
});
