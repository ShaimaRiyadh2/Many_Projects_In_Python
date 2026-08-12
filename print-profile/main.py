"""طباعة بيانات شخصية بأنواع وتنسيقات مختلفة."""

# الأنواع: نص، عدد صحيح، نص
name: str = "أحمد"
age: int = 25
city: str = "الرياض"


def main() -> None:
    print("--- 1) طباعة عادية ---")
    print(name)
    print(age)
    print(city)

    print("\n--- 2) دمج النصوص (+) ---")
    print("الاسم: " + name)
    print("العمر: " + str(age))
    print("المدينة: " + city)

    print("\n--- 3) f-string ---")
    print(f"الاسم: {name}")
    print(f"العمر: {age}")
    print(f"المدينة: {city}")

    print("\n--- 4) format ---")
    print("الاسم: {}".format(name))
    print("العمر: {}".format(age))
    print("المدينة: {}".format(city))

    print("\n--- 5) % formatting ---")
    print("الاسم: %s" % name)
    print("العمر: %d" % age)
    print("المدينة: %s" % city)

    print("\n--- 6) أنواع البيانات (type) ---")
    print(f"name -> {name!r} | type: {type(name).__name__}")
    print(f"age  -> {age!r} | type: {type(age).__name__}")
    print(f"city -> {city!r} | type: {type(city).__name__}")


if __name__ == "__main__":
    main()
