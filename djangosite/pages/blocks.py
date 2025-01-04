from wagtail.blocks import CharBlock, PageChooserBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock


class CTACardBlock(StructBlock):
    title = CharBlock(required=True)
    page = PageChooserBlock(required=True)
    background_image = ImageChooserBlock(required=True)
    alt_text = CharBlock(required=True)

    class Meta:
        template = "blocks/cta_card_block.html"
