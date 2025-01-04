from wagtail.blocks import CharBlock, PageChooserBlock, RichTextBlock, StructBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock


class CTACardBlock(StructBlock):
    title = CharBlock(required=True)
    page = PageChooserBlock(required=True)
    background_image = ImageChooserBlock(required=True)
    alt_text = CharBlock(required=True)

    class Meta:
        template = "blocks/cta_card_block.html"
        label = "Call to Action Card"


class CoreTeamBlock(StructBlock):
    name = CharBlock(required=True)
    role = CharBlock(required=True)
    image = ImageChooserBlock(required=False)

    class Meta:
        template = "blocks/core_team_block.html"
        label = "Core Team Member"


class BoardMemberBlock(StructBlock):
    name = CharBlock(required=True)
    position = CharBlock(required=True)

    class Meta:
        template = "blocks/board_member_block.html"
        label = "Board Member"


class FormBlock(StructBlock):
    title = CharBlock(required=True)
    description = CharBlock(required=False)
    document = DocumentChooserBlock(required=True)

    class Meta:
        template = "blocks/form_block.html"
        label = "Form Download"


class AccordionItemBlock(StructBlock):
    title = CharBlock(required=True)
    content = RichTextBlock()

    class Meta:
        template = "blocks/accordion_item_block.html"
        label = "Accordion/Collapsible Item"
