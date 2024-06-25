from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from clockReader import clockReader
from pharse import createPharse
from unidecode import unidecode
from dotenv import load_dotenv
import requests
import time
import os

load_dotenv()

def geraNomeUsuario():
    url = "https://randomuser.me/api/?nat=br"
    response = requests.get(url)
    if response.ok:
        for result in response.json()["results"]:
            nome_completo = f"{result['name']['first']} {result['name']['last']}"
            nome_formatado = unidecode(nome_completo).lower().replace(" ", ".")
            return nome_formatado
    else:
        return f"Erro ao acessar a API: {response.status_code}"

def clicaCadastrar(driver):
    xpath = "/html/body/div/div[3]/div[3]/div/div[1]/div[2]/button[1]"
    script = """
    var xpath = arguments[0];
    var button = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if (button) {
        button.click();
    } else {
        console.error("Botão não encontrado");
    }
    """

    try:
        driver.execute_script(script, xpath)
        print(f"Botão 'Cadastre-se' foi clicado com sucesso")
    except Exception as e:
        print(f"Erro ao clicar no botão: {e}")


def clicaSelecionar(driver):
    xpath = "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div[1]/div[1]/div/div/div[5]/button"
    script = """
    var xpath = arguments[0];
    var button = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if (button) {
        button.click();
    } else {
        console.error("Botão não encontrado");
    }
    """

    try:
        driver.execute_script(script, xpath)
        print(f"Botão 'Selecionar' foi clicado com sucesso")
    except Exception as e:
        print(f"Erro ao clicar no botão: {e}")


def clicaInputsContrato(driver):
    xpath_I = "/html/body/div/div[2]/div[2]/div/div/div/div[2]/div[1]/label/input"
    script_I = """
    var xpath = arguments[0];
    var button = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if (button) {
        button.click();
    } else {
        console.error("Input não encontrado");
    }
    """

    xpath_II = "/html/body/div/div[2]/div[2]/div/div/div/div[2]/div[2]/label/input"
    script_II = """
    var xpath = arguments[0];
    var button = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if (button) {
        button.click();
    } else {
        console.error("Input não encontrado");
    }
    """

    try:
        time.sleep(1)
        driver.execute_script(script_I, xpath_I)
        print(f"Input 'Não possuo outras contas gratuitas' foi clicado com sucesso")

        time.sleep(1)
        driver.execute_script(script_II, xpath_II)
        print(
            f"Input 'Não usarei essa conta para fins empresariais' foi clicado com sucesso"
        )
    except Exception as e:
        print(f"Erro ao clicar em algum input: {e}")


def clicaOk(driver):
    xpath = "/html/body/div/div[2]/div[2]/div/div/div/div[3]/button[2]"
    script = """
    var xpath = arguments[0];
    var button = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if (button) {
        button.click();
    } else {
        console.error("Botão não encontrado");
    }
    """

    try:
        driver.execute_script(script, xpath)
        print(f"Botão 'Ok' foi clicado com sucesso")
    except Exception as e:
        print(f"Erro ao clicar no botão: {e}")


def clicaInputsEmail(driver):
    xpath_I = "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[1]/input"
    texto_I = geraNomeUsuario()
    script_I = """
    var xpath = arguments[0];
    var inputElement = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    var texto = arguments[1];
    if (inputElement) {
        inputElement.value = texto;
        inputElement.dispatchEvent(new Event('input', { bubbles: true }));
    } else {
        console.error("Input não encontrado");
    }
    """

    xpath_II = "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/input"
    texto_II = "Og(O*+;3a1"
    script_II = """
    var xpath = arguments[0];
    var inputElement = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    var texto = arguments[1];
    if (inputElement) {
        inputElement.value = texto;
        inputElement.dispatchEvent(new Event('input', { bubbles: true }));
    } else {
        console.error("Input não encontrado");
    }
    """

    xpath_III = "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/input"
    texto_III = "Og(O*+;3a1"
    script_III = """
    var xpath = arguments[0];
    var inputElement = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    var texto = arguments[1];
    if (inputElement) {
        inputElement.value = texto;
        inputElement.dispatchEvent(new Event('input', { bubbles: true }));
    } else {
        console.error("Input não encontrado");
    }
    """

    try:
        time.sleep(1)
        driver.execute_script(script_I, xpath_I, texto_I)
        print(f"Input 'Endereço de email' foi preenchido com sucesso")

        time.sleep(1)
        driver.execute_script(script_II, xpath_II, texto_II)
        print(f"Input 'Crie sua senha' foi preenchido com sucesso")

        time.sleep(1)
        driver.execute_script(script_III, xpath_III, texto_III)
        print(f"Input 'Repita sua senha' foi preenchido com sucesso")
    except Exception as e:
        print(f"Erro ao clicar em algum input: {e}")


