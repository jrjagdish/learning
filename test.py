from pathlib import Path

fake_path = Path("C:/this/does/not/exist")
print(bool(fake_path))  # True! (object exists, even if file doesn't)

real_path = Path("C:/Users")
print(bool(real_path))  # Also True

# Correct check:
print(fake_path.exists())  # False
print(real_path.exists())  # True