from datetime import datetime

hoje = datetime.now()

dia = hoje.strftime("%d")
mes = hoje.strftime("%m")
ano = hoje.strftime("%Y")

hora = hoje.strftime("%H:%M:%S")
hora_data = hoje.strftime("~ São %H:%M:%S[%p] - Data: %d/%m/%Y")

