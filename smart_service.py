import faker
from random import randint, choice, random
from src.api import get_photos_of_customers, get_product_by_id, get_accessories
from src.recognizer import recognizer
from src.functions import typewriter, align_center, clean_align_center

PROBABILITY_OF_A_CUSTOMER_HAVING_A_DEBT = 15
PROBABILITY_OF_A_CUSTOMER_HAVING_A_WITHDRAWAL = 40 
TIME_BETWEEN_VISITS = 10
NUMBER_OF_CICLOS = 100

SIZE_TO_ALIGN = 100

def start():
    recognized_customers_list = []
    report_of_old_purchases = []
    report_of_related_product = []
    withdrawal = None
    good_customer = None
    fake_data_generator = faker.Faker(locale="pt_BR")
    
    return recognized_customers_list, report_of_old_purchases, report_of_related_product, withdrawal, good_customer, fake_data_generator

def simulate_visit(visitor_photo):
    visitor = {
        "photo": visitor_photo,
        "information": None
    }
    
    return visitor

def generate_customer(visitor, fake_data_generator):
    customer = visitor
    customer["information"] = {}
    customer["information"]["name"] = fake_data_generator.name()

    return customer

def recognize_customer(visitor, photos, fake_data_generator):    
    photos = get_photos_of_customers()
    visitor_photo = visitor["photo"]
    customer = None
    
    recognized = recognizer(visitor_photo, photos)
    if recognized:
        customer = generate_customer(visitor, fake_data_generator)
    
    return recognized, customer

def generate_old_purchases_report(old_purchases_list):
    old_purchases = []
    
    for id in old_purchases_list:
        old_purchases.append(get_product_by_id(id))
    
    return old_purchases

def checks_old_purchases(customer):
    if len(customer):
        typewriter("Verificando compras antigas feitas por " + customer["information"]["name"] + ".")
        typewriter("Gerando relatório...")
        print()
        report_of_old_purchases = generate_old_purchases_report(customer["information"]["acquisitions"])
    
    return report_of_old_purchases

def format_product_to_report(product):
    product_to_return = {}
    product_to_return["id"] = product["id"]
    product_to_return["name"] = product["product"]
    
    return product_to_return

def get_related_products(id, pacessories):
    accessories = []
    
    if len(pacessories):
        for accessory in get_accessories(id):
            accessory_ = format_product_to_report(accessory)
            accessories.append(accessory_)
    else:
        accessories = None
    
    return accessories

def generate_related_product_report(report_of_old_purchases):
    product_with_related_products = []
    
    for product in report_of_old_purchases:
        
        product_= format_product_to_report(product)
        accessories = get_related_products(product["id"], product["accessories"])
        
        product_["accessories"] = accessories
        product_with_related_products.append(product_)
    
    return product_with_related_products

def checks_related_product(report_of_old_purchases):
    if len(report_of_old_purchases):
        typewriter("Verificando produtos relacionados às últimas compras.")
        typewriter("Adicionando dados ao relatório...")
        print()
        report_of_related_product = generate_related_product_report(report_of_old_purchases)
    
    return report_of_related_product

def simulate_withdrawal(acquisitions, probability):
    withdrawal = "no"
    
    if probability <= PROBABILITY_OF_A_CUSTOMER_HAVING_A_WITHDRAWAL:
        if acquisitions:
            id = choice(acquisitions)
            withdrawal = get_product_by_id(id)["product"]
    
    return withdrawal

def checks_withdrawal(customer):
    if customer:
        typewriter("Verificando retiradas em nome de " + customer["information"]["name"]+".")
        typewriter("Adicionando dados ao relatório...")
        print()
        withdrawal = customer["information"]["withdrawal"]

    return withdrawal

def customer_have_withdrawal(customer, withdrawal):
    have_withdrawal = None
    
    if customer:
        if withdrawal != "no":
            have_withdrawal = True
        else:
            have_withdrawal = False
    
    return have_withdrawal

def trigger_responsible_for_the_sector(have_withdrawal, customer_name, withdrawal):
    was_trigged = None
    
    if have_withdrawal:
        typewriter("Acionando responsável pelo setor de retiradas.")
        typewriter("O cliente: " + customer_name + " chegou para retirar o produto: " + withdrawal)
        print()
        was_trigged = True
    else:
        was_trigged = False
    
    return was_trigged

def simulate_debt(acquisitions, probability):
    debt = None
    
    if acquisitions:
        if probability <= PROBABILITY_OF_A_CUSTOMER_HAVING_A_DEBT:
            debt = randint(1, 1000) + round(random(), 2)
        else:
            debt = 0
    
    return debt

def is_a_good_customer(customer):
    good_customer = None
    good = None
    
    if customer:
        typewriter("Verificando histórico de bom cliente de " + customer["information"]["name"] + ".")
        typewriter("Adicionando dados ao relatório...")
        print()
        debt = customer["information"]["debt"] 
        if debt > 0:
            good_customer = f"Não, cliente possui uma divida de: {debt}"
            good = False
        else:
            good_customer = "Sim, cliente não possui divida"    
            good = True

    return good, good_customer

def header(name):
    align_center("RELATÓRIO COMPLETO PARA: "+ name.upper(),SIZE_TO_ALIGN)

def print_product(product):
    print()
    print("     Id do produto:", product["id"])
    print("     Produto:", product["name"])

def format_accessories(accessories):
    data = "Acessórios: [Não possui acessórios"
    
    if accessories:
        data = "Acessórios: ["
        for i in range(0, len(accessories)):
            if i < len(accessories)-1:
                product = accessories[i]
                data += product["name"] + ", "
            else:
                product = accessories[i]
                data += product["name"]
    data += "]"
    
    return data

def print_product_report(report_data):
    for product in report_data:
        print_product(product)
        accessories = format_accessories(product["accessories"])
        print("     "+accessories)

def body(report_of_related_product, withdrawal, good_customer):
    print("PRODUTO E SEUS ACESSÓRIOS:")
    print_product_report(report_of_related_product)
    print("\nRETIRADA DE PRODUTO:", withdrawal)
    print("\nBOM CLIENTE:", good_customer)

def footer():
    print()
    clean_align_center("FIM DO RELATÓRIO", SIZE_TO_ALIGN)
    print()

def final_report(customer, report_of_related_product, withdrawal, good_customer):
    final_report_shown = None
    
    if customer:
        print()
        typewriter("Imprimindo relatório final...")
        print()
        header(customer["information"]["name"])
        body(report_of_related_product, withdrawal, good_customer)
        footer()
        final_report_shown = True
    else:
        final_report_shown = False

    return final_report_shown
