from datetime import datetime

def send_date(data_str):
    data_input = input(data_str)
    try:
        return datetime.strptime(data_input, "%d/%m/%Y").date()
    except ValueError:
        print("Data inválida. Use o formato DD/MM/AAAA.")
        return None

def show_date(data_str):
    try:
        data = datetime.strptime(str(data_str), "%Y-%m-%d")
        return data.strftime("%d/%m/%Y")
    except ValueError:
        return str(data_str)