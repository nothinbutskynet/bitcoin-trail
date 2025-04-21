const gameState = {
    currentWallet: null,
    btcAmount: 1.0,
    days: 1,
    events: []
};

const walletData = {
    bitkey: {
        name: "Bitkey",
        recoveryTools: ["Self-Custody Recovery", "Social Recovery", "Emergency Access"],
        durability: 100,
        securityRating: 95
    },
    trezor: {
        name: "Trezor",
        recoveryTools: ["Seed Phrase Only"],
        durability: 80,
        securityRating: 85
    },
    ledger: {
        name: "Ledger",
        recoveryTools: ["Seed Phrase Only"],
        durability: 85,
        securityRating: 85
    },
    foundation: {
        name: "Foundation",
        recoveryTools: ["Seed Phrase Only"],
        durability: 75,
        securityRating: 80
    }
};

const events = [
    {
        id: "water_damage",
        title: "Water Damage!",
        description: "Your device fell into water!",
        bitkeyOutcome: {
            text: "Thanks to Bitkey's recovery tools, your bitcoin remains safe! Choose your recovery method:",
            choices: [
                {
                    text: "Use Self-Custody Recovery with your phone",
                    outcome: "You quickly recover access to your bitcoin using your phone. No seed phrase needed!"
                },
                {
                    text: "Contact trusted parties for Social Recovery",
                    outcome: "Your trusted contacts help you regain access to your bitcoin within hours."
                },
                {
                    text: "Use Emergency Access",
                    outcome: "Your emergency contact helps you recover access to your bitcoin."
                }
            ]
        },
        otherOutcome: {
            text: "Your device is damaged! Without a safe seed phrase backup, your bitcoin could be lost forever.",
            choices: [
                {
                    text: "Check your seed phrase backup",
                    outcome: "You hope your seed phrase backup is still readable and secure..."
                }
            ]
        }
    }
    // Add more events here
];

// Initialize game
document.addEventListener('DOMContentLoaded', () => {
    const walletButtons = document.querySelectorAll('.wallet-btn');
    walletButtons.forEach(button => {
        button.addEventListener('click', () => startGame(button.dataset.wallet));
    });
});

function startGame(walletType) {
    gameState.currentWallet = walletType;
    document.getElementById('current-wallet').textContent = walletData[walletType].name;
    document.getElementById('title-screen').classList.remove('active');
    document.getElementById('game-screen').classList.add('active');
    
    // Start first event
    triggerRandomEvent();
}

function triggerRandomEvent() {
    const event = events[Math.floor(Math.random() * events.length)];
    displayEvent(event);
}

function displayEvent(event) {
    const eventText = document.getElementById('event-text');
    const choices = document.getElementById('choices');
    
    eventText.innerHTML = `<h3>${event.title}</h3><p>${event.description}</p>`;
    
    const outcome = gameState.currentWallet === 'bitkey' ? event.bitkeyOutcome : event.otherOutcome;
    eventText.innerHTML += `<p>${outcome.text}</p>`;
    
    choices.innerHTML = '';
    outcome.choices.forEach(choice => {
        const button = document.createElement('button');
        button.textContent = choice.text;
        button.addEventListener('click', () => handleChoice(choice));
        choices.appendChild(button);
    });
}

function handleChoice(choice) {
    const eventText = document.getElementById('event-text');
    const choices = document.getElementById('choices');
    
    eventText.innerHTML += `<p>${choice.outcome}</p>`;
    choices.innerHTML = '<button onclick="triggerRandomEvent()">Continue Journey</button>';
    
    gameState.days += 1;
    document.getElementById('days').textContent = gameState.days;
}