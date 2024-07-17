from bs4 import BeautifulSoup
import requests


class EbayScrap:
    def __init__(self, url):
        self.url = url

    def url_handling(self):
        html_text = requests.get(self.url).text
        return BeautifulSoup(html_text, 'lxml')

    def item_summary(self):
        soup = self.url_handling()
        return soup.find('div', class_='right-summary-panel-container vi-mast__col-right')

    def item_image(self):
        soup = self.url_handling()
        return soup.find('div', class_='picture-panel-container vi-mast__col-left')

    def get_item_image(self):
        picture_scrap = self.item_image().find('img')
        image_src = picture_scrap['src']
        return f'Image: {image_src}'

    def get_item_info(self):
        summary_name = self.item_summary().find('div', class_='vim x-item-title')
        item_name = summary_name.find('span', class_='ux-textspans ux-textspans--BOLD').text

        summary_price = self.item_summary().find('div', class_='vim x-price-section mar-t-20')
        item_price = summary_price.find('span', class_='ux-textspans').text

        summary_seller = self.item_summary().find('div', class_='x-sellercard-atf__info')
        item_seller = summary_seller.find('span', class_='ux-textspans ux-textspans--BOLD').text

        summary_shipping = self.item_summary().find('div', class_='vim d-shipping-minview mar-t-20')
        item_shipping = summary_shipping.find('span', class_='ux-textspans ux-textspans--BOLD').text
        return (f'Name: {item_name}\n Price: {item_price}\n '
                f'Seller: {item_seller}\n Shipping: {item_shipping}\n '
                f'Link: {self.url}')


ebay_scrap = EbayScrap(
    'https://www.ebay.com/itm/355173902208?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1'
    '%26asc%3D264183%26meid%3D4400fe09861f42fe942d6ce539d5656b%26pid%3D101224%26rk%3D2%26rkt%3D5%26sd%3D186053347939'
    '%26itm%3D355173902208%26pmt%3D0%26noa%3D1%26pg%3D2332490%26algv'
    '%3DDefaultOrganicWebV9BertRefreshRankerWithCassiniEmbRecall&_trksid=p2332490.c101224.m-1')

print(ebay_scrap.get_item_info())
print(ebay_scrap.get_item_image())
