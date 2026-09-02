"""Gera os QR Codes do cartão digital.
Uso: python3 gerar-qr.py [URL_DO_SITE]
Se a URL for informada, gera também o QR do cartão online."""
import sys, qrcode
from qrcode.image.styledpil import StyledPilImage
INK = (46, 43, 42)
def gera(dado, nome):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=12, border=2)
    qr.add_data(dado); qr.make(fit=True)
    img = qr.make_image(fill_color=INK, back_color="white")
    img.save(nome); print("ok", nome, img.size)
vcard = open("../../cassia-naujalis.vcf", encoding="utf-8").read()
gera(vcard, "qr-vcard.png")
gera("https://wa.me/5544998594288?text=Ol%C3%A1%20Cassia!%20Vi%20seu%20portf%C3%B3lio%20e%20quero%20conversar.", "qr-whatsapp.png")
if len(sys.argv) > 1:
    gera(sys.argv[1], "qr-site.png")