def clicaInputsTermos(driver):
    xpath_I = "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[3]/label/input"
    script_I = """
    var xpath = arguments[0];
    var button = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if (button) {
        button.click();
    } else {
        console.error("Input não encontrado");
    }
    """

    xpath_II = "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[4]/label/input"
    script_II = """
    var xpath = arguments[0];
    var button = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if (button) {
        button.click();
    } else {
        console.error("Input não encontrado");
    }
    """

    try:
        time.sleep(1)
        driver.execute_script(script_I, xpath_I)
        print(
            f"Input 'Eu li e concordo com os seguintes documentos' foi clicado com sucesso"
        )

        time.sleep(1)
        driver.execute_script(script_II, xpath_II)
        print(f"Input 'Eu tenho 16 anos ou mais' foi clicado com sucesso")
    except Exception as e:
        print(f"Erro ao clicar em algum input: {e}")


def clicaProximo(driver):
    xpath = (
        "/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[5]/button"
    )
    script = """
    var xpath = arguments[0];
    var button = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if (button) {
        button.click();
    } else {
        console.error("Botão não encontrado");
    }
    """

    try:
        driver.execute_script(script, xpath)
        print(f"Botão 'Próximo' foi clicado com sucesso")
    except Exception as e:
        print(f"Erro ao clicar no botão: {e}")


def resolveRecaptcha(driver):
    xpath_image = "/html/body/div/div[2]/div[3]/div/div/div/div[2]/img"
    script_get_image_src = """
        var xpath = arguments[0];
        var img = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (img) {
            var src = img.src;
            if (src.startsWith("data:image/png;base64,")) {
                src = src.replace("data:image/png;base64,", "");
            }
            return src;
        } else {
            console.error("Imagem não encontrada");
            return null;
        }
    """

    try:
        src = driver.execute_script(script_get_image_src, xpath_image)
        if src:
            print(f"Fonte da imagem sem prefixo: {src}")
            try:
                horas = clockReader(src) 
                xpath_input = "/html/body/div/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/div/input"
                script_set_input_value = """
                    var xpath = arguments[0];
                    var inputElement = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                    var value = arguments[1];
                    if (inputElement) {
                        inputElement.value = value;
                        inputElement.dispatchEvent(new Event('input', { bubbles: true }));
                    } else {
                        console.error("Input não encontrado");
                    }
                """
                print(f"Horas detectadas: {horas}")
                driver.execute_script(script_set_input_value, xpath_input, horas)
            except Exception as e:
                print(f"Erro ao executar o script para preencher o input: {e}")
        else:
            print("Erro ao obter a fonte da imagem")
    except Exception as e:
        print(f"Erro ao executar o script para obter a imagem: {e}")

funcoes = [
    clicaCadastrar,
    clicaSelecionar,
    clicaInputsContrato,
    clicaOk,
    clicaInputsEmail,
    clicaInputsTermos,
    clicaProximo,
    resolveRecaptcha
]

def main():
    print(createPharse())

    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)
    driver.get("https://app.tuta.com/login?noAutoLogin=true&keepSession=true")
    
    for funcao in funcoes:
        time.sleep(int(os.getenv("INTERVAL")))
        funcao(driver)

    time.sleep(600)
    driver.quit()

main()