document.addEventListener('DOMContentLoaded', function () {
    const regionSelect = document.getElementById('region');
    const sepaBankDetails = document.getElementById('sepa-bank-details');
    const swiftBankDetails = document.getElementById('swift-bank-details');

    regionSelect.addEventListener('change', function () {
        sepaBankDetails.style.display = 'none';
        swiftBankDetails.style.display = 'none';

        if (regionSelect.value === 'eu') {
            sepaBankDetails.style.display = 'block';
        }
        else if (regionSelect.value === 'other') {
            swiftBankDetails.style.display = 'block';
        }
    });
});
