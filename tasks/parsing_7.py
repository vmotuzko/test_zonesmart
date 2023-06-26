"""
Сайт: https://parsinger.ru/html/index1_page_1.html
Получить ссылки на страницы всех товаров, запросить все страницы (крайне желательно сделать это асинхронно)
и собрать оттуда значения поля “В наличии”. В результате должен получиться словарь [URL]->[в наличии]
"""

import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def get_product_links(session, url):
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        for img_box in soup.find_all('div', class_='img_box'):
            link = img_box.find('a', href=True)
            if link:
                links.append(link['href'])
        return links


async def get_in_stock_quantity(session, url):
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        in_stock = soup.find('span', id='in_stock')
        return in_stock.text.replace('В наличии:', '').strip()


async def get_total_pages(session, url):
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        pagination = soup.find('div', class_='pagen')
        last_page = pagination.find_all('a')[-1].text.strip()
        return int(last_page)


async def parse_data(base_url, start_page: str) -> dict:
    if base_url[-1] != '/':
        base_url += '/'

    async with aiohttp.ClientSession() as session:
        total_pages = await get_total_pages(session, f'{base_url}{start_page}')

        tasks = []
        for page in range(1, total_pages):
            tasks.append(asyncio.create_task(get_product_links(session, f'{base_url}index1_page_{page}.html')))

        links_result = await asyncio.gather(*tasks)

        tasks = []
        for product_links in links_result:
            for link in set(product_links):
                full_url = f'{base_url}{link}'
                tasks.append(asyncio.create_task(get_in_stock_quantity(session, full_url), name=full_url))

        product_results = await asyncio.gather(*tasks)

        in_stock_data = {}
        for i, result in enumerate(product_results):
            url = tasks[i].get_name()
            in_stock_data[url] = result
        return in_stock_data

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(parse_data('https://parsinger.ru/html/', 'index1_page_1.html'))
    loop.close()
    print(data)
