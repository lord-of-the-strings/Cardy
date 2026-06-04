import requests

HANDLE = 'Aadity1729'
url = f"https://cryptohack.org/api/user/{HANDLE}/"

try:
    response = requests.get(url).json()
    username = response.get("username", HANDLE)
    score = response.get("score", 0)
    rank = response.get("rank", "N/A")
    level = response.get("level", 1)
    first_bloods = response.get("first_bloods", 0)

    svg_template = f"""<svg width="350" height="140" viewBox="0 0 350 140" fill="none" xmlns="http://www.w3.org/2000/svg">
        <style>
            .title {{ font: bold 16px 'Segoe UI', Ubuntu, sans-serif; fill: #2eaf7d; }}
            .stat {{ font: 14px 'Segoe UI', Ubuntu, sans-serif; fill: #a4b1cd; }}
            .value {{ font-weight: bold; fill: #ffffff; }}
            .highlight {{ font-weight: bold; fill: #fa8231; }}
        </style>
        <rect width="100%" height="100%" rx="10" fill="#1d2530" stroke="#2eaf7d" stroke-width="1.5"/>
        <text x="20" y="35" class="title">{username.upper()}'S CRYPTOHACK STATS</text>
        <text x="20" y="65" class="stat">Score: <tspan class="value">{score}</tspan></text>
        <text x="20" y="90" class="stat">Level: <tspan class="value">{level}</tspan></text>
        <text x="20" y="115" class="stat">Rank: <tspan class="highlight">#{rank}</tspan></text>
    </svg>
    """

    with open("cryptohack_card.svg", "w") as f:
        f.write(svg_template)
    print("CryptoHack card updated successfully!")

except Exception as e:
    print(f"Error fetching CryptoHack data: {e}")