let originalData = {};

function populateTable() {
    fetch(walletValuesUrl)
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById("coin-data");
            tbody.innerHTML = '';

            const fiatBalanceElem = document.getElementById("fiat-balance");
            if (data.fiat_balance !== undefined) {
                fiatBalanceElem.textContent = `Fiat Balance: $${data.fiat_balance.toFixed(2)}`;
            } else {
                fiatBalanceElem.textContent = 'Fiat Balance: N/A';
            }

            if (data.coins && Object.keys(data.coins).length > 0) {
                originalData = { ...data.coins };

                Object.keys(data.coins).forEach(coin => {
                    const row = document.createElement("tr");
                    const coinData = data.coins[coin];
                    const totalValue = coinData.amount * coinData.current_price;

                    row.innerHTML = `
                        <td>${coin}</td>
                        <td>${coinData.amount}</td>
                        <td class="coin-price">${coinData.current_price}</td>
                        <td class="coin-total">${totalValue}</td>
                    `;
                    tbody.appendChild(row);
                });

                setInterval(updateCoinPrices, 1000);
            } else {
                tbody.innerHTML = '<tr><td colspan="4">No coins in wallet.</td></tr>';
            }
        })
        .catch(error => {
            console.error("Error fetching wallet data:", error);
            document.getElementById("coin-data").innerHTML = '<tr><td colspan="4">Error loading data</td></tr>';
        });
}
function updateCoinPrices() {
    const coinRows = document.querySelectorAll("#coin-data tr");
    coinRows.forEach(row => {
        const coinName = row.querySelector("td:first-child").textContent;
        const coinPriceCell = row.querySelector(".coin-price");
        const coinTotalCell = row.querySelector(".coin-total");

        if (coinName && coinPriceCell && coinTotalCell) {
            let originalPrice = originalData[coinName].current_price;

            let priceChange = Math.random() > 0.5 ? 10 : -10;
            let newPrice = (originalPrice + priceChange).toFixed(2);
            coinPriceCell.textContent = newPrice;
            const amount = parseFloat(row.querySelector("td:nth-child(2)").textContent);
            const newTotalValue = (amount * newPrice).toFixed(2);
            coinTotalCell.textContent = newTotalValue;
        }
    });
}

document.addEventListener("DOMContentLoaded", function () {
    populateTable();
    updateCoinPrices();
});
