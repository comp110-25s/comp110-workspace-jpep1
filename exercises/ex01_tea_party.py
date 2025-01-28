"""Program to Plan Tea Party"""

__author__: str = "730574950"


def main_planner(guests: int) -> None:
    """Main planner function that calls each and produces printed output"""
    print(f"A Cozy Tea Party for {guests} People!\n")
    print(f"Tea Bags: {tea_bags(people=guests)}")
    print(f"Treats: {treats(people=guests)}")
    print(f"Cost: ${cost(tea_bags(people=guests), treats(people=guests))}\n")
    return None


def tea_bags(people: int) -> int:
    """Needed Tea Bags for Guests"""
    return people * 2


def treats(people: int) -> int:
    """Needed Treats Based on Number of Teas Drank"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Finding Cost of Tea Bags and Treats"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
