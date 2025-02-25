async function loadData() {
    try {
        const response = await fetch('./data/providers.json');
        if (!response.ok) {
            throw new Error('Failed to load JSON data');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error loading JSON:', error);
    }
}

// Function to get the current day and time
function getCurrentDayAndTime() {
    const now = new Date();
    const day = now.toLocaleString('en-US', { weekday: 'long' }); // Get full day name (e.g., "Tuesday")
    const hour = now.getHours(); // Get current hour in 24-hour format
    return { day, hour };
}


// Example usage
function checkProviders(data) {
    let providerList = [];
    data.forEach(provider =>{
        const { day, hour } = getCurrentDayAndTime();
        let range = provider.hours[day];
        if (Array.isArray(range)){
            const [start, end] = range;
            if (hour >= start && hour < end){
                providerList.push(provider);
            }
        }
    });
    return providerList;
}

async function main() {
    const data = await loadData();
    const providers = checkProviders(data);
    return providers;
}

