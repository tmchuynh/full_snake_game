const prefix = [
    "Sir",
    "Lady",
    "Knight",
    "Dame",
    "Lord",
    "Baron",
    "Baroness",
    "Duke",
    "Duchess",
    "Prince",
    "Princess",
    "Marquis",
    "Marchioness",
    "Count",
    "Countess",
    "Viscount",
    "Viscountess",
    "Squire",
    "Noble",
    "Ruler",
    "Monarch",
    "Queen",
    "King",
    "Emperor",
    "Empress",
    "Sovereign",
    "Chancellor",
    "Governor",
    "Warden"
]

const titles_suffixes = [
    "of Oxford",
    "of Avalon",
    "from Camelot",
    "of the Realm",
    "of the Highlands",
    "from the Court",
    "of the Order",
    "of the Keep",
    "from the Kingdom",
    "of the Castle",
    "from the Guild",
    "of the House",
    "of the Clan",
    "from the Province",
    "of the Duchy",
    "from the Fortress",
    "of the Enclave",
    "from the City",
    "of the Isle",
    "from the Region",
    "of the Heritage",
    "of the Crown",
    "from the Estate",
    "of the Manor",
    "of the Empire"
]

const usernames = [
    "FrostyNinja42",
    "EpicGamerX",
    "MysticWizard99",
    "ShadowHunter7",
    "StarGazer23",
    "DragonRider88",
    "QuantumKnight",
    "LunarEclipse7",
    "SilentStorm33",
    "RogueWarrior21",
    "GoldenPhoenix",
    "CelestialVoyager",
    "NebulaWalker",
    "TurboFalcon",
    "StealthAssassin",
    "CosmicExplorer",
    "ThunderStrike5",
    "ArcaneMage77",
    "NebulaRider",
    "DarkPhoenix88",
    "SolarFlare42",
    "SilverArrow",
    "GalacticHero",
    "MysticNinja",
    "StormBringer99"
]

function randomIndex(array) {
    return Math.floor(Math.random() * array.length);
}

function randomNameGenerate() {
    const usernameInput = document.querySelector(".form-control");
    let username = randomIndex([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
    if (username % 2 == 0) {
        username = usernames[randomIndex(usernames)];
    } else {
        let pre = prefix[randomIndex(prefix)];
        let suffix = titles_suffixes[randomIndex(titles_suffixes)];
        username = pre + " " + suffix;
    }
    usernameInput.value = username;
}

const showFirstModal = (message) => {
    const modal = document.querySelector(".usernameInput");
    const modalMessage = modal.querySelector(".modal-message");
    modalMessage.innerText = message;
    modal.style.display = "block";
};

function closeModal() {
    document.addEventListener("keyup", changeDirection);
    const modal = document.querySelector(".modal");
    modal.style.display = "none";
}

showFirstModal("Let's play!");

function redirectToSnakeGame() {
    window.location.href = "/snake_game";
}