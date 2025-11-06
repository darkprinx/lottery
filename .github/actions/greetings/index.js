const core = require('@actions/core');
const github = require('@actions/github');

function generateGreeting() {
    const currentTime = new Date();
    const hour = currentTime.getHours();

    core.notice(`Current time: ${currentTime.toLocaleString()}`);

    let greeting;
    if (hour < 12) greeting = "Good morning";
    else if (hour < 18) greeting = "Good afternoon";
    else greeting = "Good evening";

    return `${greeting}! 🌟
    Action executed at: ${currentTime.toLocaleString()}
    Current repository: ${github.context.repo.owner}/${github.context.repo.repo}`;
}

// Example usage
console.log(generateGreeting());
