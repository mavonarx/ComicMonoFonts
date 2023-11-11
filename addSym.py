import fontforge

font_to_add_symbols = fontforge.open("/Users/matthiasvonarx/Library/Fonts/ComicMono/OpenType-TT/Comic Mono Regular Nerd Font.ttf")
font_with_symbols = fontforge.open("/Users/matthiasvonarx/Library/Fonts/Fantasque Sans Mono Regular Nerd Font Complete Mono.ttf")

existing_glyphs = set(font_to_add_symbols)

for glyph_name in font_with_symbols:
    # Copy the glyph if it doesn't already exist in the target font
    if glyph_name not in existing_glyphs:
        glyph = font_with_symbols[glyph_name]
        unicode_value = glyph.unicode
        if unicode_value is not None:
            font_to_add_symbols.createChar(int(unicode_value, 16), glyph.glyphname)
            font_to_add_symbols[int(unicode_value, 16)].importOutlines(glyph)


# Save and close the fonts
font_to_add_symbols.generate("/Users/matthiasvonarx/Library/Fonts/ComicMono/OpenType-TT/Comic Mono Italic Nerd Font.ttf")
font_to_add_symbols.close()
font_with_symbols.close()