document.addEventListener('DOMContentLoaded', () => {
    // Current year in footer
    const currentYearEl = document.getElementById('currentYear');
    if (currentYearEl) {
        currentYearEl.textContent = new Date().getFullYear();
    }

    // Calculator elements
    const initialInput = document.getElementById('initialAmount');
    const monthlyInput = document.getElementById('monthlyContribution');
    const returnInput = document.getElementById('expectedReturn');
    const yearsInput = document.getElementById('investmentYears');

    const initialValDisplay = document.getElementById('initialAmountVal');
    const monthlyValDisplay = document.getElementById('monthlyVal');
    const returnValDisplay = document.getElementById('returnVal');
    const yearsValDisplay = document.getElementById('yearsVal');

    const futureValueResult = document.getElementById('futureValueResult');
    const totalPrincipalResult = document.getElementById('totalPrincipalResult');
    const totalInterestResult = document.getElementById('totalInterestResult');

    function formatCurrency(amount) {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            maximumFractionDigits: 0
        }).format(amount);
    }

    function calculateGrowth() {
        const P = parseFloat(initialInput.value);
        const PMT = parseFloat(monthlyInput.value);
        const annualRate = parseFloat(returnInput.value) / 100;
        const years = parseInt(yearsInput.value, 10);

        // Update display labels
        initialValDisplay.textContent = formatCurrency(P);
        monthlyValDisplay.textContent = formatCurrency(PMT);
        returnValDisplay.textContent = `${returnInput.value}%`;
        yearsValDisplay.textContent = `${years} Years`;

        const r = annualRate / 12;
        const n = years * 12;

        // Compound interest with monthly contributions
        // FV = P * (1 + r)^n + PMT * [((1 + r)^n - 1) / r]
        let fv = P * Math.pow(1 + r, n);
        if (r > 0) {
            fv += PMT * ((Math.pow(1 + r, n) - 1) / r);
        } else {
            fv += PMT * n;
        }

        const totalContributions = P + (PMT * n);
        const totalInterest = Math.max(0, fv - totalContributions);

        futureValueResult.textContent = formatCurrency(fv);
        totalPrincipalResult.textContent = formatCurrency(totalContributions);
        totalInterestResult.textContent = formatCurrency(totalInterest);
    }

    // Attach event listeners
    [initialInput, monthlyInput, returnInput, yearsInput].forEach(input => {
        if (input) {
            input.addEventListener('input', calculateGrowth);
        }
    });

    // Run initial calculation
    calculateGrowth();

    // Serverless API check button
    const checkApiBtn = document.getElementById('checkApiBtn');
    const apiResult = document.getElementById('apiResult');

    if (checkApiBtn && apiResult) {
        checkApiBtn.addEventListener('click', async () => {
            apiResult.classList.remove('hidden');
            apiResult.textContent = 'Querying Vercel Serverless Function (/api/status)...';
            try {
                const res = await fetch('/api/status');
                if (!res.ok) {
                    throw new Error(`HTTP ${res.status}: ${res.statusText}`);
                }
                const data = await res.json();
                apiResult.textContent = JSON.stringify(data, null, 2);
            } catch (err) {
                // Fallback for local preview without serverless runner
                apiResult.textContent = `API Endpoint: /api/status\nResponse Status: Ready on Vercel deployment (${err.message})`;
            }
        });
    }
});
