import requests
from bs4 import BeautifulSoup
import tqdm

from include.models import Vacante

import pandas as pd
    
class OCCScrapper:
    def __init__(self) -> None:
        self.root_url = 'https://www.occ.com.mx/'
        self.last_page = self.get_last_page()

        self.href_elements = []
        self.vacantes = []

    def get_last_page(self) -> None:
        url = 'https://www.occ.com.mx/empleos/en-chihuahua/'
        response = requests.get(url)
        with open('data/page.html', 'w') as file:
            file.write(response.text)
            file.close()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Encuentra todos los elementos li que listan las paginas disponibles
        elementos_li = soup.select('ul.desktopPager-0-2-620 li.li-0-2-630')
        print(elementos_li)
        # Obtiene el numero mas alto para iterar

        numeros = [int(elemento_li.get_text(strip=True)) for elemento_li in elementos_li]
        
        return max(numeros)

    def get_page_objects(self, page=None) -> None:
        if not page:
            url = 'https://www.occ.com.mx/empleos/en-chihuahua/'
        else:
            url = 'https://www.occ.com.mx/empleos/en-chihuahua/?page='+str(page)
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            
            # Encuentra todos los elementos 'a' que tienen la clase 'jobcard-0-2-563'
            elementos_a = soup.find_all('a', class_='jobcard-0-2-563')
            # Itera a través de los elementos 'a' y obtén los valores de 'href'
            for elemento_a in elementos_a:
                self.href_elements.append(self.root_url+elemento_a.get('href'))

    def get_all_href(self) -> None:
        for page in tqdm.tqdm(range(2, 4)):
            self.get_page_objects(page)

        pd.DataFrame(self.href_elements, columns=['url']).to_csv('data/href.csv', index=False)


    def get_all_attributes(self) -> None:
        for url in tqdm.tqdm(self.href_elements):
            self.get_attributes(url)

        pd.DataFrame.from_records(self.get_records()).to_csv('data/records2.csv', index=False)


    def get_attributes(self, url) -> None:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Header
            try:
                header = soup.find('p', class_='heading-0-2-85').text
            except:
                header = ''
            # Extraer la categoría
            try:    
                categoria = soup.find('span', text="Categoría: ").find_next('span').text
            except:
                categoria=''
            # Extraer la subcategoría
            try:
                subcategoria = soup.find('span', text="Subcategoría: ").find_next('span').text
            except:
                subcategoria=''
            # Extraer la educación mínima requerida
            try:
                educacion_minima = soup.find('span', text="Educación mínima requerida: ").find_next('span').text
            except:
                educacion_minima=''
            # Extrae la compañia que agrego la vacante
            try:
                company = soup.find('span', class_='text-0-2-82 standard-0-2-89 highEmphasis-0-2-103 strong-0-2-92').text
            except:
                company=''

            # Encuentra el job description
            job_body = soup.find('div', id='jobbody')
            # Crea el objeto vacante
            self.vacantes.append(
                Vacante(
                    url, 
                    header, 
                    job_body.text,
                    categoria,
                    subcategoria,
                    educacion_minima,
                    company
                )
            )

    def get_records(self) -> list:
        records = []

        for vacante in self.vacantes:
            records.append(vacante.to_record())

        return records