from selenium import webdriver

URL_PLANILHA = "https://docs.google.com/spreadsheets/d/1UuQvg3g8vhNRayUq5HtdCGjIT1fNJXDjZDX3BgO1QLM/edit?usp=sharing"

print("Iniciando Chrome...")

try:
    driver = webdriver.Chrome()
    driver.maximize_window()

    print("Abrindo Google Planilhas...")
    driver.get(URL_PLANILHA)

    print("Planilha aberta no navegador!")

    input("Pressione ENTER para fechar o Chrome...")

    driver.quit()

except Exception as erro:
    print(f"ERRO: {erro}")
    input("Pressione ENTER para encerrar...")