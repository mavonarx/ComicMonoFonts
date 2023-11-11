import fontforge

font = fontforge.open("/Users/matthiasvonarx/Library/Fonts/ComicMono/OpenType-TT/Comic Mono Regular Nerd Font.ttf")

# Set the oblique angle (adjust as needed)

italic_angle = 0.4  # Adjust this value to control the oblique effect

# Apply a shear transformation to achieve an oblique effect
font.selection.all()
font.transform([1, 0, italic_angle, 1, 0, 0])

# Set the fontname directly
font.fontname = "ComicMonoNerdFont-Italic"

# Save the obliqued font with a new name
output_path = "/Users/matthiasvonarx/Library/Fonts/ComicMono/OpenType-TT/Comic Mono Italic Nerd Font.ttf"
font.generate(output_path)

font.close()