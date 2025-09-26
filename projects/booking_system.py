"""Mock booking system: create/reserve/cancel slots."""

class BookingSystem:
    def __init__(self):
        self.slots = {}  # slot_id -> { 'available': bool, 'user': Optional[str] }

    def create_slot(self, slot_id: str):
        self.slots[slot_id] = {"available": True, "user": None}

    def reserve(self, slot_id: str, user: str) -> bool:
        s = self.slots.get(slot_id)
        if s and s["available"]:
            s["available"] = False
            s["user"] = user
            return True
        return False

    def cancel(self, slot_id: str) -> bool:
        s = self.slots.get(slot_id)
        if s and not s["available"]:
            s["available"] = True
            s["user"] = None
            return True
        return False

def demo():
    bs = BookingSystem()
    bs.create_slot("2025-10-01T10:00")
    print(bs.reserve("2025-10-01T10:00", "Emma"))
    print(bs.cancel("2025-10-01T10:00"))

if __name__ == "__main__":
    demo()
