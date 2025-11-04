from __future__ import annotations

class LoyaltyProgram:
    def __init__(self, program_name: str, member_id: str, tier: str, points: int = 0) -> None:
        self.program_name: str = program_name
        self.member_id: str = member_id
        self.tier: str = tier
        self.points: int = points

    def add_points(self, amount: int) -> None:
        self.points += amount

    def redeem_points(self, amount: int) -> bool:
        if amount > self.points:
            return False
        self.points -= amount
        return True
