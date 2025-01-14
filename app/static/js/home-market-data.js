function getRandomPriceChange(currentPrice) {
    let priceChange = (Math.random() > 0.5 ? 1 : -1) * Math.floor(Math.random() * 1000);
    return Math.max(25, Math.min(1000000, currentPrice + priceChange));
}

function getRandomPercentage() {
    return (Math.random() * 10 - 5).toFixed(2);
}

function getRandomMarketCapChange(currentMarketCap) {
    const marketCapChange = (Math.random() * 10 - 5) / 100;
    return (currentMarketCap * (1 + marketCapChange)).toFixed(2);
}

function getRandomVolumeChange(currentVolume) {
    const volumeChange = (Math.random() * 10 - 5) / 100;
    return (currentVolume * (1 + volumeChange)).toFixed(2);
}

function getRandomSupplyChange(currentSupply) {
    const supplyChange = (Math.random() * 2 - 1) / 100;
    return (currentSupply * (1 + supplyChange)).toFixed(0);
}

function updateCell(cell, value) {
    cell.textContent = value;
    if (value.includes('%')) {
        const change = parseFloat(value);
        cell.classList.toggle('text-success', change > 0);
        cell.classList.toggle('text-danger', change <= 0);
    }
}

function updateTable() {
    document.querySelectorAll('#coinTable tbody tr').forEach(row => {
        let previousValues = [...row.querySelectorAll('td')].slice(3, 6).map(cell => parseFloat(cell.textContent.replace(/[^0-9.-]+/g, "")));
        let marketCap = parseFloat(row.cells[6].textContent.replace(/[^0-9.-]+/g, ""));
        let volume = parseFloat(row.cells[7].textContent.replace(/[^0-9.-]+/g, ""));
        let supply = parseFloat(row.cells[8].textContent.replace(/[^0-9.-]+/g, "").replace(/,/g, ""));

        row.querySelectorAll('td').forEach((cell, i) => {
            if (i === 2) {
                updateCell(cell, `$${getRandomPriceChange(parseFloat(cell.textContent.replace(/[^0-9.-]+/g, ""))).toFixed(2)}`);
            } else if (i >= 3 && i <= 5) {
                updateCell(cell, `${getRandomPercentage()}%`);
            } else if (i === 6) {
                updateCell(cell, `$${getRandomMarketCapChange(marketCap)}`);
            } else if (i === 7) {
                updateCell(cell, `$${getRandomVolumeChange(volume)}`);
            } else if (i === 8) {
                updateCell(cell, `${getRandomSupplyChange(supply)}`);
            }
        });
    });
}

setInterval(updateTable, 1500);
