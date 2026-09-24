

def mock_excel_rows():
    data = [
        {"name": "小明", "score": 85},
        {"name": "小红", "score": 92},
        {"name": "小刚", "score": 78},
    ]

    for row in data:
        yield row


def process_data():
    with open("../../demo_log.txt", "w") as log:

        scores = [row["score"] for row in mock_excel_rows()]

        print(f"{scores=}")


        log.write(f"平均分: {sum(scores) / len(scores)}")

if __name__ == '__main__':
    process_data()