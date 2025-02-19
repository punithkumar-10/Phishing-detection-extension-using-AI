document.getElementById('checkButton').addEventListener('click', async () => {    
    const resultDiv = document.getElementById('result');
    resultDiv.style.display = 'none';

    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    
    if (tab.url) {
        try {
            const response = await fetch('http://localhost:8000/check_url', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url: tab.url }),
            });
            
            const data = await response.json();
            resultDiv.textContent = data.result;
            resultDiv.className = data.result.includes('Yes') ? 'alert alert-danger' : 'alert alert-success';
            resultDiv.style.display = 'block';
        } catch (error) {
            console.error('Error:', error);
            resultDiv.textContent = 'Error checking URL.';
            resultDiv.className = 'alert alert-warning';
            resultDiv.style.display = 'block';
        }
    }
});
