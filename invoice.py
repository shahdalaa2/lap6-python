from dataclasses import dataclass
from enum import Enum

HOURLY_RATE = 350
STAFF_CHILD_DISCOUNT = 0.5
SIBLING_DISCOUNT_RATE = 0.1
HIGH_FEE_THRESHOLD = 6000
HIGH_FEE_REDUCTION = 200
SUMMER_SURCHARGE = 150

class StudentType(Enum):
    REGULAR = 1
    STAFF_CHILD = 2
    SCHOLARSHIP = 3

@dataclass(frozen=True)
class Course:
    hours: int

@dataclass(frozen=True)
class SiblingPolicy:
    enabled: bool = False
    rate: float = SIBLING_DISCOUNT_RATE

    def apply(self, amount):
        if not self.enabled:
            return amount
        return amount * (1.0 - self.rate)

def tuition_fee(courses, student_type, summer=False, discount=None, extra=(), sibling_policy=SiblingPolicy()):
    total = 0
    for course in courses:
        if student_type == StudentType.REGULAR:
            total += course.hours * HOURLY_RATE
        elif student_type == StudentType.STAFF_CHILD:
            total += course.hours * HOURLY_RATE * STAFF_CHILD_DISCOUNT
        elif student_type == StudentType.SCHOLARSHIP:
            total += 0
    total = sibling_policy.apply(total)
    if total > HIGH_FEE_THRESHOLD:
        total -= HIGH_FEE_REDUCTION
    if summer:
        total += SUMMER_SURCHARGE
    if discount is not None:
        total -= discount
    for item in extra:
        total += item
    return total

def process_all(students, sibling_policy=SiblingPolicy()):
    results = {}
    for st in students:
        results[st["name"]] = tuition_fee(st["courses"], st["type"], summer=st.get("summer", False), sibling_policy=sibling_policy)
    return results
