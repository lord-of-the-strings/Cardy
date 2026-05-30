import requests
import json
HANDLE='Aadity1729'
url=f"https://codeforces.com/api/user.info?handles={HANDLE}"
response=requests.get(url).json()
if response["status"]=="OK":
    user_data=response["result"][0]
    rating=user_data.get("rating","Unrated")
    max_rating=user_data.get("maxRating","Unrated")
    rank=user_data.get("rank","Newbie")
    svg_template = f"""
    <svg width="350" height="120" viewBox="0 0 350 120" fill="none" xmlns="http://www.w3.org/2000/svg">
        <style>
            .title {{ font: bold 16px 'Segoe UI', Ubuntu, sans-serif; fill: #61afef; }}
            .stat {{ font: 14px 'Segoe UI', Ubuntu, sans-serif; fill: #abb2bf; }}
            .rank {{ font: bold 14px 'Segoe UI', Ubuntu, sans-serif; fill: #e5c07b; }}
        </style>
        <rect width="100%" height="100%" rx="10" fill="#282c34"/>
        <text x="20" y="35" class="title">{HANDLE.upper()}'S CODEFORCES STATUS</text>
        <text x="20" y="65" class="stat">Current Rating: <tspan font-weight="bold">{rating}</tspan></text>
        <text x="20" y="90" class="stat">Rank: <tspan class="rank">{rank.title()}</tspan></text>
    </svg>
    """
    with open("codeforces_card.svg", "w") as f:
        f.write(svg_template)
