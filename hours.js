const data =  require('./data/providers.json') //TODO will this work on browser?

// Function to get the current day and time
function getCurrentDayAndTime() {
    const now = new Date();
    const day = now.toLocaleString('en-US', { weekday: 'long' }); // Get full day name (e.g., "Tuesday")
    const hour = now.getHours(); // Get current hour in 24-hour format
    return { day, hour };
}


// Example usage
function checkProviders() {
    providerList = [];
    data.forEach(provider =>{
        const { day, hour } = getCurrentDayAndTime();
        range = provider.hours[day];
        if (Array.isArray(range)){
            const [start, end] = range;
            if (hour >= start && hour < end){
                providerList.push(provider);
            }
        }
    });
    return providerList;
}
p = checkProviders(); 
console.log(p);
