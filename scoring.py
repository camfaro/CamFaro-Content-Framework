# scoring.py

def calculate_platform_score(price, usability, safety, support):
    score = (
        price * 0.25 +
        usability * 0.25 +
        safety * 0.30 +
        support * 0.20
    )

    return round(score, 2)


if __name__ == "__main__":
    score = calculate_platform_score(
        price=7,
        usability=8,
        safety=6,
        support=7
    )

    print("Score da plataforma:", score)
