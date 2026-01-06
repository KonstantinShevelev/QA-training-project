contacts = dict(
    **{
        "Анна Иванова": dict(
            phone="+79001234567",
            email="anna.ivanova@example.com"
        ),
        "Петр Сидоров": dict(
            phone="+79119876543",
            email="petr.sidorov@example.com"
        )
    }
)

print(f"Анна Иванова: {contacts['Анна Иванова']}")
contacts["Петр Сидоров"]["phone"] = "+79225551122"
contacts["Анна Иванова"]["address"] = "Москва, ул. Пушкина, д. 10"
del contacts["Петр Сидоров"]["email"]
print(f"Контакты: {contacts}")

