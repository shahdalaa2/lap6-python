# Completed Code Smells Table (Task C1)

| Code Smell | Location in Legacy Code | Refactoring Applied (Task C2) |
| --- | --- | --- |
| Magic Numbers & Codes | 350, 0.5, 6000, 200, 150, and t (1, 2, 3) | Extracted named constants and StudentType Enum |
| Long Parameter List & Primitive Obsession | calc(d, t, y, s, disc, extra=[]) with raw dicts/flags | Introduced Course dataclass and SiblingPolicy object |
| Duplicate / Scattered Fee Logic | Repeated conditional/fee calculations across calc, report, and batch logic | Centralized calculation in tuition_fee and process_all |
| Dead / Unused Code & Side Effects | Unused variables/imports (os, math, tmp) and print inside report | Removed dead code and separated pure calculation from reporting |
