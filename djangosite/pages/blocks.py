from wagtail.blocks import CharBlock, PageChooserBlock, StructBlock
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
