import gspread
from google.oauth2.service_account import Credentials
import json

# Definir los alcances manualmente
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Cargar credenciales con los nuevos scopes
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

# Abrir la hoja de cálculo
SHEET_ID = "1t3SZc7Ab1vd8cTYOLH-Yd3fTtQqVNJ1esFWw78fe5W0"  # Tu ID de Sheets
worksheet = client.open_by_key(SHEET_ID).sheet1  

# Obtener lista de IDs desde la primera columna
player_ids = worksheet.col_values(1)

# Guardar los IDs en un archivo JSON
with open("player_ids.json", "w") as file:
    json.dump(player_ids, file)

print("IDs guardados correctamente en 'player_ids.json'.")